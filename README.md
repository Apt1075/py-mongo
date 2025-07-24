
# 🚀 FastAPI MongoDB CRUD API

This is a simple FastAPI application to perform basic CRUD operations (Create, Read, Update, Delete) with MongoDB using Motor (async MongoDB driver for Python).

---

## 🧾 Requirements

- Python 3.8+
- MongoDB running locally
- pip (Python package installer)

---

## 🛠️ Installation Steps

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd py-mongo
```

### 2. Set up a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **On Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Required Packages

```bash
pip install fastapi uvicorn pymongo motor
```

---

## 📂 Project Structure

```
py-mongo/
│
├── config/
│   └── db.py                  # MongoDB connection setup
│
├── models/
│   └── user_models.py         # Pydantic model for user entity
│
├── routes/
│   └── user_routes.py         # All user route definitions (CRUD)
│
├── schemas/
│   └── user_schemas.py        # Request/response schema
│
├── index.py                   # Main app entry point
└── README.md
```

---

## ▶️ Running the Project

Start the server with:

```bash
uvicorn index:app --reload
```

Visit the documentation at:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📬 Available Endpoints

| Method | Endpoint         | Description       |
|--------|------------------|-------------------|
| POST   | `/create`        | Create a new user |
| PUT    | `/update/{id}`   | Update user by ID |
| DELETE | `/delete/{id}`   | Delete user by ID |

> ⚠️ Make sure you use the correct HTTP method in tools like Postman to avoid `405 Method Not Allowed` errors.
