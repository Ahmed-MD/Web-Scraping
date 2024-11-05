from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import random
import redis
import psycopg2
from psycopg2.extras import RealDictCursor
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

nltk.download('punkt')
nltk.download('stopwords')

# Redis setup
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# PostgreSQL setup
conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

# OpenAI setup
openai.api_key = os.getenv('OPENAI_API_KEY')

def scrape_website(url):
    # Check Redis cache first
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Cache the result in Redis
    redis_client.setex(url, 3600, text)  # Cache for 1 hour

    return text

def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    filtered_words = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return Counter(filtered_words).most_common(10)

def generate_ai_questions(keywords):
    prompt = f"Generate 5 multiple-choice questions to classify website visitors based on their interests or industry. Use these keywords as context: {', '.join([k[0] for k in keywords])}. Format each question with 4 options."

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    questions = response.choices[0].text.strip().split('\n\n')
    formatted_questions = []

    for q in questions:
        lines = q.split('\n')
        question_text = lines[0].strip()
        options = [opt.strip()[3:] for opt in lines[1:]]  # Remove the "a. ", "b. ", etc.
        formatted_questions.append({
            'text': question_text,
            'options': options
        })

    return formatted_questions

def store_questions(url, questions):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            INSERT INTO questions (url, questions_data)
            VALUES (%s, %s)
            ON CONFLICT (url) DO UPDATE
            SET questions_data = EXCLUDED.questions_data
        """, (url, psycopg2.extras.Json(questions)))
    conn.commit()

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json['url']
    content = scrape_website(url)
    keywords = extract_keywords(content)
    questions = generate_ai_questions(keywords)
    store_questions(url, questions)
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)