import base64
import os
from dotenv import load_dotenv

load_dotenv()

def autenticar_prime_start():
    usuario = os.getenv("PRIMESTART_USER")
    senha = os.getenv("PRIMESTART_PASSWORD")
    credenciais = f"{usuario}:{senha}"
    return base64.b64encode(credenciais.encode()).decode()

def autenticar_runrun():
    return {
        "app-key": os.getenv("RUNRUN_APP_KEY"),
        "user-token": os.getenv("RUNRUN_USER_TOKEN")
    }
