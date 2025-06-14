import random

from discord import (ApplicationContext, IntegrationType,
                     InteractionContextType)
from discord.ext import commands


class Rate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='rate',
        description='Rate something',
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def rate(
            self,
            ctx: ApplicationContext,
            firstname: str,
            secondname: str
    ):
        rate = random.randint(1, 100)
        description = f'{firstname} is {rate}% {secondname}!'
        await ctx.respond(description)


def setup(bot):
    bot.add_cog(Rate(bot))
