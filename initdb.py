# -*- coding: utf-8 -*-

from pymongo import MongoClient
from expanse.utils.security import SecurityTools


security_tools = SecurityTools()
client = MongoClient()
client.drop_database('expanse_soccer')

db = client.expanse_soccer

users = db.users
cbf_id = users.insert({
    "name": "CBF",
    "username": "cbf",
    "email": "cbf@example.com",
    "password": security_tools.hash_password("cbf"),
    "locale": "Locale"
})

teams = db.teams
teams.insert_many([
    {"name": "Atlético-GO", "players": [], "team_manager_id": cbf_id},
    {"name": "Atlético-MG", "players": [], "team_manager_id": cbf_id},
    {"name": "Atlético-PR", "players": [], "team_manager_id": cbf_id},
    {"name": "Avaí", "players": [], "team_manager_id": cbf_id},
    {"name": "Bahia", "players": [], "team_manager_id": cbf_id},
    {"name": "Botafogo", "players": [], "team_manager_id": cbf_id},
    {"name": "Chapecoense", "players": [], "team_manager_id": cbf_id},
    {"name": "Corinthians", "players": [], "team_manager_id": cbf_id},
    {"name": "Coritiba", "players": [], "team_manager_id": cbf_id},
    {"name": "Cruzeiro", "players": [], "team_manager_id": cbf_id},
    {"name": "Flamengo", "players": [], "team_manager_id": cbf_id},
    {"name": "Fluminense", "players": [], "team_manager_id": cbf_id},
    {"name": "Grêmio", "players": [], "team_manager_id": cbf_id},
    {"name": "Palmeiras", "players": [], "team_manager_id": cbf_id},
    {"name": "Ponte Preta", "players": [], "team_manager_id": cbf_id},
    {"name": "Santos", "players": [], "team_manager_id": cbf_id},
    {"name": "Sport", "players": [], "team_manager_id": cbf_id},
    {"name": "São Paulo", "players": [], "team_manager_id": cbf_id},
    {"name": "Vasco", "players": [], "team_manager_id": cbf_id},
    {"name": "Vitória", "players": [], "team_manager_id": cbf_id}
])
