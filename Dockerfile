FROM python:3.8-slim

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

COPY src src
COPY gunicorn_config.py src/gunicorn_config.py

COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install -y poppler-utils
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR src

EXPOSE 5000

CMD ["gunicorn", "-c", "gunicorn_config.py", "app:create_app()"]
