Spy_cats
Spy Cat Agency API This project implements the backend system for the Spy Cat Agency , which manages spy cats, missions, and targets. It provides CRUD functionalities to add, update, and delete cats, missions, and their corresponding targets.

Setup and Installation Prerequisites Python 3.8 or later PostgreSQL installed and running pip for managing dependencies Step 1: Clone the repository Clone this repository to your local machine using Git:

bash
Копіювати код
git clone https://github.com/yourusername/spy-cat-agency.git
cd spy-cat-agency
Step 2: Install dependencies
Create a virtual environment and install required dependencies:

bash
Копіювати код
python -m venv env
source env/bin/activate  # For Mac/Linux
env\Scripts\activate  # For Windows

pip install -r requirements.txt Step 3: Configure PostgreSQL Make sure your PostgreSQL database is set up. You can use a local or remote PostgreSQL instance. Create a database for the project and update the DATABASE_URL in database.py with the connection string to your database:

python
Копіювати код
DATABASE_URL = "postgresql://user:password@localhost/spy_cat_agency"
Step 4: Run database migrations
Run the database migrations to create the required tables:

bash
Копіювати код
alembic upgrade head
Step 5: Start the FastAPI server
Once the setup is complete, start the FastAPI server:

bash
Копіювати код
uvicorn main:app --reload
Your FastAPI server should now be running at http://localhost:8000.

Postman collection you can find in app dir - https://github.com/AntonVydyborets/Spy_cats/blob/main/Spy%20cats.postman_collection.json