import discord
from discord.ext import commands

def general_embed(bot: commands.Bot, title: str = None, description: str = None, author: str = "Salem", footer: str = "Meow~") -> discord.Embed:
    avatar_url = bot.user.display_avatar.url if bot.user.display_avatar else None
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color.dark_green()
    )
    embed.set_author(name=author, icon_url=avatar_url)
    embed.set_thumbnail(url=avatar_url)
    embed.set_footer(text=footer)
    return embed