import random
import re

from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import discord

class owo:
    def __init__(self, text):
        self.text = text

    def owo(text): # pasted from SEOwned lmfao
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
            text = re.sub(pattern, replacement, text)
        if len(text):
            suffix = random.choice(suffixes)
            text += " " + suffix
        return text

class owoify(commands.Cog):
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
        await ctx.respond(owo.owo(str(text))) # use string moron
    
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
        await ctx.respond(owo.owo(str(message.content)))
        
    
def setup(bot):
    bot.add_cog(owoify(bot))