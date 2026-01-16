# Job Board API

Backend REST API for a simple job board application,  built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

The API supports three user roles:
- **Admin** – manages users and roles  
- **Employer** – creates and manages job posts  
- **Candidate** – browses jobs and applies  

The project is designed as a clean, production-ready backendwith authentication, role-based authorization, database migrations, and deployment.

---

## Tech Stack

**Backend**
- Python 3.12+
- FastAPI
- SQLAlchemy (async)
- Alembic
- Pydantic

**Database**
- PostgreSQL (local and cloud - Neon)

**Auth & Security**
- JWT authentication
- Role-based access control
- Password hashing with `passlib[bcrypt]`

**Deployment**
- Railway
- Gunicorn + Uvicorn workers

---

## Features

### Authentication
- User registration
- User login with JWT access token
- Secure password hashing

### Roles & Permissions
- `admin`
- `employer`
- `candidate`
- Role-based endpoint protection

### Jobs
- Create job listings (employer/admin)
- View all jobs (public)
- View own jobs (employer)
- View job details

### Application
- Candidates can apply for jobs
- Candidates can view their applications
- Employers/Admins can view applications for their jobs

### Admin
- View all users
- Change user roles

---
## Project structure
```
job_board_api/
│
├── alembic/        # Database migrations
├── database/       # DB engine and session
├── dependencies/   # Auth & role sependencies
├── models/         # SQLAlchemy models
├── routers/        # API routers
├── schemas/        # Pydantic schemas
├── services/       # Auth & JWT logic
├── main.py
├── requirements.txt
├── .env.example
├── README.md
```
## Environment Variables
Create a `.env` file in the project root:
```
DATABASE_URL=postgresql://user:password@host:5432/dbname
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```
**Note:**
DATABASE_URL engine is the **sync URL.**
The async engine automatically converts it to asyncpg

---
## Database & Migrations
Run migrations with Alembic:
```
alembic upgrade head
```
Create new migration after model changes:
```
alembic revision --autogenerate -m "description"
```

---
## Running Locally
```
# Create virtual environment
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```
API will be available at:
```
http://localhost:8000
```
Swagger docs:
```
http://localhost:8000/docs
```

## Deployment
The application is deployed using **Railway** with:
```
gunicorn -k uvicorn.workers.UvicornWorker main:app
```
- PostgreSQL hosted on **Neon**
- Environment variables configured via Railway dashboard

## Design notes
-**Single-role model:** a user has exactly one facing role
- Clear separation of concerns:
    - services -> business logic
    - dependencies -> request-level concerns
    - routers -> API layer
---

## Status
- Core functionality completed
- Deployed and operational
- Future improvements
    - Refresh tokens
    - Pagination & filtering
    - Frontend client
    - Permission matrix
---

## Author
Built by **Oliver Aladrović / oliver.aladrovic**
Backend-focused Python developer.