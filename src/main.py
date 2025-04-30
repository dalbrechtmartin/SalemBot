import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import importlib
import inspect

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("DISCORD_GUILD_ID")

# Ajoutez l'intent de message
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def load_all_commands():
    # Chemin vers le dossier des commandes
    commands_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commands")
    
    # Liste tous les fichiers Python dans le dossier commands
    command_files = [f for f in os.listdir(commands_dir) 
                    if f.endswith('.py') and not f.startswith('__')]
    
    print(f"📂 Recherche de commandes dans : {commands_dir}")
    
    # Pour chaque fichier, importe le module
    for file in command_files:
        module_name = file[:-3]  # Enlève l'extension .py
        module_path = f"commands.{module_name}"
        
        try:
            # Import dynamique du module
            module = importlib.import_module(module_path)
            
            # Recherche des classes qui héritent de commands.Cog
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, commands.Cog) and obj != commands.Cog:
                    # Instancie la classe et l'ajoute au bot
                    cog_instance = obj(bot)
                    await bot.add_cog(cog_instance)
                    print(f"✅ Commande chargée : {name} depuis {file}")
        
        except Exception as e:
            print(f"❌ Erreur lors du chargement de {module_path}: {e}")
            # Afficher plus de détails sur l'erreur
            import traceback
            traceback.print_exc()

async def setup():
    print("🔄 Chargement des commandes...")
    await load_all_commands() 
    print("🔄 Synchronisation des commandes slash...")
    try:
        # Synchronisation des commandes avec Discord
        synced = await bot.tree.sync()
        print(f"🌐 Commandes slash synchronisées : {len(synced)} commande(s)")
    except Exception as e:
        print(f"❌ Erreur lors de la synchronisation : {e}")

@bot.event
async def on_ready():
    print(f"🌐 Connecté en tant que {bot.user}")
    try:
        await setup()
    except Exception as e:
        print(f"❌ Erreur dans setup() : {e}")
        import traceback
        traceback.print_exc()

bot.run(TOKEN)