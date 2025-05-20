
from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='ping',
        description='Check bot latency',
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def ping(
        self,
        ctx: ApplicationContext
    ):
        latency = self.bot.latency
        await ctx.respond(f'{latency * 1000:.2f} ms ({latency:.2f} s)')


def setup(bot):
    bot.add_cog(ping(bot))