FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt;

COPY . .

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

#EXPOSE 8000

#RUN pip install --upgrade pip --no-cache-dir && pip install psycopg2-binary && pip install -r requirements.txt --no-cache-dir;