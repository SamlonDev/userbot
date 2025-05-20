from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import discord

class KSI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="ksi",
        description="From The Screen To The Ring To The Pen To The King 🤑🤑🤑",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def ksi(self, ctx: ApplicationContext):
        file = discord.File("resources/ksi.jpg")
        embed = discord.Embed(title="From The Screen To The Ring To The Pen To The King 🤑🤑🤑", color=discord.Color.purple())
        embed.set_image(url="attachment://ksi.jpg")
        await ctx.respond(file=file, embed=embed)

def setup(bot):
    bot.add_cog(KSI(bot))
