from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import discord
import re

class SubMath():
    def calculate(expression):
        expression = expression.replace("x", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("^", "**")
        return eval(expression)
    
class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(
        name="math", 
        description="do math",
                integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def math(self, ctx: ApplicationContext, equation: str):
        result = SubMath.calculate(equation)
        await ctx.respond(f"{equation} = {result}")

def setup(bot):
    bot.add_cog(Math(bot))