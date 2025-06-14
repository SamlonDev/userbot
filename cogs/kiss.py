import os
import random

import discord
from discord import (ApplicationContext, IntegrationType,
                     InteractionContextType)
from discord.ext import commands


class KissView(discord.ui.View):
    def __init__(self, author, target):
        super().__init__()
        self.author = author
        self.target = target

    @discord.ui.button(label="Kiss Back x3", style=discord.ButtonStyle.primary)
    async def kiss_back(self, interaction: discord.Interaction):
        if interaction.user.id != self.target.id:
            await interaction.response.send_message("This kiss isn't for you to return!", ephemeral=True)
            return

        # choose a random file from the folder
        file_path = os.path.join('D:\\XxMamCukrzycexX\\pycord\\main\\Userbot-salmon-mech\\resources\\kiss\\normal')
        files = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.gif')]
        file = discord.File(random.choice(files), filename="kiss.gif")
        embed = discord.Embed(
            title=f"{self.target.name} returned {self.author.name}'s kiss X3",
            color=0xffc0cb
        )
        embed.set_image(url="attachment://kiss.gif")
        await interaction.response.send_message(file=file, embed=embed)
        self.stop()

    @discord.ui.button(label="Don't Kiss Back :c", style=discord.ButtonStyle.secondary)
    async def no_kiss(self, interaction: discord.Interaction):
        if interaction.user.id != self.target.id:
            await interaction.response.send_message("This kiss isn't for you to reject!", ephemeral=True)
            return

        embed = discord.Embed(
            title=f"{self.target.name} didn't want to kiss back :c",
            color=0xffc0cb
        )
        await interaction.response.send_message(embed=embed)
        self.stop()


class Kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def kiss_user(ctx, user):
        await ctx.defer()
        file_path = os.path.join('D:\\XxMamCukrzycexX\\pycord\\main\\Userbot-salmon-mech\\resources\\kiss\\normal')
        files = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.gif')]
        file = discord.File(random.choice(files), filename="kiss.gif")
        embed = discord.Embed(
            title=f"{ctx.author.name} kissed {user.name}! 💖",
            color=0xffc0cb
        )
        embed.set_image(url="attachment://kiss.gif")
        view = KissView(ctx.author, user)
        await ctx.respond(file=file, embed=embed, view=view)

    @commands.slash_command(
        name="kiss",
        description="Kiss another person x3",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def kiss(
            self,
            ctx: ApplicationContext,
            user: discord.Member
    ):
        await self.kiss_user(ctx, user)

    @commands.user_command(
        name="kiss",
        description="Kiss another person x3",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def user_kiss(
            self,
            ctx: ApplicationContext,
            user: discord.Member
    ):
        await self.kiss_user(ctx, user)


def setup(bot):
    bot.add_cog(Kiss(bot))
