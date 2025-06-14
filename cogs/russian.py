import re

import discord
from discord import (ApplicationContext, IntegrationType,
                     InteractionContextType)
from discord.ext import commands


class Pattern:
    def __init__(self, text):
        self.text = text

    def russia(self):
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
            self = re.sub(pattern, replacement, self)

        return self


class Russian(commands.Cog):
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
        await ctx.respond(Pattern.russia(text))
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
        await ctx.respond(Pattern.russia(message.content))
        return


def setup(bot):
    bot.add_cog(Russian(bot))
