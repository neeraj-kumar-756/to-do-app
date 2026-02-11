# Flask To-Do List Application

A simple, user-based to-do list web application built with Python and Flask. This project allows users to register, log in, and manage their own personal tasks.

## Features

- **User Authentication**: Secure user registration and login system.
- **Persistent Storage**: User and task data are stored in a SQLite database.
- **Task Management**: Users can add, view, and clear their own tasks.
- **Status Toggling**: Mark tasks as "Pending" or "Done".
- **Clean UI**: A simple and intuitive interface for managing tasks.

## Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite with Flask-SQLAlchemy
- **Forms**: Flask-WTF
- **Frontend**: HTML, CSS

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd to-do-app
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install Flask Flask-SQLAlchemy Flask-WTF Werkzeug email-validator
    ```

4.  **Run the application:**
    ```bash
    python run.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.