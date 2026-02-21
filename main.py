import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Rota exata que o Free Fire antigo pede: /live/ver.php
@app.route('/live/ver.php', methods=['GET', 'POST', 'OPTIONS'])
def ver_php():
    # Log para você ver no painel do Render quando o jogo conectar
    print(f"Jogo conectou! Método: {request.method} | IP: {request.remote_addr}")
    
    response_data = {
        "appstore_url": "https://discord.gg/seu-link",
        "billboard_msg": "Servidor Online! Bem-vindo!",
        "cdn_url": "https://dl.cdn.freefiremobile.com/live/ABHotUpdates/",
        "client_ip": request.headers.get('X-Forwarded-For', request.remote_addr ),
        "code": 0,
        "country_code": "BR",
        "force_to_restart_app": False,
        "gdpr_version": 2,
        "is_firewall_open": False,
        "is_review_server": False,
        "is_server_open": True,
        "maintenance_announcement": "",
        "maintenance_region": "",
        "query_params": {},
        "remote_option_version": "1.0.0",
        "remote_version": "1",
        "server_url": f"https://{request.host}/login/" 
    }
    return jsonify(response_data )

# Rota de backup (caso o jogo peça apenas /live/)
@app.route('/live/', methods=['GET', 'POST'])
@app.route('/live', methods=['GET', 'POST'])
def live_root():
    return ver_php()

# Rota principal para teste no navegador
@app.route('/')
def home():
    return "Servidor Free Fire Online no Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
