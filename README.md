Spy_cats Spy Cat Agency API

This project implements the backend system for the Spy Cat Agency, which manages spy cats, missions, and targets. It provides CRUD functionalities to add, update, and delete cats, missions, and their corresponding targets.

Setup and Installation

Prerequisites:
- Python 3.8 or later
- pip for managing dependencies

Step 1: Clone the repository

Clone this repository to your local machine using Git:

https://github.com/AntonVydyborets/Spy_cats

Step 2: Install dependencies

Create a virtual environment and install the required dependencies:

python -m venv env
source env/bin/activate  # For Mac/Linux
env\Scripts\activate  # For Windows

pip install -r requirements.txt

Step 3: Configure SQLite

SQLite does not require a separate database server, making it easier to set up locally.

1. Edit the `database.py` file to configure SQLite as your database. Change the `DATABASE_URL` connection string to use SQLite:

DATABASE_URL = "sqlite:///./spy_cat_agency.db"

This will create an SQLite database file named `spy_cat_agency.db` in your project directory.

Step 4: Run database migrations

Now that the SQLite database is set up, run the database migrations to create the required tables:

alembic upgrade head

Step 5: Start the FastAPI server

Once the database setup is complete, start the FastAPI server:

uvicorn main:app --reload

Your FastAPI server should now be running at http://localhost:8000.

Postman Collection - https://github.com/AntonVydyborets/Spy_cats/blob/main/Spy%20cats.postman_collection.json

You can find the Postman collection in the app directory for testing the API:

Spy Cats Postman Collection

