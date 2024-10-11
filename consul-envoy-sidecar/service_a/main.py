from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/greet")
def greet():
    return {"message": f"Hello from Service A running on port {os.getenv('PORT', '8000')}!"}

import consul

def register_with_consul():
    c = consul.Consul(host="consul", port=8500)
    service_name = os.getenv("SERVICE_NAME", "service_a")
    service_port = int(os.getenv("PORT", "8000"))
    c.agent.service.register(
        service_name,
        service_id=service_name,
        address="localhost",
        port=service_port,
        check=consul.Check.http(f"http://localhost:{service_port}/health", "10s"),
    )
