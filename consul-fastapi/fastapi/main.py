import base64
import os
import requests
from fastapi import FastAPI

app = FastAPI()

CONSUL_URL = os.getenv("CONSUL_URL", "http://localhost:8500")
CONFIG_KEY = "config/myapp"

@app.get("/config")
def read_config():
    try:
        response = requests.get(f"{CONSUL_URL}/v1/kv/{CONFIG_KEY}")
        response.raise_for_status()
        data = response.json()
        if data:
            encoded_value = data[0]['Value']
            decoded_value = base64.b64decode(encoded_value).decode("utf-8")
            return {"config": decoded_value}
        return {"error": "No config found"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
