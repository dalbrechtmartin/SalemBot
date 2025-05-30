import discord
from discord import app_commands
from discord.ext import commands

from utils.players_utils import player_exists, get_player, get_player_interaction
from utils.translations_utils import translate
from utils.logs_utils import log_command_usage

from embeds.error_embed import error_embed

class ProfileCommand(commands.Cog):
    
    command_name = "profil"
    command_description = "Affiche ton profil magique."
    
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name=command_name, description=command_description)
    async def profile(self, interaction: discord.Interaction):
        user_id, user_nickname, user_lang = get_player_interaction(interaction)
        log_command_usage(interaction.command.name, user_id, user_nickname, user_lang)

        if player_exists(user_id):
            try:
                player_data = get_player(user_id)
                if not player_data:
                    raise Exception(translate("profile.not_registered"))

                embed = discord.Embed(
                    title=f"Profil de {user_nickname}",
                    color=discord.Color.purple()
                )
                embed.set_thumbnail(url=interaction.user.display_avatar.url)
                embed.add_field(name="Niveau", value=f"`{player_data['level']}`", inline=True)
                embed.add_field(name="XP", value=f"`{player_data['xp']}`", inline=True)
                embed.add_field(name="Or", value=f"`{player_data['gold']}`", inline=True)
                wand_info = player_data['wand'] if player_data['wand'] else translate("item.missing")
                embed.add_field(name="Baguette", value=f"`{wand_info}`", inline=False)
                inventory = player_data['inventory'] or []
                inventory_text = translate("item.missing") if not inventory else ", ".join(map(str, inventory))
                embed.add_field(name="Inventaire", value=f"`{inventory_text}`", inline=False)
                quests = player_data['quests'] or []
                quests_text = translate("quests.empty") if not quests else "\n".join(map(str, quests))
                embed.add_field(name="Quêtes", value=f"`{quests_text}`", inline=False)
                achievements = player_data['achievements'] or []
                achievements_text = translate("achievements.empty") if not achievements else "\n".join(map(str, achievements))
                embed.add_field(name="Réalisations", value=f"`{achievements_text}`", inline=False)
                embed.set_footer(text="Meow~")
                await interaction.response.send_message(embed=embed)
            except Exception as e:
                print(f"Erreur : {e}")
                await interaction.followup.send(
                    embed=error_embed(
                        translate("profile.error", user_lang),
                        self.bot
                    )
                )
        else:
            await interaction.response.send_message(
                embed=error_embed(
                    translate("profile.not_registered", user_lang),
                    self.bot
                )
            )