import random
import re

import discord
from discord import (ApplicationContext, IntegrationType,
                     InteractionContextType)
from discord.ext import commands


class Owoifier:
    def __init__(self, text):
        self.text = text

    def owo(self):  # pasted from SEOwned lmfao
        patterns = [
            ("r", "w"),
            ("R", "W"),
            ("n([aeiou])", "ny\\1"),
            ("N([aeiou])", "Ny\\1"),
            ("N([AEIOU])", "NY\\1"),
        ]

        suffixes = [
            "UwU",
            "OwO",
            "owo",
            "uwu",
            "nwn",
            ":3",
            ">w<",
            "^w^",
            "<3",
            "^_^",
            "^-^",
            ">_<",
            ";3",
            "x3",
            ">:3"
        ]

        for pattern, replacement in patterns:
            self = re.sub(pattern, replacement, self)
        if len(self):
            suffix = random.choice(suffixes)
            self += " " + suffix
        return self


class Owoify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='owoify',
        description='owoify text',
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def owoify(
            self,
            ctx: ApplicationContext,
            text: str
    ):
        await ctx.respond(Owoifier.owo(str(text)))  # use string moron

    @commands.message_command(
        name='owoify',
        description='owoify text',
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def owoify(
            self,
            ctx: ApplicationContext,
            message: discord.Message
    ):
        await ctx.respond(Owoifier.owo(str(message.content)))


def setup(bot):
    bot.add_cog(Owoify(bot))
