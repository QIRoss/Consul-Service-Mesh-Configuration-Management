from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/get-greeting")
def get_greeting():
    try:
        response = requests.get("http://localhost:8080/service_a/greet")
        return {"message": response.json()}
    except Exception as e:
        return {"error": str(e)}

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
