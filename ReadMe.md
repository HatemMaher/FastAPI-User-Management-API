# FastAPI User Management API

A production-style REST API built with **FastAPI** that demonstrates user management, authentication, password hashing, JWT authorization, dependency injection, and SQLAlchemy ORM.

This project was built as part of a backend learning journey and focuses on applying clean architecture principles and modern FastAPI development practices.

---

## Features

- User Registration
- User Login
- JWT Authentication
- Password Hashing (Argon2)
- Protected Routes
- User CRUD Operations
- SQLAlchemy ORM
- SQLite Database
- Dependency Injection
- Clean Project Structure

---

## Tech Stack

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT (python-jose)
- pwdlib (Argon2)
- Uvicorn

---

## Project Structure

```
project/
│
├── database/
│   ├── database.py
│   └── models.py
│
├── dependencies/
│   └── auth.py
│
├── routers/
│   ├── auth_router.py
│   └── user_router.py
│
├── schemas/
│   ├── auth_schema.py
│   └── user_schema.py
│
├── services/
│   ├── auth_service.py
│   └── user_service.py
│
├── utils/
│   ├── hashing.py
│   └── jwt_handler.py
│
├── config.py
├── main.py
└── requirements.txt
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

Move into the project

```bash
cd your-repository
```

Create a virtual environment

### Windows

```bash
python -m venv .venv
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn main:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

## Authentication Flow

### Register

```
POST /auth/register
```

Registers a new user.

---

### Login

```
POST /auth/login
```

Authenticates a user and returns a JWT access token.

Example response

```json
{
    "access_token": "your-jwt-token",
    "token_type": "bearer"
}
```

---

## Protected Endpoints

The following endpoints require a valid JWT Bearer Token.

| Method | Endpoint |
|---------|-----------|
| GET | /users |
| GET | /users/{id} |
| PUT | /users/{id} |
| DELETE | /users/{id} |

---

## Security

- Passwords are hashed using Argon2.
- Authentication is handled using JWT.
- Protected endpoints require a valid Bearer Token.

---

## Learning Objectives

This project demonstrates:

- REST API development
- FastAPI routing
- SQLAlchemy ORM
- Database relationships
- Authentication & Authorization
- JWT Token generation
- Password hashing
- Dependency Injection
- Clean Architecture
- API testing with Postman

---

## Future Improvements

- Environment variables (.env)
- Alembic migrations
- Global exception handling
- Response models
- Pagination
- Docker support
- Unit testing
- Refresh Tokens
- Role-Based Authorization (RBAC)

---

## Author

**Hatem Hussein**

Backend Software Engineer

GitHub:
https://github.com/your-github

LinkedIn:
https://linkedin.com/in/your-linkedin