import discord
from discord import app_commands
from discord.ext import commands
from openai import OpenAI
import os

class AICommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    @app_commands.command(name="ai", description="Répond avec une réponse IA.")
    async def ai(self, interaction: discord.Interaction, prompt: str):
        try:
            await interaction.response.send_message("🧠 Je réfléchis...")
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            await interaction.followup.send(response.choices[0].message.content)
        except Exception as e:
            if "insufficient_quota" in str(e):
                await interaction.followup.send("❌ Le service IA est temporairement indisponible.")
            else:
                await interaction.followup.send("❌ Une erreur s'est produite.")
            print(e)