# Django User Management App

This project is a Django-based application for user management, including features such as registration, login, logout, profile management, and user deletion.

## Features

- **Home Page**: Displays a list of all users.
- **User Registration**: Allows new users to register.
- **User Login**: Enables users to log in.
- **User Logout**: Allows users to log out.
- **User Profile**: Displays the logged-in user's profile.
- **Update Profile**: Lets users update their profile information.
- **Delete Profile**: Allows users to delete their accounts.

## Requirements

- Python 3.8+
- Django 4.2+
- A database backend (e.g., SQLite, PostgreSQL, MySQL)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/whdev36/django-auth-system.git
   cd django-auth-system
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Register**: Create a new user account.
- **Login**: Access your account using your username and password.
- **Profile**: View and update your profile details.
- **Logout**: Securely log out of the application.
- **Delete Account**: Permanently remove your account.

## Project Structure

```
├── project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app_name/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── requirements.txt
```

## Attributions

<a href="https://www.flaticon.com/free-icons/shield" title="shield icons">Shield icons created by Freepik - Flaticon</a>

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
