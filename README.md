# Late Show API Challenge

A Flask REST API for managing a Late Night TV show system.

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Kipla1/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install dependencies

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### 3. PostgreSQL Setup

- Ensure PostgreSQL is installed and running.
- Create the database:

```sql
CREATE DATABASE late_show_db;
```

### 4. Configure Environment Variables

Edit `servers/config.py` and set your database URI:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
```

---

## 🛠 How to Run

### 1. Database Migrations

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 2. Seed the Database

```bash
python server/seed.py
```

### 3. Run the Server

```bash
flask run
```

---

## 🔐 Auth Flow

- **Register:**  
  `POST /register` with JSON `{ "username": "...", "password": "..." }`
- **Login:**  
  `POST /login` with JSON `{ "username": "...", "password": "..." }`  
  → Returns `{ "access_token": "<JWT>" }`
- **Token Usage:**  
  For protected routes, add header:  
  `Authorization: Bearer <JWT>`

---

## 📚 Routes

| Route                       | Method | Auth Required | Description                        |
|-----------------------------|--------|---------------|------------------------------------|
| `/register`                 | POST   | ❌            | Register a user                    |
| `/login`                    | POST   | ❌            | Log in, get JWT token              |
| `/episodes`                 | GET    | ❌            | List episodes                      |
| `/episodes/<int:id>`        | GET    | ❌            | Get episode + appearances          |
| `/episodes/<int:id>`        | DELETE | ✅            | Delete episode + appearances       |
| `/guests`                   | GET    | ❌            | List guests                        |
| `/appearances`              | POST   | ✅            | Create appearance                  |

### Sample Request/Response

**Register**
```http
POST /register
Content-Type: application/json

{
  "username": "alice",
  "password": "password123"
}
```

**Login**
```http
POST /login
Content-Type: application/json

{
  "username": "alice",
  "password": "password123"
}
```
_Response:_
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Protected Request Example**
```http
POST /appearances
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 2
}
```

---

## 🧪 Postman Usage Guide

1. Import `challenge-4-lateshow.postman_collection.json` into Postman.
2. Use the `/register` and `/login` endpoints to get a JWT token.
3. For protected routes, set the `Authorization` header:  
   `Bearer <your_token_here>`
4. Test all endpoints as described above.

---

## 🔗 GitHub Repo
https://github.com/Kipla1/late-show-api-challenge.git