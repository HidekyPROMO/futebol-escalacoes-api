from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/escalacao', methods=['GET'])
def buscar_escalação():
    time = request.args.get('time')
    if not time:
        return jsonify({"error": "Parâmetro 'time' obrigatório"}), 400

    query = f"{time} escalação provável hoje site:sofascore.com"
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    blocos = soup.find_all("div", class_="BNeawe")

    if blocos:
        resultado = blocos[0].get_text(strip=True)
        return jsonify({
            "time": time,
            "escalacao": resultado
        })
    else:
        return jsonify({
            "time": time,
            "escalacao": "Nenhum dado encontrado. O formato da fonte pode ter mudado."
        }), 404
