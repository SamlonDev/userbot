import discord
from discord.ext import commands

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command()
    @commands.has_permissions(kick_members = True)
    async def kick(
        self,
        ctx,
        member = discord.Option(discord.Member, "The member to kick", required=True),
        reason = discord.Option(str, "The reason for the kick", required=False)
    ):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked for {reason}.')

def setup(bot):
    bot.add_cog(kick(bot))