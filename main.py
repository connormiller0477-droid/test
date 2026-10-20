import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return f"УСПЕХ! Ключ получен из внешней среды: {api_key}"
    else:
        return "Ключ не найден!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
