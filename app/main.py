from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.Scrapper.ContentScrapper import ContentScrapper
from app.DatabaseContext.DatabaseContext import DatabaseContext
import os

load_dotenv()

app = FastAPI(title="News Summary API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthy")
def healthy():
    print('I am healthy')
    return {"message": "I'm healthy"}

@app.post("/news")
def get_news_summary(url: str = Body(..., embed=True)):
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")
    
    db_context = DatabaseContext()
    scrapper = ContentScrapper(db_context)
    summary = scrapper.scrape_news(url)
    return {"summary": summary}