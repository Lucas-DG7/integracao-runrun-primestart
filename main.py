from src.webhook_handler import app  # Certifique-se de que esse caminho está correto!

if __name__ == "__main__":
    print("🚀 Middleware ativo: ouvindo eventos de Runrun.it...")
    app.run(host="0.0.0.0", port=5000)
