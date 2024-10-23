# Task Manager

## Setup environment

1. **Create and activate a virtual environment:**
    - python -m venv venv
    - source venv\Scripts\activate
    - pip install -r requirements.txt
2. Create the database and superuser
    - python manage.py migrate
    - python manage.py createsuperuser

4. run the server
    - python manage.py runserver

5. add some tasks in admin or shell and navigate to 'http://127.0.0.1:8000/'

