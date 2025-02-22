from app.CeleryConfigs.Config import celery_app
from app.Summarizer.Summarizer import summarize_news
from app.Scrapper.ContentScrapper import ContentScrapper
from app.DatabaseContext.DatabaseContext import DatabaseContext

@celery_app.task
def invoke_summarize_news():
    db_context = DatabaseContext()
    url = "https://www.prothomalo.com/politics/f5vlbyjenc"
    scrapper = ContentScrapper(db_context)
    summary = scrapper.scrape_news(url)