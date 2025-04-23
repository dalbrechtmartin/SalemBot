import discord
from discord import app_commands
from discord.ext import commands
from utils.players_utils import player_exists, create_player
import asyncio  # N'oublions pas d'importer asyncio pour les erreurs de timeout

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
        user_id = interaction.user.id
        print(f"Commande 'meow' appelée par {interaction.user.name}")

        if player_exists(user_id):
            await interaction.response.send_message(
                embed=salem_embed(f"*meow.* Tu es déjà des nôtres, {interaction.user.display_name}.", self.bot)
            )
        else:
            await interaction.response.send_message(
                embed=salem_embed("Dis-moi... Quel est ton **prénom magique** ?", self.bot)
            )

            def check(m):
                # Vérification si le message provient du bon auteur et du bon canal
                print(f"Vérification du message de {m.author.name} dans le canal {m.channel.name}")
                return m.author.id == user_id and m.channel == interaction.channel

            try:
                # Attente du prénom
                print("Attente du prénom...")
                prenom_msg = await self.bot.wait_for("message", check=check, timeout=60)
                print(f"Prénom reçu : {prenom_msg.content}")

                if not prenom_msg.content.strip():  # Vérification si la réponse est vide
                    await interaction.followup.send(
                        embed=salem_embed("**Salem** : Hmm... Tu n'as pas répondu. Essaie encore.", self.bot)
                    )
                    return

                await interaction.followup.send(
                    embed=salem_embed("Et ton **nom d'héritage** ?", self.bot)
                )

                # Attente du nom
                print("Attente du nom...")
                nom_msg = await self.bot.wait_for("message", check=check, timeout=60)
                print(f"Nom reçu : {nom_msg.content}")

                if not nom_msg.content.strip():  # Vérification si la réponse est vide
                    await interaction.followup.send(
                        embed=salem_embed("**Salem** : Hmm... Tu n'as pas répondu. Essaie encore.", self.bot)
                    )
                    return

                # Création du profil
                print("Création du profil...")
                create_player(user_id, prenom_msg.content, nom_msg.content)
                await interaction.followup.send(
                    embed=salem_embed(f"Meow~ Enchanté, {prenom_msg.content} {nom_msg.content}. La magie t'accepte.", self.bot)
                )
            except asyncio.TimeoutError:
                # Si le temps est dépassé
                print("Le délai d'attente a été dépassé")
                await interaction.followup.send(
                    embed=salem_embed("Hmm... Le silence est louche. Reviens me voir plus tard.", self.bot)
                )
            except Exception as e:
                # Autres erreurs
                print(f"Erreur : {e}")
                await interaction.followup.send(
                    embed=salem_embed(f"Une erreur est survenue : {e}", self.bot)
                )
