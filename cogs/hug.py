from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import discord
import random
import os

class hugView(discord.ui.View):
    def __init__(self, author, target):
        super().__init__()
        self.author = author
        self.target = target

    @discord.ui.button(label="hug Back x3", style=discord.ButtonStyle.primary)
    async def hug_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user.id != self.target.id:
            await interaction.response.send_message("This hug isn't for you to return!", ephemeral=True)
            return
        
        # choose a random file from the folder
        file_path = os.path.join('D:\\XxMamCukrzycexX\\pycord\\main\\Userbot-salmon-mech\\resources\\hug')
        files = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.gif')]
        file = discord.File(random.choice(files), filename="hug.gif")
        embed = discord.Embed(
            title=f"{self.target.name} hug's back {self.author.name} 💖",
            color=0xffc0cb
        )
        embed.set_image(url="attachment://hug.gif")
        await interaction.response.send_message(file=file, embed=embed)
        self.stop()

class hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def hug_user(self, ctx, user):
        file_path = os.path.join('D:\\XxMamCukrzycexX\\pycord\\main\\Userbot-salmon-mech\\resources\\hug')
        files = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.gif')]
        file = discord.File(random.choice(files), filename="hug.gif")
        embed = discord.Embed(
            title=f"{ctx.author.name} hugs {user.name} 💖",
            color=0xffc0cb
        )
        embed.set_image(url="attachment://hug.gif")
        view = hugView(ctx.author, user)
        await ctx.respond(file=file, embed=embed, view=view)
    
    @commands.slash_command(
        name="hug",
        description="hug someone :3",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def hug(
        self,
        ctx: ApplicationContext,
        user: discord.Member
    ):
        await self.hug_user(ctx, user)
    
    @commands.user_command(
        name="hug",
        description="hug someone :3",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def user_hug(
        self,
        ctx: ApplicationContext,
        user: discord.Member
    ):
        await self.hug_user(ctx, user)


def setup(bot):
    bot.add_cog(hug(bot))
