This guide provides step-by-step instructions for setting up and running the Django project on different operating systems: Windows, macOS, and Linux.

## Prerequisites

Ensure that you have the following installed on your system:

- Python (3.8 or later) - [Download here](https://www.python.org/downloads/)
- pip (Python package manager) - Comes pre-installed with Python
- virtualenv (for creating an isolated Python environment)
- Git (optional, but recommended) - [Download here](https://git-scm.com/)

## Cloning the Project

If you haven't already cloned the project, use Git to do so:

```sh
# Clone the repository
[git clone ](https://github.com/Dar2402/file-handling.git)
cd file-handling
```

---

## Setting Up the Virtual Environment

### Windows

1. Open a terminal or PowerShell in the project directory.
2. Run the following commands:

```sh
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

### macOS/Linux

1. Open a terminal in the project directory.
2. Run the following commands:

```sh
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

---

## Installing Dependencies

Once the virtual environment is activated, install the required dependencies:

```sh
pip install -r requirements.txt
```

If `requirements.txt` is not available, manually install Django:

```sh
pip install django
```

---

## Setting Up the Database (SQLite)

Since SQLite is the default database in Django, no extra setup is needed. Run the following commands to initialize it:

```sh
# Apply database migrations
python manage.py migrate
```

---

## Creating a Superuser (Admin Access)

To create an admin user, run:

```sh
python manage.py createsuperuser
```

Enter the required details (username, email, password) when prompted.

---

## Running the Development Server

To start the Django development server, use:

```sh
python manage.py runserver
```

The server will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Configuring Environment Variables (Optional)

If your project requires environment variables, create a `.env` file in the project directory and add necessary variables:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=*
```

You may need to install `django-environ` to manage environment variables:

```sh
pip install django-environ
```

---

## Running Tests

To run tests, execute:

```sh
python manage.py test
```

---

## Common Issues and Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'django'`

Solution: Ensure that the virtual environment is activated and dependencies are installed.

```sh
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Issue: `sqlite3.OperationalError: unable to open database file`

Solution: Ensure that the database file has the correct permissions or delete `db.sqlite3` and run `python manage.py migrate` again.

### Issue: `Command 'python' not found`

Solution: Try using `python3` instead of `python`.

---

## Deployment Notes

For production deployment, consider using a more robust database (PostgreSQL, MySQL) and configuring a web server (Gunicorn, Nginx). Ensure `DEBUG=False` in production settings.

---

## Additional Resources

- [Django Official Documentation](https://docs.djangoproject.com/en/stable/)
- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)

