import discord
from discord import app_commands
from discord.ext import commands

import asyncio 

from utils.players_utils import player_exists, create_player, get_player_interaction
from utils.translations_utils import translate
from utils.logs_utils import log_command_usage

from embeds.general_embed import general_embed    
from embeds.error_embed import error_embed

class MeowCommand(commands.Cog):
    
    # Paramètres de la commande
    command_name = "meow"
    command_description = "Commence ton initiation magique avec Salem."
    
    # Initialisation de la commande
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name=command_name, description=command_description)
    async def meow(self, interaction: discord.Interaction):
        
        # Variables
        user_id, user_nickname, user_lang = get_player_interaction(interaction)
        
        # Logs
        log_command_usage(interaction.command.name, user_id, user_nickname, user_lang)

        if player_exists(user_id):
            await interaction.response.send_message(
                embed=general_embed(
                    translate("meow.already_registered", user_lang, name=user_nickname),
                    self.bot
                )
            )
        else:
            await interaction.response.send_message(
                embed=general_embed(
                    translate("meow.welcome", user_lang, name=user_nickname),
                    self.bot
                )
            )

            try:
                create_player(user_id, user_nickname)
                await interaction.followup.send(
                    embed=general_embed(
                        translate("meow.profile_created", user_lang, name=user_nickname),
                        self.bot
                    )
                )
            except asyncio.TimeoutError:
                await interaction.followup.send(
                    embed=error_embed(
                        translate("meow.timeout", user_lang),
                        self.bot
                    )
                )
            except Exception as e:
                await interaction.followup.send(
                    embed=error_embed(
                        translate("meow.error", user_lang),
                        self.bot
                    )
                )