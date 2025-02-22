from celery import Celery

celery_app = Celery('news_summarizer', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

celery_app.conf.beat_schedule = {
    'run-every-minute': {
        'task': 'app.CeleryConfigs.Tasks.invoke_summarize_news',
        'schedule': 6000.0,  # Run every minute
    },
}


celery_app.conf.timezone = 'UTC'

# Import the tasks module to register the tasks
import app.CeleryConfigs.Tasks
