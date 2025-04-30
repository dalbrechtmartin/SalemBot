import json
import os

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(SCRIPT_DIR, "data/players", "players.json")

def load_players():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
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

def create_player(user_id, nickname):
    players = load_players()
    players[str(user_id)] = {
        "nickname": nickname,
        "level": 0,
        "xp": 0,
        "gold": 100,
        "wand": None,
        "inventory": [],
        "quests": [],
        "achievements": [],
    }
    save_players(players)
