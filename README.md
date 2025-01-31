# Chat Assistant for SQLite Database

## Overview

This project is a **FastAPI-based Chat Assistant** that interacts with an SQLite database. It uses **spaCy NLP** to process natural language queries and convert them into SQL queries to fetch relevant data.

## Features

- Accepts natural language queries.
- Converts queries into SQL statements dynamically.
- Fetches and returns structured data from an SQLite database.
- Handles errors gracefully.
- Deployed using FastAPI.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- SQLite
- pip (Python package manager)

### Clone the Repository

```sh
git clone <repo_url>
cd chat-assistant-sqlite
```

### Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Initialize the Database

```sh
python -c "from main import init_db; init_db()"
```

### Run the Server

```sh
uvicorn main:app --reload
```

The server will start at: `http://127.0.0.1:8000`

## API Usage

### Query Endpoint

- **Endpoint**: `POST /query`
- **Request Body (JSON format)**:

```json
{
  "query": "Show me all employees in Sales department."
}
```

- **Response (Example)**:

```json
{
  "employees": ["Alice"]
}
```

## Deployment

To deploy this project, use **Docker**, **Render**, or **Railway**.

Example Docker usage:

```sh
docker build -t chat-assistant .
docker run -p 8000:8000 chat-assistant
```

## Improvements

- Enhance NLP model for better entity recognition.
- Add a front-end UI.
- Improve error handling and logging.

## License

MIT License
