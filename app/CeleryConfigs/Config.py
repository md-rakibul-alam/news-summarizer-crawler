from celery import Celery

celery_app = Celery('news_summarizer', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

celery_app.conf.beat_schedule = {
    'run-every-second': {
        'task': 'app.CeleryConfigs.Tasks.summarize_news',
        'schedule': 10.0,  # Run every second
    },
}

celery_app.conf.timezone = 'UTC'

# Import the tasks module to register the tasks
import app.CeleryConfigs.Tasks
