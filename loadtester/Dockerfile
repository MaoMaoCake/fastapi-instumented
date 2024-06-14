FROM python:3.11.8-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY loadtest.py .

CMD ["python", "loadtest.py"]