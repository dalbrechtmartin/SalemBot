import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import importlib
import inspect

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

async def load_all_commands():
    commands_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "commands")
    
    command_files = [f for f in os.listdir(commands_dir) 
                    if f.endswith('.py') and not f.startswith('__')]
    
    print(f"📂 Recherche de commandes dans : {commands_dir}")
    
    for file in command_files:
        module_name = file[:-3]  # Remove .py extension
        module_path = f"commands.{module_name}"
        
        try:
            module = importlib.import_module(module_path)
            
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, commands.Cog) and obj != commands.Cog:
                    cog_instance = obj(bot)
                    await bot.add_cog(cog_instance)
                    print(f"✅ Commande chargée : {name} depuis {file}")
        
        except Exception as e:
            print(f"❌ Erreur lors du chargement de {module_path}: {e}")
            import traceback
            traceback.print_exc()

async def setup():
    print("🔄 Chargement des commandes...")
    await load_all_commands() 
    print("🔄 Synchronisation des commandes slash...")
    try:
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
        
@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingRole):
        await interaction.response.send_message(
            "❌ Vous n'avez pas les permissions d'utiliser cette commande.",
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            "❌ Une erreur est survenue lors de l'exécution de la commande.",
            ephemeral=True
        )
        raise error

bot.run(TOKEN)