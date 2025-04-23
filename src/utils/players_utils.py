import json
import os

DATA_FILE = "src/data/players.json"

def load_players():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_players(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def player_exists(user_id):
    players = load_players()
    return str(user_id) in players

def create_player(user_id, prenom, nom):
    players = load_players()
    players[str(user_id)] = {
        "prenom": prenom,
        "nom": nom,
        "inventaire": [],
        "baguette": None
    }
    save_players(players)
