# Futebol API Multifuncional

API baseada no Flask conectada à [API-Football](https://www.api-football.com/) com múltiplos endpoints dinâmicos.

## 🚀 Endpoints disponíveis

Todos os endpoints seguem o padrão:
/<endpoint>
/<section>/<endpoint>
/<section>/<sub>/<endpoint>

Exemplos:

- `/fixtures`
- `/teams?search=Flamengo`
- `/players/topscorers?league=71&season=2024`

## 🔑 Autenticação

A chave da API é passada como variável de ambiente no Render: `API_FOOTBALL_KEY`.

## 🛠️ Deploy no Render

1. Suba este repositório para o GitHub
2. Conecte no [Render](https://render.com)
3. Clique em **Create Web Service**
4. Escolha o repositório, confirme o `buildCommand` e `startCommand`
5. Defina a variável de ambiente: `API_FOOTBALL_KEY`

Pronto!
