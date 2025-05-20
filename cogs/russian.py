from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import discord
import re

class pattern():
    def __init__(self, text):
        self.text = text
    def russia(text):
        russian_patterns = [
            (r"[Ww]", "в"),
            (r"[Ee]", "е"),
            (r"[Rr]", "р"),
            (r"[Tt]", "т"),
            (r"[Yy]", "ы"),
            (r"[Uu]", "у"),
            (r"[Ii]", "и"),
            (r"[Oo]", "о"),
            (r"[Pp]", "п"),
            (r"[Aa]", "а"),
            (r"[Ss]", "с"),
            (r"[Dd]", "д"),
            (r"[Ff]", "ф"),
            (r"[Gg]", "г"),
            (r"[Hh]", "х"),
            (r"[Jj]", "й"),
            (r"[Kk]", "к"),
            (r"[Ll]", "л"),
            (r"[Zz]", "з"),
            (r"[Xx]", "ж"),
            (r"[Cc]", "ц"),
            (r"[Vv]", "в"),
            (r"[Bb]", "б"),
            (r"[Nn]", "н"),
            (r"[Mm]", "м"),
        ]

        for pattern, replacement in russian_patterns:
            text = re.sub(pattern, replacement, text)
        
        return text

class russian(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="russian",
        description="Convert letters to russian",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def russian(self, ctx: ApplicationContext, text: str):
        await ctx.respond(pattern.russia(text))
        return

    @commands.message_command(
        name="russian",
        description="Convert letters to russian",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def russian(self, ctx: ApplicationContext, message: discord.Message):
        await ctx.respond(pattern.russia(message.content))
        return

def setup(bot):
    bot.add_cog(russian(bot))