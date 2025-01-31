# Chat Assistant with SQLite

This is a FastAPI-powered web application that allows users to query an SQLite database and get formatted responses based on predefined queries. It supports basic SQL queries like listing employees from a department, getting the manager of a department, listing employees hired after a certain date, and more.

The app includes a simple UI where users can type natural language queries, and it returns results in a user-friendly format.

## Features

- **FastAPI Backend**: Fast, modern web framework for building APIs.
- **SQLite Database**: Lightweight, serverless, self-contained SQL database engine.
- **Intuitive UI**: A simple web interface where users can type queries and see results.
- **Dockerized**: Easily deployable using Docker.
- **Public URL**: Hosted on platforms like Railway or Render for free.

## Project Structure

```
chat-assistant-sqlite/
├── company.db            # SQLite database file
├── Dockerfile            # Dockerfile for deployment
├── main.py               # FastAPI application logic
├── requirements.txt      # Python dependencies
├── static/               # Static files like CSS, JS
├── templates/            # HTML templates for the UI
└── .dockerignore         # Files to exclude from Docker image
```

### Tables in the Database

#### Employees Table

| ID  | Name    | Department  | Salary | Hire_Date  |
| --- | ------- | ----------- | ------ | ---------- |
| 1   | Alice   | Sales       | 50000  | 2021-01-15 |
| 2   | Bob     | Engineering | 70000  | 2020-06-10 |
| 3   | Charlie | Marketing   | 60000  | 2022-03-20 |

#### Departments Table

| ID  | Name        | Manager |
| --- | ----------- | ------- |
| 1   | Sales       | Alice   |
| 2   | Engineering | Bob     |
| 3   | Marketing   | Charlie |

## Getting Started

Follow these steps to set up and run the application locally or deploy it.

### Prerequisites

- Python 3.9+
- Docker (optional, if you want to run the app in a container)

### Installing Locally

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/chat-assistant-sqlite.git
   cd chat-assistant-sqlite
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the app at `http://127.0.0.1:8000`.

4. You can visit the UI at `http://127.0.0.1:8000/` and start interacting with the app by typing queries.

### Dockerizing the App

1. **Build the Docker image**:

   ```bash
   docker build -t chat-assistant-sqlite .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 8000:8000 chat-assistant-sqlite
   ```

3. Your app will be available at `http://127.0.0.1:8000` in the browser.

### Deploying to Railway

You can deploy this app to Railway for free with the following steps:

1. Go to [Railway](https://railway.app/) and sign up or log in.
2. Create a new project and select **"Deploy from GitHub"**.
3. Link your GitHub account and select the repository you just created.
4. Railway will automatically detect the `Dockerfile` and deploy your app.
5. After deployment, Railway will provide a public URL to access the app.

## UI Interaction

Once deployed or running locally, you can interact with the app through the following types of queries:

- **"Show me all employees in the Sales department."**
- **"Who is the manager of the Engineering department?"**
- **"List all employees hired after 2021-01-01."**
- **"What is the total salary expense for the Marketing department?"**

The app will return formatted results for these queries, and you can ask more based on the supported types.

## File and Database Structure

- The app is initialized with a sample SQLite database (`company.db`) containing tables for **Employees** and **Departments**.
- You can modify the database by adding more employees, departments, or changing existing data.
