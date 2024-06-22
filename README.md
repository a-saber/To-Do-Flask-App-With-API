# Flask To-Do App

A simple to-do application built with Flask, providing both a web interface and a RESTful API.

## Features

- Add and list to-do items via a web interface
- API endpoints for managing to-do items
- SQLite database for persistent storage

## Requirements

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- pytest (for testing)
- pytest-flask (for testing)

## Setup

1. **Clone the repository**:

2. **Go inside the project**:
    ```bash
    cd ToDO
    ```
3. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
4. **Activate the virtual environment:**
- on macOS/Linux:
     ```bash
    source venv/bin/activate
    ```
- on Windows:
     ```bash
    venv\Scripts\activate
    ```
5. **Install the dependencies:**
     ```bash
    pip install -r requirements.txt
    ```
6. **Run the app:**
- For Development:  
    ```bash
    python app.py
    ```

- For Production:  
    ```bash
    gunicorn -w 4 -b 127.0.0.1:8000 wsgi:application
    ```

## Usage

### Web Interface
1. Open your web browser and navigate to 
http://127.0.0.1:5000/ (for development) or http://127.0.0.1:8000/ (for production).

2. Add a new to-do item using the form.
3. View the list of to-do items on the homepage.

### API Endpoints

1. Get all to-do items:
    ```bash
        GET /api/todos
    ```
2. Create a new to-do item::
    ```bash
        POST /api/todos
    ```
    Request body:
    {
        "title": "New Todo"
    }


## Running Tests

1.**Run all tests:**
    ```bash
        pytest
    ```




