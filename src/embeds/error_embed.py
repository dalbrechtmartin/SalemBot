import discord
from discord.ext import commands

def error_embed(description: str, bot: commands.Bot, author: str = "Salem", footer: str = "Meow~") -> discord.Embed:
    avatar_url = bot.user.avatar.url if bot.user.avatar else None
    embed = discord.Embed(
        description=description,
        color=discord.Color.red()
    )
    embed.set_author(name=author, icon_url=avatar_url)
    embed.set_thumbnail(url=avatar_url)
    embed.set_footer(text=footer)
    return embed