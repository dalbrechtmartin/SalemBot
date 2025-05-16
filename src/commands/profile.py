import discord
from discord import app_commands
from discord.ext import commands

from utils.players_utils import player_exists, load_players, get_player_interaction
from utils.translations_utils import translate
from utils.logs_utils import log_command_usage

from embeds.error_embed import error_embed

class ProfileCommand(commands.Cog):
    
    # Paramètres de la commande
    command_name = "profil"
    command_description = "Affiche ton profil magique."
    
    # Initialisation de la commande
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name=command_name, description=command_description)
    async def profile(self, interaction: discord.Interaction):
        
        # Variables
        user_id, user_nickname, user_lang = get_player_interaction(interaction)
        
        # Logs
        log_command_usage(interaction.command.name, user_id, user_nickname, user_lang)

        if player_exists(user_id):
            try:
                # Charger les données du joueur
                players_data = load_players()
                player_data = players_data[str(user_id)]
                
                # Embed avec les informations du joueur
                embed = discord.Embed(
                    title=f"Profil de {player_data['nickname']}",
                    color=discord.Color.purple()
                )
                
                # Avatar de l'utilisateur
                embed.set_thumbnail(url=interaction.user.display_avatar.url)
                
                # Informations de base
                embed.add_field(name="Niveau", value=f"`{player_data['level']}`", inline=True)
                embed.add_field(name="XP", value=f"`{player_data['xp']}`", inline=True)
                embed.add_field(name="Or", value=f"`{player_data['gold']}`", inline=True)
                
                # Baguette
                wand_info = player_data['wand'] if player_data['wand'] else "Aucune baguette"
                embed.add_field(name="Baguette", value=f"`{wand_info}`", inline=False)
                
                # Inventaire
                inventory = player_data['inventory']
                inventory_text = "Vide" if not inventory else ", ".join(inventory)
                embed.add_field(name="Inventaire", value=f"`{inventory_text}`", inline=False)
                
                # Quêtes
                quests = player_data['quests']
                quests_text = "Aucune quête" if not quests else "\n".join(quests)
                embed.add_field(name="Quêtes", value=f"`{quests_text}`", inline=False)
                
                # Réalisations
                achievements = player_data['achievements']
                achievements_text = "Aucune réalisation" if not achievements else "\n".join(achievements)
                embed.add_field(name="Réalisations", value=f"`{achievements_text}`", inline=False)
                
                # Footer avec un message aléatoire de Salem
                embed.set_footer(text="Meow~")
                
                # Envoyer le profil
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