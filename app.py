from fastapi import FastAPI, Query
import requests
from fastapi.responses import JSONResponse

app = FastAPI()

API_KEY = "58ccb64123b8f5e6631108ac4a05815e"
API_URL = "https://v3.football.api-sports.io"
HEADERS = {"x-apisports-key": API_KEY}


def call_api(path: str, params: dict):
    try:
        res = requests.get(f"{API_URL}{path}", headers=HEADERS, params=params)
        return JSONResponse(status_code=res.status_code, content=res.json())
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/fixtures")
def get_fixtures(team: int = Query(None), season: int = Query(None), league: int = Query(None)):
    params = {}
    if team: params["team"] = team
    if season: params["season"] = season
    if league: params["league"] = league
    return call_api("/fixtures", params)


@app.get("/teams")
def get_teams(search: str = Query(...)):
    return call_api("/teams", {"search": search})


@app.get("/teams/statistics")
def get_team_stats(team: int = Query(...), league: int = Query(...), season: int = Query(...)):
    return call_api("/teams/statistics", {"team": team, "league": league, "season": season})


@app.get("/players/topscorers")
def get_top_scorers(league: int = Query(...), season: int = Query(...)):
    return call_api("/players/topscorers", {"league": league, "season": season})


# === Arquivos adicionais para deploy ===

# requirements.txt
# -----------------
# fastapi
# requests
# uvicorn

# vercel.json
# -----------------
# {
#   "version": 2,
#   "builds": [
#     { "src": "api/index.py", "use": "@vercel/python" }
#   ],
#   "routes": [
#     { "src": "/(.*)", "dest": "/api/index.py" }
#   ]
# }

# README.md
# -----------------
# # Futebol API (Vercel + FastAPI)
#
# API leve, pronta para uso com GPT via Actions, integrada à API-Football.
#
# ## Rotas disponíveis:
# - `/fixtures`
# - `/teams?search=Palmeiras`
# - `/teams/statistics?team=56&league=39&season=2023`
# - `/players/topscorers?league=71&season=2024`
#
# ## Deploy (Passo a passo):
# 1. Suba esse projeto para o GitHub
# 2. Conecte-o ao Vercel (vercel.com)
# 3. O deploy será automático
# 4. Use a URL base no seu GPT personalizado
