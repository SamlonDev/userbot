import discord
from discord.ext import commands

class on_message_edit(commands.Cog):
    def __init__(self, bot):    
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        logs = 1305896232950169731
        await self.bot.get_channel(logs).send(f'{before.author.display_name}: {before.content}\nturned to\n{after.author.display_name}: {after.content}')

def setup(bot):
    bot.add_cog(on_message_edit(bot))