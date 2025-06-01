from embeds.general_embed import general_embed
from utils.translations_utils import translate

def profile_embed(bot, player_data, user_nickname, user_lang, user_avatar):
    embed = general_embed(
        bot=bot,
        title=translate("profile.title", user_lang, name=user_nickname),
    )
    embed.add_field(
        name=translate("profile.level", user_lang),
        value=f"`{player_data['level']}`",
        inline=True
    )
    embed.add_field(
        name=translate("profile.xp", user_lang),
        value=f"`{player_data['xp']}`",
        inline=True
    )
    embed.add_field(
        name=translate("profile.gold", user_lang),
        value=f"`{player_data['gold']}`",
        inline=True
    )
    # ...
    embed.set_thumbnail(url=user_avatar)
    return embed