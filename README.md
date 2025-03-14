# Cinema ticket sale site
# Cinema Ticket Sale Site

Fully functional website written by Django for cinema ticket sales.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project is a web application for managing and selling cinema tickets. It is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Features
- User authentication and authorization
- Movie management (CRUD operations)
- Show time management
- Ticket booking and purchase
- Payment processing
- User profile management
- Admin dashboard for managing the site

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- A virtual environment tool (e.g., `venv` or `virtualenv`)

### Steps
1. Clone the repository
    ```bash
    git clone https://github.com/theonlykingpin/Cinema.git
    cd Cinema
    ```

2. Create and activate a virtual environment
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations
    ```bash
    python manage.py migrate
    ```

5. Create a superuser
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server
    ```bash
    python manage.py runserver
    ```

7. Access the site at `http://127.0.0.1:8000/`

## Usage
- Register a new user or log in with an existing account.
- Browse available movies and showtimes.
- Book and purchase tickets.
- Manage your profile and view booking history.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
