from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/greet")
def greet():
    return {"message": f"Hello from Service A running on {os.getenv('SERVICE_HOST', 'unknown_host')}"}