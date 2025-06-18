# ⚽ Futebol API (Vercel + FastAPI)

API leve e escalável desenvolvida em Python com FastAPI, pronta para uso com agentes GPT via Actions. Conectada à API-Football (API Sports), permite buscar dados atualizados de partidas, times, estatísticas, artilheiros e muito mais.

---

## ✅ Endpoints Disponíveis

| Rota                        | Descrição                                      |
|-----------------------------|-----------------------------------------------|
| `/fixtures`                 | Retorna partidas por time, liga ou temporada  |
| `/teams?search=Palmeiras`  | Retorna ID de um time pelo nome               |
| `/teams/statistics`         | Estatísticas completas por time/liga/temporada|
| `/players/topscorers`       | Lista artilheiros por liga e temporada        |

---

## 🔧 Parâmetros de exemplo

### `/teams/statistics`
