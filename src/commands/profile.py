import discord
from discord import app_commands
from discord.ext import commands

from utils.players_utils import player_exists, get_player, get_player_interaction, get_player_avatar_interaction
from utils.translations_utils import translate
from utils.logs_utils import log_command_usage

from embeds.error_embed import error_embed
from embeds.profile_embed import profile_embed

class ProfileCommand(commands.Cog):
    
    command_name = "profil"
    command_description = "Affiche ton profil magique."
    
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name=command_name, description=command_description)
    async def profile(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=False)
        
        user_id, user_nickname, user_lang = get_player_interaction(interaction)
        user_avatar = get_player_avatar_interaction(interaction)
        log_command_usage(interaction.command.name, user_id, user_nickname, user_lang)

        if player_exists(user_id):
            try:
                player_data = get_player(user_id)

                embed = profile_embed(self.bot, player_data, user_nickname, user_lang, user_avatar)
                await interaction.followup.send(embed=embed)
            except Exception as e:
                print(f"Erreur : {e}")
                await interaction.followup.send(
                    embed=error_embed(
                        translate("profile.error", user_lang),
                        self.bot
                    )
                )
        else:
            await interaction.followup.send(
                embed=error_embed(
                    translate("profile.not_registered", user_lang),
                    self.bot
                )
            )