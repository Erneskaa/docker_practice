FROM python:3.12

RUN pip install flask jinja2 redis

COPY . .

CMD ["python3", "/app/app.py"]
