FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["celery", "-A", "app.CeleryConfigs.Config", "worker", "--loglevel=info"]