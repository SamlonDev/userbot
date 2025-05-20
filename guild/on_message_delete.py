import discord
from discord.ext import commands

class on_message_delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        logs = 1305896232950169731
        await self.bot.get_channel(logs).send(f"{message.author.display_name} deleted: {message.content}")

def setup(bot):
    bot.add_cog(on_message_delete(bot))