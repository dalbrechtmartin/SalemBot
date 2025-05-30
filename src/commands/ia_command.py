import discord
from discord import app_commands
from discord.ext import commands
import os
import requests
import json
import asyncio

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434/api/chat")
ADMIN_ROLE_ID = int(os.getenv("DISCORD_ADMIN_ROLE_ID", "-1"))

class AICommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.checks.has_role(ADMIN_ROLE_ID)
    @app_commands.command(name="ai", description="Répond avec une réponse IA.")
    async def ai(self, interaction: discord.Interaction, prompt: str):
        try:
            await interaction.response.send_message("🧠 Je réfléchis...")

            payload = {
                "model": "llama3",
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,           
                "options": {
                    "num_predict": 600     
                }
            }

            def ollama_request():
                resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
                resp.raise_for_status()
                lines = resp.text.strip().splitlines()
                data = None
                for line in lines:
                    try:
                        data = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                return data or {}

            data = await asyncio.to_thread(ollama_request)
            content = data.get("message", {}).get("content", "Aucune réponse.")
            await interaction.followup.send(content)

        except Exception as e:
            await interaction.followup.send("❌ Une erreur s'est produite avec Ollama.")
            print(e)