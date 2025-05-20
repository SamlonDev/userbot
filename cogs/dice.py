from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import random

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="dice",
        description="Roll a dice",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def dice(
        self, 
        ctx: ApplicationContext, 
        number: int
    ):
        dice_roll = random.randint(1, number)
        await ctx.respond(f"d{number} rolled {dice_roll}")
        return

def setup(bot):
    bot.add_cog(dice(bot))