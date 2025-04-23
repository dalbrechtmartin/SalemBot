import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from commands.meow import MeowCommand

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("DISCORD_GUILD_ID")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

async def setup():
    await bot.add_cog(MeowCommand(bot))    
    await bot.tree.sync()
    print("🌐 Commandes slash synchronisées")                  

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")
    try:
        bot.loop.create_task(setup())
    except Exception as e:
        print(e)

bot.run(TOKEN)