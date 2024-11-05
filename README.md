# Web-Scraping and Question Generation Application

A full-stack web application for scraping websites, extracting keywords, and generating relevant questions for user engagement. This project uses **Flask** for the backend and **React** with **Redux** for the frontend.

## Features

- **Web Scraping**: Scrapes content from the specified website URL and extracts key information.
- **Keyword Extraction**: Identifies important keywords from the scraped content.
- **Question Generation**: Generates questions based on the extracted keywords to classify user interests.
- **Global State Management**: Utilizes Redux for managing state across React components.

## Getting Started

### Prerequisites
- [Python](https://www.python.org/downloads/) (v3.8 or above)
- [Node.js](https://nodejs.org/) and npm
- [PostgreSQL](https://www.postgresql.org/download/)
- [Redis](https://redis.io/download)

## Backend Overview (`app.py`)

The backend is built with **Flask** and handles web scraping, keyword extraction, and question generation.

#### Key Responsibilities:
- **Flask Setup**: Initializes the Flask app and configures necessary settings.
- **API Endpoint**: Defines an endpoint for triggering web scraping.
- **Web Scraping Logic**: Implements scraping functions to extract content from the target website.
- **Keyword Extraction**: Parses content for relevant keywords.
- **Question Generation**: Produces questions based on keywords to classify visitor interests.

## Frontend Overview

The frontend is a **React** application structured with Redux for state management. It manages user input, renders results, and handles data flow from backend to frontend.

### Entry Point (`index.tsx`)

The entry point of the React app, where the main **App** component is wrapped with the **Redux Provider**.

- **Purpose**: Sets up and configures the app's Redux store, making the global state accessible throughout the app.

### Main Component (`App.tsx`)

The primary component of the frontend application.

- **Responsibilities**:
  - Renders the user interface and accepts user input (e.g., website URL).
  - Dispatches actions to request generated questions from the backend.
  - Displays the fetched questions and options to the user.

### Redux Store (`redux/store.ts`)

The Redux store configuration file.

- **Responsibilities**:
  - Creates and configures the Redux store.
  - Combines reducers for better state management.
  - Applies middleware like Redux Thunk for handling asynchronous actions.

### Redux Actions (`redux/actions.ts`)

Defines the Redux actions used across the application.

- **Responsibilities**:
  - Creates action types and action creators for Redux.
  - Handles asynchronous actions such as API calls to fetch questions.

### Redux Reducers (`redux/reducers.ts`)

Manages state changes in response to dispatched actions.

- **Responsibilities**:
  - Updates the application state in an immutable way.
  - Defines how the state should change based on various actions.

## Configuration

### API Key Setup

To access the OpenAI API for generating questions:

1. Sign up for an OpenAI account at [OpenAI Sign Up](https://beta.openai.com/signup/).
2. Navigate to the API keys section in your account dashboard and create a new API key.

**Setting the API Key**:
- Store your API key securely in a `.env` file in the project root.
- Add a line to the `.env` file as follows:
  ```plaintext
  OPENAI_API_KEY=your-api-key-here
