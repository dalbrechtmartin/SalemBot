import discord
from discord import app_commands
from discord.ext import commands
from utils.players_utils import player_exists, create_player
from utils.translations_utils import translate
import asyncio 

def salem_embed(description: str, bot: commands.Bot) -> discord.Embed:
    avatar_url = bot.user.avatar.url if bot.user.avatar else None
    embed = discord.Embed(
        description=description,
        color=discord.Color.purple()
    )
    embed.set_author(name="Meow~", icon_url=None)
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
        user_lang = interaction.locale
        
        # Logs
        print(f"Commande 'meow' appelée par {user_nickname} ({user_id}) [{user_lang}]")

        if player_exists(user_id):
            await interaction.response.send_message(
                embed=salem_embed(
                    translate("meow.already_registered", user_lang, name=user_nickname),
                    self.bot
                )
            )
        else:
            await interaction.response.send_message(
                embed=salem_embed(
                    translate("meow.welcome", user_lang, name=user_nickname),
                    self.bot
                )
            )

            try:
                create_player(user_id, user_nickname)
                await interaction.followup.send(
                    embed=salem_embed(
                        translate("meow.profile_created", user_lang, name=user_nickname),
                        self.bot
                    )
                )
            except asyncio.TimeoutError:
                print("Le délai d'attente a été dépassé")
                await interaction.followup.send(
                    embed=salem_embed(
                        translate("meow.timeout", user_lang),
                        self.bot
                    )
                )
            except Exception as e:
                print(f"Erreur : {e}")
                await interaction.followup.send(
                    embed=salem_embed(
                        translate("meow.error", user_lang, error=str(e)),
                        self.bot
                    )
                )