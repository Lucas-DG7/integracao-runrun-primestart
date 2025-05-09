# 🚀 Integração Runrun.it x PrimeStart – Automação Inteligente em Python  

A revolução na conectividade entre plataformas chegou! Esta integração **simples, robusta e eficiente** conecta o sistema de gestão de tarefas **Runrun.it** à plataforma **PrimeStart**, garantindo um fluxo de trabalho ágil e automatizado.  

## 🔗 O que essa solução oferece?  
✅ **Captura de eventos do Runrun.it** via Webhook  
✅ **Processamento inteligente** e envio para a API PrimeStart  
✅ **Arquitetura modular e segura** com Flask & Python  
✅ **Configuração rápida** e documentação impecável  

---

## 📦 Estrutura do Projeto  
```bash
integracao-runrun-primestart/
├── src/
│   ├── __init__.py
│   ├── autenticacao.py
│   ├── webhook_handler.py
│   ├── api_p2s.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🛠️ Configuração e Uso  

### 1️⃣ **Clone o repositório**  
```sh
git clone git@github.com:seu-usuario/integracao-runrun-primestart.git
cd integracao-runrun-primestart
```

### 2️⃣ **Crie o ambiente virtual e instale dependências**  
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3️⃣ **Configure variáveis no `.env`**  
Crie um arquivo `.env` e adicione suas credenciais:  
```ini
PRIMESTART_USER=seu_usuario
PRIMESTART_PASSWORD=sua_senha
RUNRUN_APP_KEY=sua_app_key
RUNRUN_USER_TOKEN=seu_user_token
```

### 4️⃣ **Execute o projeto**  
```sh
python main.py
```
Você verá:  
```
🚀 Middleware ativo: ouvindo eventos de Runrun.it...
 * Running on http://0.0.0.0:5000
```

### 5️⃣ **Simule um evento Webhook**  
```sh
curl -X POST http://localhost:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{"evento": "tarefa_criada", "usuario": "lucas.dev", "id": 789}'
```

---

## 🎯 Para quem é essa solução?  
💡 **Profissionais** que buscam automação eficiente  
💡 **Desenvolvedores** querendo impressionar recrutadores  
💡 **Empresas** que precisam de integração contínua  

🔥 Agilidade, segurança e escalabilidade em um único projeto!  

---

## "Este projeto mostra minha capacidade de integrar plataformas reais, com foco em segurança, manutenção e escalabilidade. Estou pronto para trazer esse nível de integração para sua empresa." 
