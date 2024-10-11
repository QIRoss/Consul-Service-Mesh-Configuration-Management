from fastapi import FastAPI
import requests
import os

app = FastAPI()

@app.get("/greet")
def greet():
    service_host = os.getenv('SERVICE_HOST', 'unknown_host')
    return {"message": f"Hello from Service A instance running on {service_host}!"}

@app.on_event("startup")
def register_with_consul():
    consul_url = os.getenv("CONSUL_URL", "http://localhost:8500")
    service_id = os.getenv("SERVICE_ID", f"service_a_{os.getenv('SERVICE_PORT')}")
    registration = {
        "ID": service_id,
        "Name": "service_a",
        "Address": os.getenv("SERVICE_HOST", "service_a"),
        "Port": int(os.getenv("SERVICE_PORT", 8001)),
        "Check": {
            "HTTP": f"http://{os.getenv('SERVICE_HOST', 'service_a')}:{os.getenv('SERVICE_PORT', 8001)}/greet",
            "Interval": "10s"
        }
    }
    requests.put(f"{consul_url}/v1/agent/service/register", json=registration)