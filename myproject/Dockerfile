FROM python:3.9

WORKDIR /usr/src/newsapp

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /usr/src/newsapp

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]