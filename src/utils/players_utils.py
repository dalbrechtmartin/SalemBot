from db.data.players import player_exists_db, create_player_db, get_player_db

def player_exists(user_id):
    """Vérifie si un joueur existe"""
    return player_exists_db(user_id)

def create_player(user_id, nickname=None):
    """Crée un nouveau joueur"""
    return create_player_db(user_id, nickname)

def get_player_interaction(interaction):
    """Extrait les informations de l'utilisateur depuis l'interaction Discord"""
    user_id = str(interaction.user.id)
    user_nickname = interaction.user.display_name
    user_lang = "fr"  # Par défaut ou à récupérer des préférences
    
    return user_id, user_nickname, user_lang

def get_player(user_id):
    """Récupère les données d'un joueur"""
    return get_player_db(user_id)