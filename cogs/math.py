from discord import (ApplicationContext, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import subprocess


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
        """
        Evaluates a mathematical expression using the qalc program.

        Parameters:
        equation (str): The mathematical expression to evaluate. This expression is passed directly to the qalc program.

        Returns:
        str: The result of the evaluation. If the expression is invalid, an error message is returned.

        Raises:
        subprocess.CalledProcessError: If the qalc program returns an error.
        """
        try:
            result = subprocess.check_output(f"qalc -e {equation}", shell=True)
            await ctx.respond(f"{result.decode('utf-8').strip()}")
        except subprocess.CalledProcessError as e:
            await ctx.respond(e, ephemeral=True)
            print(e)


def setup(bot):
    bot.add_cog(Math(bot))
