# Student Management System

A small practice project. FastAPI for the backend, plain HTML/CSS/JS for the frontend.

You can add, edit, and delete student records.

## Tech Stack

- Python / FastAPI
- Mysql (database)
- MySQL
- HTML / CSS / JS

## Project Structure


学生管理系统/
├── backend/
│   ├── main.py        # API routes
│   ├── models.py      # database models
│   ├── schemas.py     # data schemas
│   └── database.py    # database connection
├── frontend/
│   ├── index.html
│   └── style.css
└── requirements.txt


## Getting Started

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Start the backend from the project root

```bash
uvicorn backend.main:app --reload
```

3. Open `frontend/index.html` in your browser
