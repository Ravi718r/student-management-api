# 🎓 College ERP — Student Management API

A production-style **College ERP / Student Management REST API** built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, **JWT Authentication**, and **Docker**.

The project demonstrates how to structure a scalable backend application using a layered architecture with authentication, authorization, database relationships, migrations, validation, exception handling, and containerized deployment.

---

## 📌 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Project Structure](#-project-structure)
- [Core Modules](#-core-modules)
- [Authentication and Authorization](#-authentication-and-authorization)
- [Database](#-database)
- [SQLAlchemy](#-sqlalchemy)
- [Alembic Database Migrations](#-alembic-database-migrations)
- [Docker](#-docker)
- [Environment Variables](#-environment-variables)
- [API Routers](#-api-routers)
- [Request Flow](#-request-flow)
- [Default Admin](#-default-admin)
- [Installation and Setup](#-installation-and-setup)
- [Running the Project](#-running-the-project)
- [Database Migration Commands](#-database-migration-commands)
- [API Documentation](#-api-documentation)
- [Example API Flow](#-example-api-flow)
- [Production Considerations](#-production-considerations)
- [Future Improvements](#-future-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [License](#-license)

---

## 🚀 Introduction

The **College ERP — Student Management API** is a backend application designed to manage different academic and administrative operations of a college.

The system provides APIs for managing:

- Students
- Users
- Departments
- Courses
- Subjects
- Enrollments
- Attendance
- Marks
- Results
- Fees
- Faculty
- Faculty-Subject relationships
- Timetables

The project uses a modular FastAPI architecture so that each domain is separated into its own router, model, schema, and CRUD logic.

The application also implements:

- JWT-based authentication
- Password hashing
- Role-based authorization
- PostgreSQL database
- SQLAlchemy ORM
- Alembic migrations
- Centralized exception handling
- Docker containerization
- Environment-based configuration
- Default admin creation

---

## ✨ Features

### 👨‍🎓 Student Management

Provides APIs for managing student information.

Operations include:

- Create student
- Retrieve students
- Retrieve a specific student
- Update student
- Delete student
- Search and filter students
- Department relationship

---

### 👤 User Management

User functionality includes:

- User registration
- User login
- Password hashing
- Password verification
- JWT token generation
- Current-user authentication
- Role-based authorization

---

### 🏢 Department Management

Departments can be created and managed within the ERP system.

Students can be associated with departments using a foreign-key relationship.

---

### 📚 Course Management

The system provides APIs for creating and managing courses.

---

### 📖 Subject Management

Subjects can be created and associated with academic entities.

---

### 📝 Enrollment Management

Students can enroll in courses and subjects through the enrollment system.

---

### 📊 Marks Management

The marks module provides functionality for storing and managing student marks.

---

### 🏆 Result Management

The result module manages student academic results.

---

### 💰 Fee Management

The fee module manages student fee-related information.

---

### 👨‍🏫 Faculty Management

Faculty members can be created and managed.

The faculty functionality supports information such as:

- Employee ID
- Email
- Faculty details

---

### 🔗 Faculty-Subject Relationship

The project includes a separate relationship between faculty members and subjects.

This allows the system to represent which faculty members teach particular subjects.

---

### 📅 Timetable Management

The timetable module provides APIs for managing academic schedules.

---

### 📋 Attendance Management

The attendance module manages student attendance information.

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM / database interaction |
| Alembic | Database migrations |
| Pydantic | Request/response validation |
| JWT | Authentication |
| Passlib / bcrypt | Password hashing |
| Uvicorn | ASGI server |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |

---

# 🏗 Project Architecture

The project follows a modular backend architecture.

```text
Client
  │
  ▼
FastAPI
  │
  ├── Router
  │     │
  │     ▼
  │   Schema / Validation
  │     │
  │     ▼
  │   CRUD / Business Logic
  │     │
  │     ▼
  │   SQLAlchemy ORM
  │     │
  │     ▼
  │   PostgreSQL
  │
  └── Authentication
        │
        ├── JWT
        ├── Password Hashing
        └── Role Authorization
```

The application is divided into separate responsibilities instead of putting all backend logic inside a single file.

This makes the project easier to:

- Maintain
- Test
- Debug
- Extend
- Deploy
- Scale

---

## 📁 Project Structure

```text
Student Api/
│
├── app/
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── handler.py
│   │   └── logging_config.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── student.py
│   │   ├── user.py
│   │   ├── department.py
│   │   ├── attendance.py
│   │   ├── course.py
│   │   ├── subject.py
│   │   ├── enrollment.py
│   │   ├── marks.py
│   │   ├── fee.py
│   │   ├── faculty.py
│   │   ├── faculty_subject.py
│   │   └── timetable.py
│   │
│   ├── routers/
│   │   ├── students.py
│   │   ├── users.py
│   │   ├── department.py
│   │   ├── attendance.py
│   │   ├── course.py
│   │   ├── subject.py
│   │   ├── enrollment.py
│   │   ├── marks.py
│   │   ├── result.py
│   │   ├── fee.py
│   │   ├── faculty.py
│   │   ├── faculty_subject.py
│   │   └── timetable.py
│   │
│   ├── schemas/
│   │
│   ├── crud.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── bootstrap.py
│   └── main.py
│
├── alembic/
│   ├── versions/
│   │   └── cacc6c9d61fb_initial_schema.py
│   ├── env.py
│   └── script.py.mako
│
├── .dockerignore
├── .env
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🧩 Core Modules

## `main.py`

`main.py` is the entry point of the FastAPI application.

It:

- Creates the FastAPI application
- Registers centralized exception handlers
- Creates the default admin
- Defines the root endpoint
- Includes application routers

Example:

```python
app = FastAPI(
    title="Student Management API",
    description="Professional FastAPI Project",
    version="1.0.0"
)
```

The routers are registered using:

```python
app.include_router(students.router)
app.include_router(users.router)
app.include_router(department.router)
app.include_router(attendance.router)
app.include_router(course.router)
app.include_router(subject.router)
app.include_router(enrollment.router)
app.include_router(marks.router)
app.include_router(result.router)
app.include_router(fee.router)
app.include_router(faculty.router)
app.include_router(faculty_subject.router)
app.include_router(timetable.router)
```

This keeps the application's entry point clean while allowing each domain to maintain its own routes.

---

## `routers/`

The router layer defines the API endpoints.

Examples include:

- Student endpoints
- User endpoints
- Department endpoints
- Course endpoints
- Subject endpoints
- Enrollment endpoints
- Attendance endpoints
- Marks endpoints
- Faculty endpoints
- Timetable endpoints

The router is responsible primarily for handling HTTP-level concerns such as:

- HTTP methods
- URL paths
- Request parameters
- Request bodies
- Dependencies
- Authentication
- Calling CRUD/service logic
- Returning responses

A simplified flow is:

```text
HTTP Request
     │
     ▼
Router
     │
     ▼
Validation
     │
     ▼
CRUD / Service
     │
     ▼
Database
     │
     ▼
Response
```

---

## `schemas/`

The schema layer uses **Pydantic** models for request and response validation.

Schemas define what data the API expects and what data it returns.

For example:

```text
Client Request
      │
      ▼
Pydantic Schema
      │
      ├── Type Validation
      ├── Required Fields
      ├── Optional Fields
      └── Data Validation
```

This prevents invalid data from directly entering the application logic.

---

## `models/`

The model layer contains SQLAlchemy ORM models.

Each model represents a database table.

Examples:

```text
Student       → students
User          → users
Department    → departments
Course        → courses
Subject       → subjects
Faculty       → faculty
Enrollment    → enrollments
Marks         → marks
Attendance    → attendance
Fee           → fees
Timetable     → timetables
```

Relationships between entities are represented using foreign keys and SQLAlchemy relationships.

---

## `crud.py`

The CRUD layer contains database operations.

CRUD stands for:

```text
C → Create
R → Read
U → Update
D → Delete
```

Instead of putting database queries directly inside every router, database operations can be centralized inside CRUD functions.

Example:

```text
Router
   │
   ▼
CRUD Function
   │
   ▼
SQLAlchemy Session
   │
   ▼
PostgreSQL
```

This separation keeps API endpoints smaller and easier to maintain.

---

## `services/`

The service layer is used for application-level business logic.

A useful separation is:

```text
Router
   │
   ▼
Service
   │
   ▼
CRUD
   │
   ▼
Database
```

The service layer is useful when business rules become more complex than simple database operations.

Examples:

- Enrollment rules
- Result calculation
- Fee processing
- Attendance rules
- Multi-step operations

---

## `dependencies.py`

The dependency layer provides reusable FastAPI dependencies.

One important dependency is the database session.

The typical flow is:

```text
Request
   │
   ▼
get_db()
   │
   ▼
SQLAlchemy Session
   │
   ▼
Router
   │
   ▼
CRUD
```

The database session is created for the request and closed after the request finishes.

---

## `database.py`

`database.py` configures SQLAlchemy.

It contains:

- Database engine
- Session factory
- Declarative base

Example:

```python
engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False
)

Base = declarative_base()
```

The engine manages communication between the Python application and PostgreSQL.

`SessionLocal` creates SQLAlchemy database sessions.

`Base` is used as the parent class for SQLAlchemy models and provides the metadata required by Alembic.

---

## `auth.py`

`auth.py` contains authentication and authorization logic.

It handles:

- Password hashing
- Password verification
- JWT creation
- JWT verification
- Current-user retrieval
- Admin authorization

Authentication flow:

```text
Login Request
      │
      ▼
Verify User
      │
      ▼
Verify Password
      │
      ▼
Create JWT
      │
      ▼
Return Token
```

Protected endpoint flow:

```text
Client
   │
   │ Authorization: Bearer <JWT>
   ▼
FastAPI
   │
   ▼
JWT Verification
   │
   ▼
Get Current User
   │
   ▼
Authorization Check
   │
   ▼
Endpoint
```

---

## `bootstrap.py`

`bootstrap.py` contains startup initialization logic.

The project uses it to create a default admin user if an admin does not already exist.

The logic is:

```text
Application Starts
       │
       ▼
Check Database
       │
       ▼
Does Admin Exist?
    /       \
  Yes        No
   │          │
   ▼          ▼
Continue    Create Admin
```

If an admin already exists, another admin is not created.

---

## `core/`

The `core` package contains application-wide configuration and infrastructure logic.

It includes:

- Configuration
- Exception handling
- Logging configuration

This keeps cross-cutting concerns separate from business modules.

---

# 🔐 Authentication and Authorization

The project uses JWT-based authentication.

JWT stands for **JSON Web Token**.

The authentication system contains three major components:

- Password hashing
- JWT authentication
- Role-based authorization

---

## Password Hashing

Passwords are never intended to be stored as plain text.

The project uses Passlib with bcrypt for password hashing.

```text
Plain Password
      │
      ▼
bcrypt / Password Hashing
      │
      ▼
Password Hash
      │
      ▼
Database
```

During login:

```text
Entered Password
      │
      ▼
Verify Against Stored Hash
      │
      ▼
Valid?
   /     \
 Yes      No
 │         │
 ▼         ▼
JWT      Reject
```

---

## JWT Token

After successful authentication, the server creates an access token.

The token contains claims such as:

```text
sub → user identifier
exp → expiration time
```

The token is cryptographically signed using:

```text
SECRET_KEY
+
ALGORITHM
```

The client then sends the token with protected requests:

```http
Authorization: Bearer <access_token>
```

---

## JWT Validation

The API does not need to store every issued JWT in the database.

When a request contains a JWT, the application:

1. Extracts the token
2. Decodes the token
3. Verifies the signature
4. Checks expiration
5. Extracts the user identifier
6. Looks up the user in the database
7. Applies authorization rules

Simplified flow:

```text
JWT
 │
 ▼
Decode
 │
 ▼
Verify Signature
 │
 ▼
Check Expiration
 │
 ▼
Extract "sub"
 │
 ▼
Find User
 │
 ▼
Authorization
```

---

## Role-Based Authorization

The project includes role-based authorization.

For example:

```text
User
 │
 ├── student
 │
 ├── faculty
 │
 └── admin
```

An admin-only endpoint can use an authorization dependency.

The authorization flow is:

```text
Request
   │
   ▼
JWT Authentication
   │
   ▼
Current User
   │
   ▼
Check Role
   │
   ├── admin → Allow
   │
   └── non-admin → 403 Forbidden
```

---

# 🗄 Database

The project uses **PostgreSQL** as its relational database.

The database is running as a Docker container through Docker Compose.

The main database is:

```text
college_erp
```

The database architecture is:

```text
FastAPI Container
       │
       │ PostgreSQL Network
       ▼
PostgreSQL Container
       │
       ▼
college_erp
```

---

## Database Relationships

The ERP contains multiple related entities.

A simplified relationship structure is:

```text
Department
    │
    └── Students

Course
    │
    └── Subjects

Student
    │
    ├── Enrollment
    ├── Attendance
    ├── Marks
    ├── Result
    └── Fees

Faculty
    │
    └── Faculty Subjects
             │
             └── Subjects

Timetable
    │
    ├── Faculty
    ├── Subject
    └── Course
```

Foreign keys are used to maintain relationships between related tables.

---

# 🧱 SQLAlchemy

SQLAlchemy is used as the ORM layer.

ORM stands for **Object Relational Mapping**.

Instead of writing raw SQL for every database operation, SQLAlchemy allows Python classes to represent database tables.

For example:

```text
Python Class
     │
     ▼
SQLAlchemy ORM
     │
     ▼
Database Table
```

Example concept:

```python
class Student(Base):
    __tablename__ = "students"
```

The `Student` class represents the `students` database table.

---

## SQLAlchemy Engine

The SQLAlchemy engine manages the connection between the application and the database.

```text
FastAPI
   │
   ▼
SQLAlchemy Engine
   │
   ▼
PostgreSQL
```

The engine is created using the database URL.

---

## SQLAlchemy Session

A SQLAlchemy session is used to interact with the database.

Typical operations include:

```python
db.add(student)
db.commit()
db.query(Student)
db.delete(student)
```

The session provides the working context for database operations.

---

## Session Lifecycle

The application uses a database dependency to manage sessions.

```text
Request Starts
      │
      ▼
Create Session
      │
      ▼
Use Session
      │
      ▼
CRUD Operations
      │
      ▼
Request Ends
      │
      ▼
Close Session
```

This prevents database sessions from remaining open unnecessarily.

---

# 🔄 Alembic Database Migrations

**Alembic** is used to manage database schema changes.

Instead of manually changing PostgreSQL tables, Alembic tracks schema changes through migration files.

The migration workflow is:

```text
SQLAlchemy Models
       │
       ▼
Alembic Autogenerate
       │
       ▼
Migration File
       │
       ▼
alembic upgrade head
       │
       ▼
PostgreSQL Schema
```

---

## Alembic Configuration

The main Alembic configuration is stored in:

```text
alembic.ini
```

The migration environment is configured in:

```text
alembic/env.py
```

The migration history is stored inside:

```text
alembic/versions/
```

---

## Autogenerating a Migration

A migration can be generated using:

```bash
docker compose run --rm api alembic revision --autogenerate -m "initial_schema"
```

Alembic compares:

```text
SQLAlchemy Models
        │
        ▼
Current Database Schema
        │
        ▼
Detect Differences
        │
        ▼
Generate Migration
```

The generated migration should always be reviewed before applying it, especially for destructive schema changes or changes involving existing data.

---

## Applying Migrations

To apply migrations:

```bash
docker compose run --rm api alembic upgrade head
```

`head` means the latest migration revision.

---

## Migration Versioning

Each migration contains:

```text
revision
down_revision
upgrade()
downgrade()
```

Example:

```text
Migration A
    │
    ▼
Migration B
    │
    ▼
Migration C
```

Alembic uses this revision chain to determine which migrations have already been applied.

---

# 🐳 Docker

The application is containerized using Docker.

Docker Compose manages multiple containers.

The project currently uses:

```text
┌───────────────────────────────┐
│        Docker Compose         │
│                               │
│  ┌─────────────┐              │
│  │ FastAPI API │              │
│  │ college_api │              │
│  └──────┬──────┘              │
│         │                     │
│         │ PostgreSQL Network  │
│         ▼                     │
│  ┌──────────────────┐        │
│  │    PostgreSQL    │        │
│  │ college_postgres │        │
│  └──────────────────┘        │
│                               │
└───────────────────────────────┘
```

---

## Dockerfile

The Dockerfile:

- Uses Python 3.12 slim
- Sets the working directory
- Copies `requirements.txt`
- Installs dependencies
- Copies application code
- Exposes port `8000`
- Starts Uvicorn

The container starts FastAPI using:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## Docker Compose

Docker Compose defines two services:

```text
db
│
└── PostgreSQL 16

api
│
└── FastAPI Application
```

The API depends on the database service.

The PostgreSQL database uses a Docker volume so that database data can persist across normal container recreation.

---

## Container Networking

Inside Docker Compose, the API does not connect to PostgreSQL using:

```text
localhost
```

Instead, it connects using the PostgreSQL service name:

```text
db
```

Therefore, inside the API container:

```text
postgresql://postgres:<password>@db:5432/college_erp
```

is used.

From the Windows host machine, PostgreSQL can be accessed through the published port using:

```text
localhost:5432
```

This distinction is important:

```text
Inside API Container:

API ───────► db:5432


From Windows Host:

Windows ───► localhost:5432
```

---

# ⚙️ Environment Variables

Sensitive configuration is stored in `.env`.

Example structure:

```env
DATABASE_URL=postgresql://postgres:<password>@db:5432/college_erp

SECRET_KEY=<your-secret-key>

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

The `.env` file should not be committed to GitHub.

Add it to `.gitignore`:

```text
.env
```

For production deployments, secrets should be provided through a secure secret-management system or deployment environment rather than hard-coded in source code.

---

# 🛣 API Routers

The application separates endpoints into different routers.

| Router | Responsibility |
|---|---|
| `students.py` | Student management |
| `users.py` | User registration and authentication |
| `department.py` | Department management |
| `attendance.py` | Attendance management |
| `course.py` | Course management |
| `subject.py` | Subject management |
| `enrollment.py` | Enrollment management |
| `marks.py` | Marks management |
| `result.py` | Result management |
| `fee.py` | Fee management |
| `faculty.py` | Faculty management |
| `faculty_subject.py` | Faculty-subject relationships |
| `timetable.py` | Timetable management |

This approach prevents `main.py` from becoming a large collection of endpoints.

---

# 🔄 Request Flow

A typical request follows this architecture:

```text
Client
  │
  │ HTTP Request
  ▼
FastAPI
  │
  ▼
Router
  │
  ▼
Pydantic Schema
  │
  ▼
Dependencies
  │
  ├── Database Session
  │
  └── Authentication
  │
  ▼
Service / CRUD
  │
  ▼
SQLAlchemy
  │
  ▼
PostgreSQL
  │
  ▼
SQLAlchemy Result
  │
  ▼
Response Schema
  │
  ▼
JSON Response
  │
  ▼
Client
```

---

## 🔐 Protected Request Flow

For an authenticated endpoint:

```text
Client
  │
  │ Authorization: Bearer JWT
  ▼
FastAPI
  │
  ▼
OAuth2PasswordBearer
  │
  ▼
JWT Verification
  │
  ▼
Get Current User
  │
  ▼
Role Authorization
  │
  ▼
Router
  │
  ▼
CRUD / Service
  │
  ▼
PostgreSQL
```

If authentication fails:

```text
401 Unauthorized
```

If authentication succeeds but the user does not have sufficient permissions:

```text
403 Forbidden
```

---

# 👑 Default Admin

The project contains a bootstrap mechanism that creates a default administrator if an administrator does not already exist.

The bootstrap logic checks the database first:

```text
Application Start
       │
       ▼
Check for Admin
       │
   ┌───┴───┐
   │       │
 Exists   Missing
   │       │
   ▼       ▼
Continue  Create Admin
```

The default credentials configured during development are:

```text
Username: admin
Email: admin@gmail.com
Password: 123456
Role: admin
```

These credentials are intended for development/testing.

For a real production deployment, the default password should be changed immediately or the bootstrap mechanism should be replaced with a secure administrative provisioning process.

---

# 🚀 Installation and Setup

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd Student-Api
```

---

## 2. Create a Virtual Environment

On Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:<password>@db:5432/college_erp

SECRET_KEY=<your-secret-key>

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# ▶️ Running the Project

The recommended way to run the complete application is using Docker Compose.

Build and start the containers:

```bash
docker compose up --build
```

The API will start on:

```text
http://localhost:8000
```

To run the containers in detached mode:

```bash
docker compose up -d
```

To stop the containers:

```bash
docker compose down
```

---

## View Running Containers

```bash
docker ps
```

Expected containers include:

```text
college_api
college_postgres
```

---

## View Application Logs

```bash
docker compose logs api
```

Or follow the logs:

```bash
docker compose logs -f api
```

---

## Stop Containers

```bash
docker compose down
```

To remove the Docker Compose database volume as well:

```bash
docker compose down -v
```

**Warning:** Removing the PostgreSQL volume deletes the database data stored in that Docker volume.

---

# 🗃 Database Migration Commands

## Create a Migration

After changing SQLAlchemy models:

```bash
docker compose run --rm api alembic revision --autogenerate -m "describe_your_change"
```

Example:

```bash
docker compose run --rm api alembic revision --autogenerate -m "add_department_relationship"
```

---

## Apply Latest Migrations

```bash
docker compose run --rm api alembic upgrade head
```

---

## Check Current Migration

```bash
docker compose run --rm api alembic current
```

---

## View Migration History

```bash
docker compose run --rm api alembic history
```

---

## Downgrade One Migration

```bash
docker compose run --rm api alembic downgrade -1
```

Migration files should be reviewed carefully before applying or downgrading them, especially when existing database data is involved.

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

```text
http://localhost:8000/docs
```

Swagger UI allows you to:

- Explore endpoints
- View request schemas
- View response schemas
- Send API requests
- Test authentication
- Test protected endpoints

---

## ReDoc

Open:

```text
http://localhost:8000/redoc
```

ReDoc provides an alternative API documentation interface.

---

## Root Endpoint

Open:

```text
http://localhost:8000/
```

Response:

```json
{
    "message": "Welcome to Student Management API"
}
```

---

# 🔁 Example API Flow

A typical authentication flow looks like this:

```text
1. Register User
       │
       ▼
2. Password Hashed
       │
       ▼
3. User Stored in PostgreSQL
       │
       ▼
4. Login
       │
       ▼
5. Password Verification
       │
       ▼
6. JWT Generated
       │
       ▼
7. Client Stores Token
       │
       ▼
8. Client Sends Bearer Token
       │
       ▼
9. JWT Verified
       │
       ▼
10. Current User Identified
       │
       ▼
11. Authorization Checked
       │
       ▼
12. Protected Endpoint Executes
```

---

# 🧪 Example Development Workflow

A typical development workflow for this project is:

```text
Modify SQLAlchemy Model
        │
        ▼
Generate Alembic Migration
        │
        ▼
Review Migration
        │
        ▼
Apply Migration
        │
        ▼
Start FastAPI
        │
        ▼
Test API through Swagger
        │
        ▼
Verify PostgreSQL Data
```

Example:

```bash
docker compose run --rm api alembic revision --autogenerate -m "update_student_model"

docker compose run --rm api alembic upgrade head

docker compose up
```

---

# 🛡️ Centralized Exception Handling

The application registers exception handlers from the application's core handler module.

The handler is registered globally:

```python
registere_exception_handlers(app)
```

This means the exception handling behavior can be applied across the FastAPI application instead of manually registering the same handler repeatedly for every route.

The architecture becomes:

```text
Any Router
    │
    ▼
Exception Occurs
    │
    ▼
FastAPI Exception System
    │
    ▼
Registered Global Handler
    │
    ▼
Consistent Error Response
```

This improves consistency and keeps individual routers focused on their actual business logic.

---

# 📦 Dependency Injection

FastAPI dependency injection is used for reusable application components.

Examples include:

- Database sessions
- Current authenticated user
- Admin authorization

The dependency chain can look like:

```text
Protected Endpoint
       │
       ▼
get_current_user()
       │
       ▼
OAuth2PasswordBearer
       │
       ▼
verify_access_token()
       │
       ▼
Database User Lookup
```

For admin endpoints:

```text
Admin Endpoint
       │
       ▼
admin_required()
       │
       ▼
get_current_user()
       │
       ▼
Check role == "admin"
```

This avoids duplicating authentication logic across endpoints.

---

# 🧠 Separation of Responsibilities

The project follows separation of concerns.

| Layer | Responsibility |
|---|---|
| Router | HTTP/API handling |
| Schema | Input/output validation |
| Service | Business/application logic |
| CRUD | Database operations |
| Model | Database representation |
| Dependency | Reusable request dependencies |
| Auth | Authentication and authorization |
| Core | Application-wide infrastructure |
| Alembic | Database schema versioning |
| Docker | Application infrastructure |

This separation makes the application easier to maintain and extend.

---

# ⚡ Production Considerations

Although this is a production-style learning project, additional work would be required before deploying it to a real production environment.

Important considerations include:

### Security

- Never commit `.env` files
- Use strong production secrets
- Rotate secrets when required
- Use secure password policies
- Use HTTPS
- Implement appropriate CORS policies
- Add rate limiting
- Add account lockout or abuse protection where appropriate
- Avoid exposing development credentials

---

### Database

- Use connection pooling appropriately
- Configure database backups
- Monitor database performance
- Add appropriate indexes
- Review foreign-key constraints
- Use transactions for multi-step operations
- Monitor slow queries

---

### Authentication

- Use short-lived access tokens where appropriate
- Consider refresh-token architecture for long-lived sessions
- Protect token storage on clients
- Rotate or revoke credentials when necessary
- Use strong signing secrets
- Consider key-management infrastructure for larger deployments

---

### API

- Add structured API logging
- Add request tracing
- Add monitoring
- Add health-check endpoints
- Add rate limiting
- Add automated tests
- Validate authorization for every protected resource
- Avoid exposing sensitive database errors

---

### Deployment

A production deployment could use:

```text
Client
   │
   ▼
Load Balancer / Reverse Proxy
   │
   ▼
FastAPI Application
   │
   ├── PostgreSQL
   │
   ├── Redis
   │
   └── Monitoring / Logging
```

The exact architecture depends on deployment requirements and traffic.

---

# 🔮 Future Improvements

Possible future improvements include:

- Redis caching
- Background task processing
- Celery integration
- Refresh token support
- Advanced RBAC
- Permission-based authorization
- API rate limiting
- Automated testing with Pytest
- CI/CD with GitHub Actions
- Health-check endpoints
- Structured logging
- Observability and tracing
- Prometheus metrics
- Grafana dashboards
- Database backup automation
- Email notifications
- File upload support
- Cloud deployment
- Kubernetes deployment
- Reverse proxy using Nginx
- API versioning
- Pagination improvements
- Advanced search
- Full-text search
- Audit logging

---

# 📚 Learning Outcomes

This project provides practical experience with backend engineering concepts including:

- FastAPI application architecture
- REST API development
- Python backend development
- Pydantic validation
- SQLAlchemy ORM
- PostgreSQL
- Database relationships
- Database sessions
- CRUD architecture
- Service-layer architecture
- Dependency injection
- JWT authentication
- Password hashing
- Role-based authorization
- Exception handling
- Alembic migrations
- Docker
- Docker Compose
- Environment configuration
- Container networking
- API documentation
- Modular project organization

The project also demonstrates how individual backend concepts work together as a complete application rather than as isolated technologies.

---

# 🎯 Why This Project Is Resume-Worthy

This project demonstrates more than basic CRUD development.

It covers several backend engineering concepts:

```text
REST API
   │
   ├── Authentication
   ├── Authorization
   ├── Validation
   ├── Database Design
   ├── ORM
   ├── Migrations
   ├── Exception Handling
   ├── Dependency Injection
   ├── Modular Architecture
   └── Containerization
```

It therefore provides a practical foundation for understanding how a multi-module backend application can be designed, developed, migrated, tested, and containerized.

---

# 🧑‍💻 Author

**Ravi Yadav**

B.Tech — Electronics and Communication Engineering

Interested in:

- Backend Engineering
- AI Engineering
- Agentic AI
- LLM Applications
- FastAPI
- RAG Systems
- Software Engineering

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project according to the terms of the license.

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
