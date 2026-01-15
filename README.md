# Job Board API

A production-ready backend API for a job board platform built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

This project supports three user roles:
- **Admin** – manages users and roles  
- **Employer** – posts jobs and reviews applications  
- **Candidate** – browses jobs and applies  

The system uses **JWT authentication**, **role-based access control**, and **Alembic migrations**, and is designed to be deployed to a cloud environment.

---

## Tech Stack

| Layer | Technology |
|------|-----------|
| API | FastAPI |
| Database | PostgreSQL (Neon) |
| ORM | SQLAlchemy (async) |
| Migrations | Alembic |
| Auth | JWT (python-jose) |
| Passwords | Passlib (bcrypt) |
| Validation | Pydantic |
| Deployment | Railway |

---

## Authentication & Roles

Authentication is handled using **JWT Bearer tokens**.

Each user has exactly one role:
- `admin`
- `employer`
- `candidate`

Role-based access is enforced at the endpoint level.

---

## Main Features

### Users
- Register as **employer** or **candidate**
- Login and receive JWT token
- Admin can change user roles

### Employers
- Create job listings
- View their own jobs
- View applications for their jobs

### Candidates
- View all job listings
- Apply to jobs
- View their own applications

### Admin
- View all users
- Change user roles

---

## API Endpoints

### Auth
```
POST /auth/register
POST /auth/login
```

### Jobs
```
GET /jobs
GET /jobs/{job_id}
GET /jobs/my
POST /jobs
GET /jobs/{job_id}/applications
```

### Applications
```
POST /applications
GET /applications/my
```

### Admin
```
GET /admin/users
PUT /admin/users/{user_id}/role
```

---

## Local Development

### 1. Create virtual environment
```
python -m venv venv
venv\Scripts\activate
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Configure environment variables
Create a `.env` file:
```
DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DBNAME?sslmode=require
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
```
### 4. Run migrations
```
alembic upgrade head
```
### 5. Run server
```
uvicorn main:app --reload
```
## API Docs
After starting the server, open:
```
http://localhost:8000/docs
```
## License
MIT