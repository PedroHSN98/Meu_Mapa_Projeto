import json
import os
from flask import Flask, render_template, jsonify, request
import requests
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
JSON_FILE = "historico_rotas.json"

def salvar_no_json(novo_registo):
    """Lê o histórico existente, adiciona o novo e grava no ficheiro JSON."""
    historico = []
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as f:
                historico = json.load(f)
        except json.JSONDecodeError:
            historico = []
    historico.append(novo_registo)
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    return render_template('index.html', token=MAPBOX_TOKEN)

@app.route('/calculate_matrix', methods=['POST'])
def calculate_matrix():
    data = request.json
    coords = data.get('coords') 
    names = data.get('names')      
    share_url = data.get('share_url') 
    
    url = f"https://api.mapbox.com/directions-matrix/v1/mapbox/driving/{coords}"
    params = {
        "access_token": MAPBOX_TOKEN,
        "annotations": "duration,distance"
    }
    
    try:
        response = requests.get(url, params=params)
        res_data = response.json()

        if response.status_code == 200:
            registo = {
                "data_hora": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "url_partilha": share_url,
                "pontos": [
                    {"identificador": n, "coordenada": c} 
                    for n, c in zip(names, coords.split(';'))
                ],
                "matriz_resultados": {
                    "duracoes_segundos": res_data.get('durations'),
                    "distancias_metros": res_data.get('distances')
                }
            }
            salvar_no_json(registo)
            return jsonify(res_data)
        else:
            return jsonify({"error": "Erro na API Mapbox"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)