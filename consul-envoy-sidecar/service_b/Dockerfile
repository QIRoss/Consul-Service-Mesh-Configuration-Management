FROM python:3.9-slim

WORKDIR /app
COPY main.py /app/main.py
RUN pip install fastapi uvicorn python-consul requests
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]