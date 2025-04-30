import discord
from discord import app_commands
from discord.ext import commands
from utils.players_utils import player_exists, create_player
import asyncio 

def salem_embed(description: str, bot: commands.Bot) -> discord.Embed:
    avatar_url = bot.user.avatar.url if bot.user.avatar else None
    embed = discord.Embed(
        description=description,
        color=discord.Color.purple()
    )
    embed.set_author(name="Salem", icon_url=avatar_url)
    embed.set_thumbnail(url=avatar_url)
    return embed

class MeowCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="meow", description="Commence ton initiation magique avec Salem.")
    async def meow(self, interaction: discord.Interaction):
        
        # Variables
        user_id = interaction.user.id
        user_nickname = interaction.user.display_name
        
        # Debug
        print(f"Commande 'meow' appelée par {user_nickname} ({user_id})")

        if player_exists(user_id):
            await interaction.response.send_message(
                embed=salem_embed(f"*Meow.* Tu es déjà des nôtres, {user_nickname}.", self.bot)
            )
        else:
            await interaction.response.send_message(
                embed=salem_embed(f"*Meow*... Bonjour, {user_nickname} !", self.bot)
            )

            try:
                # Création du profil
                print("Création du profil...")
                create_player(user_id, user_nickname)
                await interaction.followup.send(
                    embed=salem_embed(f"*Meow~* Enchanté, {user_nickname}. La magie t'accepte.", self.bot)
                )
            except asyncio.TimeoutError:
                # Timeout
                print("Le délai d'attente a été dépassé")
                await interaction.followup.send(
                    embed=salem_embed("*Hmm...* Le silence est louche. Reviens me voir plus tard.", self.bot)
                )
            except Exception as e:
                # Autres erreurs
                print(f"Erreur : {e}")
                await interaction.followup.send(
                    embed=salem_embed(f"Une erreur est survenue : {e}", self.bot)
                )
