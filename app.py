from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = "58ccb64123b8f5e6631108ac4a05815e"
API_URL = "https://v3.football.api-sports.io"
HEADERS = {"x-apisports-key": API_KEY}

def fetch_from_api(path, params=None):
    url = f"{API_URL}{path}"
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json(), response.status_code

@app.route("/<endpoint>", methods=['GET'])
def generic_endpoint(endpoint):
    params = request.args.to_dict()
    data, status = fetch_from_api(f"/{endpoint}", params)
    return jsonify(data), status

@app.route("/<section>/<endpoint>", methods=['GET'])
def nested_endpoint(section, endpoint):
    params = request.args.to_dict()
    data, status = fetch_from_api(f"/{section}/{endpoint}", params)
    return jsonify(data), status

@app.route("/<section>/<sub>/<endpoint>", methods=['GET'])
def deep_nested_endpoint(section, sub, endpoint):
    params = request.args.to_dict()
    data, status = fetch_from_api(f"/{section}/{sub}/{endpoint}", params)
    return jsonify(data), status

if __name__ == '__main__':
    app.run(debug=True)
# Ensure the API key is set as an environment variable for security
if not API_KEY:
    raise ValueError("API_KEY is not set. Please set the API_KEY environment variable.")
# Ensure the API URL is set as an environment variable for flexibility
if not API_URL:
    raise ValueError("API_URL is not set. Please set the API_URL environment variable.")