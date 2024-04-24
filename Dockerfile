FROM python:3.11.8-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["opentelemetry-instrument", "uvicorn", "main:app"]