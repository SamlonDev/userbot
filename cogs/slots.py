import random

import discord
from discord import ApplicationContext, IntegrationType, InteractionContextType
from discord.ext import commands


class Slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.symbols = ['🍒', '🍊', '🍋', '🍇', '💎', '7️⃣']

    @commands.slash_command(
        name='slots',
        description="It's gambling time!",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def slots(self, ctx: ApplicationContext):
        result = [random.choice(self.symbols) for _ in range(3)]  # random slots

        slots_display = f"[ {result[0]} | {result[1]} | {result[2]} ]"  # display slots

        # make embed
        if len(set(result)) == 1:  # if slots are the same
            color = 0xFFD700
            title = "🎉 JACKPOT!"
            description = f"{slots_display}\nMEGA BIG WIN"
        elif len(set(result)) == 2:  # if two slots are the same
            color = 0x00FF00
            title = "🎯 You won't lose your money this time"
            description = f"{slots_display}\nTwo symbols match!"
        else:  # if no slots are the same
            color = 0xFF0000
            title = "99% of gamblers quit before they win"
            description = f"{slots_display}\nKeep trying!"

        # create // send embed
        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )
        embed.set_footer(text=f"Played by {ctx.author.name}")

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Slots(bot))
