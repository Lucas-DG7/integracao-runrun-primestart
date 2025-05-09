import requests
from .autenticacao import autenticar_prime_start

def enviar_para_prime_start(dados):
    url = "https://api.primestart.com/objeto"
    token = autenticar_prime_start()
    
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=dados)
    
    if response.status_code == 200:
        print("✅ Dados enviados com sucesso ao PrimeStart.")
    else:
        print(f"❌ Erro ao enviar para PrimeStart: {response.status_code}")
        print(response.text)
        
    return response.status_code, response.text
