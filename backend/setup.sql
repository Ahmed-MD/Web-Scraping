CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    url TEXT UNIQUE NOT NULL,
    questions_data JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_questions_url ON questions(url);