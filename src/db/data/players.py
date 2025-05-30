from db.connect import get_db_connection

def player_exists_db(user_id):    
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM users WHERE id = %s", (user_id,))
            return cursor.fetchone() is not None
    except Exception as e:
        print(f"❌ Erreur lors de la vérification de l'existence du joueur : {e}")
        return False
    finally:
        connection.close()

def create_player_db(user_id, nickname=None):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (id)
                VALUES (%s)
                ON CONFLICT (id) DO NOTHING
                RETURNING id;
            """, (user_id,))
            connection.commit()
            return cursor.fetchone() is not None
    except Exception as e:
        connection.rollback()
        print(f"❌ Erreur lors de la création du joueur : {e}")
        return False
    finally:
        connection.close()

def get_player_db(user_id):    
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, level, xp, gold, wand, inventory, quests, achievements
                FROM users
                WHERE id = %s
            """, (user_id,))
            player_data = cursor.fetchone()
            
            if player_data:
                return {
                    "id": player_data[0],
                    "level": player_data[1],
                    "xp": player_data[2],
                    "gold": player_data[3],
                    "wand": player_data[4],
                    "inventory": player_data[5],
                    "quests": player_data[6],
                    "achievements": player_data[7]
                }
            return None
    except Exception as e:
        print(f"❌ Erreur lors de la récupération du joueur : {e}")
        return None
    finally:
        connection.close()