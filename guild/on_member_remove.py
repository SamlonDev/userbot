import discord
from discord.ext import commands


class on_member_remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = 1305896872900300850
        await self.bot.get_channel(channel).send(f'Goodbye {member.mention}...')

def setup(bot):
    bot.add_cog(on_member_remove(bot))