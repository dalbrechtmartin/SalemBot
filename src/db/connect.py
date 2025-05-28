import psycopg2
import os
import time

def get_db_connection(max_retries=5, retry_delay=2):
    retries = 0
    while retries < max_retries:
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
            retries += 1
            print(f"❌ Tentative {retries}/{max_retries} - Erreur de connexion : {e}")
            if retries < max_retries:
                print(f"⏳ Attente de {retry_delay} secondes avant nouvelle tentative...")
                time.sleep(retry_delay)
    print("❌ Impossible de se connecter à la base de données après plusieurs tentatives")
    return None