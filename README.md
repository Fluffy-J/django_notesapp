# Django Notes Application

A Django-based notes application with a server-rendered web interface and REST API.

**Live Demo:** https://notesapp-qv1o.onrender.com


\

## Table of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Screenshots](#screenshots)
* [API Endpoints](#api-endpoints)
* [Testing](#testing)
* [Deployment](#deployment)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Contact](#contact)

## About the Project

The Django Notes Application is a practical backend-focused project built to demonstrate Django development, REST API development, relational data modelling, automated testing, and production deployment.

The application allows users to:

* Create notes
* View recent notes
* View individual notes
* Delete notes
* Interact with notes through a REST API

The project uses SQLite for local development and PostgreSQL in production.

### Why I Built It

The project started as a Django learning application and was progressively developed into a deployable portfolio project.

During development, the application was strengthened through:

* REST API development
* PostgreSQL integration
* Production configuration
* Static-file handling
* Automated testing
* Code and repository restructuring
* Cloud deployment

## Built With

* **Python 3.11**
* **Django 5.2.17**
* **Django REST Framework 3.18.0**
* **SQLite** — local development
* **PostgreSQL** — production
* **WhiteNoise** — static files
* **Gunicorn + Uvicorn** — production server
* **Pipenv** — dependency management
* **Render** — deployment

## Getting Started

### Prerequisites

You will need:

* Python 3.11
* Pip
* Pipenv
* Git

### Installation

Clone the repository:

```bash
git clone https://github.com/Fluffy-J/django_notesapp.git
cd django_notesapp
```

Install dependencies:

```bash
pip install pipenv
pipenv sync
```

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY
```

Apply the database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Usage

The application provides a browser interface for managing notes.

<img width="1071" height="281" alt="image" src="https://github.com/user-attachments/assets/b32ec867-58ca-439d-95c3-cc731e96efe1" />


Users can create a note containing a title and body, view individual notes, and delete notes.

The application also exposes a REST API for programmatic interaction with the notes.

## Screenshots

### Application Interface

<img width="1065" height="667" alt="image" src="https://github.com/user-attachments/assets/9d870fdc-40c3-4211-99ab-8f12a192dd75" />


### Create Note

<img width="822" height="541" alt="image" src="https://github.com/user-attachments/assets/c77b2aea-3b6f-42e9-aac4-c9e8fc207082" />


### API

<img width="1068" height="667" alt="image" src="https://github.com/user-attachments/assets/fee8c333-e0b8-46a6-9202-07592f24dbb2" />


### Production Deployment

<img width="807" height="815" alt="image" src="https://github.com/user-attachments/assets/4eec1492-a701-440b-a3db-48d6e5e8170b" />


## API Endpoints

| Method | Endpoint                | Description         |
| ------ | ----------------------- | ------------------- |
| GET    | `/api/log/`             | List notes          |
| POST   | `/api/makenote/`        | Create a note       |
| PUT    | `/api/updatenote/<id>/` | Update a note title |
| DELETE | `/api/noteDelete/<id>/` | Delete a note       |

Example request:

```/api/makenote/

{
  "title": "Test_5",
  "body_text": "Created through the production API"
}

```

## Testing

The project uses Django's testing framework and Django REST Framework's `APITestCase`.

Tests are separated by responsibility:

```text
notes/tests/
├── test_models.py
├── test_views.py
└── test_api.py
```

The current test suite contains **14 automated tests** covering:

* Model behaviour and relationships
* Web views
* Note creation and deletion
* REST API operations
* Database changes
* Regression cases

Run the complete test suite with:

```bash
python manage.py test notes
```

<img width="970" height="240" alt="image" src="https://github.com/user-attachments/assets/0b5437d1-0402-44cd-a51d-bd9dfdde3398" />

## Deployment

The application is deployed on Render.

**Live application:** https://notesapp-qv1o.onrender.com

Production uses:

* PostgreSQL
* Gunicorn
* Uvicorn
* WhiteNoise
* Environment-based configuration

The deployment process installs the locked dependencies, collects static files, and applies database migrations.

<img width="807" height="815" alt="image" src="https://github.com/user-attachments/assets/36445f4c-e3d5-4e9f-a709-c9b0210d0f2c" />

## Roadmap

Planned improvements include:

* User authentication
* User-specific note ownership
* API permissions
* Improved API validation
* Editing note bodies through the API
* Pagination
* Continuous integration
* Improved frontend styling

## Contributing

This project is primarily a portfolio project, but suggestions and improvements are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run the test suite.
5. Submit a pull request.

## Contact

**Fluffy-J**

GitHub: https://github.com/Fluffy-J

Project Repository: https://github.com/Fluffy-J/django_notesapp

Live Application: https://notesapp-qv1o.onrender.com
