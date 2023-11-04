FROM python:3.10-slim

WORKDIR /app

COPY ./src ./src

CMD ["python3", "main.py"]