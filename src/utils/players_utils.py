import json
import os

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(SCRIPT_DIR, "data/players", "players.json")

# Retourne les informations de base de l'utilisateur
def get_player_interaction(interaction):
    user_id = interaction.user.id
    user_nickname = interaction.user.display_name
    user_lang = interaction.locale

    return user_id, user_nickname, user_lang

# Charge les données des joueurs
def load_players():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Sauvegarde les données des joueurs
def save_players(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Vérifie si un joueur existe
def player_exists(user_id):
    players = load_players()
    return str(user_id) in players

# Crée un nouveau joueur
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
