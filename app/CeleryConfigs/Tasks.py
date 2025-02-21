from app.CeleryConfigs.Config import celery_app

@celery_app.task
def summarize_news():
    print("Summarizing news...")
    print('Testing calling from Celery task')
    # Add your task implementation here
    # For example, you can call a function to summarize news articles
    # summarize_news()
