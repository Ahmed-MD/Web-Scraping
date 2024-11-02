from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import random



app = Flask(__name__)
CORS(app)


def ensure_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')

ensure_nltk_data()

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')  # This line ensures punkt_tab is downloaded
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return text

def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    filtered_words = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return Counter(filtered_words).most_common(10)

def generate_questions(keywords):
    industries = ['Technology', 'Finance', 'Healthcare', 'Education', 'Entertainment']
    questions = []
    
    for keyword, _ in keywords:
        question = {
            'text': f'How interested are you in {keyword}?',
            'options': ['Very interested', 'Somewhat interested', 'Not interested']
        }
        questions.append(question)
    
    industry_question = {
        'text': 'Which industry best describes your interests?',
        'options': industries
    }
    questions.append(industry_question)
    
    return questions

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json['url']
    content = scrape_website(url)
    keywords = extract_keywords(content)
    questions = generate_questions(keywords)
    return jsonify(questions)

if __name__ == '__main__':

    app.run(debug=True)


