FROM python:3.10-slim

WORKDIR /app

COPY ./src /app

CMD ["python3", "main.py"]