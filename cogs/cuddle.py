import os
import random

import discord
from discord import (ApplicationContext, IntegrationType,
                     InteractionContextType)
from discord.ext import commands


class CuddleView(discord.ui.View):
    def __init__(self, author, target):
        super().__init__()
        self.author = author
        self.target = target

    @discord.ui.button(label="Cuddle Back x3", style=discord.ButtonStyle.primary)
    async def cuddle_back(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id != self.target.id:
            await interaction.response.send_message("This cuddle isn't for you to return!", ephemeral=True)
            return

        # choose a random file from the folder
        file_path = os.path.join('D:\\XxMamCukrzycexX\\pycord\\main\\Userbot-salmon-mech\\resources\\cuddle')
        files = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.gif')]
        file = discord.File(random.choice(files), filename="cuddle.gif")
        embed = discord.Embed(
            title=f"{self.target.name} cuddle's back {self.author.name} 💖",
            color=0xffc0cb
        )
        embed.set_image(url="attachment://cuddle.gif")

        if interaction.response.is_done():
            await interaction.followup.send(file=file, embed=embed)
        else:
            await interaction.response.send_message(file=file, embed=embed)

        self.stop()


class Cuddle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def send_cuddle(ctx, user):
        file_path = os.path.join('D:\\XxMamCukrzycexX\\pycord\\main\\Userbot-salmon-mech\\resources\\cuddle')
        files = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.gif')]
        file = discord.File(random.choice(files), filename="cuddle.gif")
        embed = discord.Embed(
            title=f"{ctx.author.name} cuddles {user.name} 💖",
            color=0xffc0cb
        )
        embed.set_image(url="attachment://cuddle.gif")
        view = CuddleView(ctx.author, user)
        await ctx.respond(file=file, embed=embed, view=view)  # await the ctx.respond() method

    @commands.slash_command(
        name="cuddle",
        description="Cuddle with someone :3",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def cuddle(
            self,
            ctx: ApplicationContext,
            user: discord.Member
    ):
        await self.send_cuddle(ctx, user)

    @commands.user_command(
        name="cuddle",
        description="Cuddle with someone :3",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def user_cuddle(
            self,
            ctx: ApplicationContext,
            user: discord.Member
    ):
        await self.send_cuddle(ctx, user)


def setup(bot):
    bot.add_cog(Cuddle(bot))
