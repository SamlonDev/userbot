from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import random
import discord

class Ship(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def ship_users(self, ctx: ApplicationContext, user1: discord.Member, user2: discord.Member):
        love = random.randint(1, 100)
        if love <= 35:
            emoji = ":broken_heart:"
        elif 35 < love <= 90:
            emoji = ":heart:"
        else:
            emoji = ":sparkling_heart:"
        await ctx.respond(content=(f"{emoji} **{user1.display_name}** is compatible with **{user2.display_name}** in **{love}%**! {emoji}"))

    @commands.slash_command(
        name="ship",
        description="Ship 2 users",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def ship(
        self,
        ctx: ApplicationContext,
        user1: discord.Member,
        user2: discord.Member,
    ):
        await self.ship_users(ctx, user1, user2)

    @commands.user_command(
        name="ship",
        description="Ship 2 users",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def ship_user(
        self,
        ctx: ApplicationContext,
        user2: discord.Member
    ):
        await self.ship_users(ctx, ctx.author, user2)


def setup(bot):
    bot.add_cog(Ship(bot))