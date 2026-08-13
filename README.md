# URL-shortener
The URL Shortener Application is a web-based backend application developed using FastAPI, Python, SQLAlchemy, and SQLite. It converts long URLs into short, unique URLs that are easier to share and access.
# 🔗 Simple URL Shortener

A simple URL Shortener backend application built using **FastAPI, Python, SQLAlchemy, and SQLite**.

The application accepts a long URL, generates a unique short code, stores the URL mapping in a database, and redirects users from the short URL to the original URL.

## 🚀 Features

* Accept long URLs through a REST API.
* Generate unique short codes automatically.
* Store URL mappings in SQLite.
* Redirect short URLs to their original URLs.
* Validate URLs using Pydantic.
* Use SQLAlchemy for database operations.
* Interactive API documentation using FastAPI Swagger UI.

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Uvicorn**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**

## 📁 Project Structure

```text
simple-url-shortener/
│
├── venv/
│   └── Python virtual environment
│
├── main.py
│   └── FastAPI application and API routes
│
├── database.py
│   └── Database connection and configuration
│
├── models.py
│   └── SQLAlchemy database model
│
├── requirements.txt
│   └── Required Python packages
│
├── urls.db
│   └── SQLite database
│
└── README.md
    └── Project documentation
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd simple-url-shortener
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

## 🔗 API Endpoints

### 1. Home

```text
GET /
```

Checks whether the server is running.

Example response:

```json
{
    "message": "URL Shortener API is running"
}
```

### 2. Create Short URL

```text
POST /shorten
```

Request:

```json
{
    "original_url": "https://www.google.com"
}
```

Example response:

```json
{
    "original_url": "https://www.google.com/",
    "short_code": "K8mP2x",
    "short_url": "http://127.0.0.1:8000/K8mP2x"
}
```

### 3. Redirect

```text
GET /{short_code}
```

Example:

```text
http://127.0.0.1:8000/K8mP2x
```

The application searches for `K8mP2x` in the database and redirects the user to the original URL.

## 🗄️ Database Structure

The application uses SQLite with a `urls` table.

```text
urls
├── id
├── original_url
└── short_code
```

Example:

| id | original_url        | short_code |
| -: | ------------------- | ---------- |
|  1 | https://google.com  | K8mP2x     |
|  2 | https://youtube.com | A92LmQ     |

## 🔄 Application Workflow

```text
User enters long URL
        ↓
POST /shorten
        ↓
FastAPI receives URL
        ↓
Generate unique short code
        ↓
Store URL + short code
        ↓
Return short URL
        ↓
User opens short URL
        ↓
Search database
        ↓
Find original URL
        ↓
Redirect to original URL
```

## 🔮 Future Improvements

The project can be extended with:

* Basic web frontend
* Custom short URLs
* URL expiration
* Click/visit tracking
* User authentication
* QR code generation
* PostgreSQL database
* Deployment to a cloud platform

## 👨‍💻 Author

**Pavan Kumar**

B.Tech — CSE (AIML)

## 📄 License

This project is created for educational and learning purposes.
