from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session

import secrets
import string

from database import engine, Base, SessionLocal
from models import URL


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="Simple URL Shortener API",
    description="A simple URL shortening service using FastAPI",
    version="1.0"
)


# Database session
def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Request model
class URLRequest(BaseModel):

    original_url: HttpUrl


# Generate short code
def generate_short_code(length=6):

    characters = string.ascii_letters + string.digits

    return ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )


# Home route
@app.get("/")
def home():

    return {
        "message": "URL Shortener API is running"
    }


# Shorten URL
@app.post("/shorten")
def shorten_url(
    request: URLRequest,
    db: Session = Depends(get_db)
):

    # Generate a unique short code
    while True:

        short_code = generate_short_code()

        existing_url = (
            db.query(URL)
            .filter(URL.short_code == short_code)
            .first()
        )

        if not existing_url:
            break


    # Create database record
    new_url = URL(
        original_url=str(request.original_url),
        short_code=short_code
    )


    # Save to database
    db.add(new_url)
    db.commit()
    db.refresh(new_url)


    # Return response
    return {
        "original_url": new_url.original_url,
        "short_code": new_url.short_code,
        "short_url": f"http://127.0.0.1:8000/{short_code}"
    }


# Redirect short URL
@app.get("/{short_code}")
def redirect_to_original(
    short_code: str,
    db: Session = Depends(get_db)
):

    # Find URL
    url = (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )


    # URL not found
    if not url:

        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )


    # Redirect user
    return RedirectResponse(
        url=url.original_url,
        status_code=307
    )