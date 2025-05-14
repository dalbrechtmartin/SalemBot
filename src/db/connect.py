import psycopg2
import os

def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT")
        )
        print("✅ Connexion à la base de données réussie")
        return connection
    except Exception as e:
        print(f"❌ Erreur de connexion à la base : {e}")
        return None
