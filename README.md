# Django Task App

A Django project for training, simple task management application built to practice what I learned.
The app covers basic task management, user authentication, and permissions. Each user has their own task list, so the content changes depending on who is logged in.

## Features

- User registration, login, and logout.
- Create and view tasks.
- Edit tasks and mark them as completed.
- Delete tasks with the required permissions.
- Separate task lists for each user.
- Permission-based access for certain actions.
- A responsive interface using Bootstrap.

## Built With

- Python
- Django
- SQLite
- HTML & CSS
- Bootstrap 5

## Getting Started

To run the project locally, follow these steps.

### 1. Clone the repository

```bash
git clone https://github.com/Alnood-QG/django-task-app.git
cd django-task-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

```bash
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

Open the local address shown in your terminal to use the app.