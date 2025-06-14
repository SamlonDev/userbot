import discord
from discord.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(ban_members=True)
    async def ban(
            self,
            ctx,
            member=discord.Option(discord.Member, "The member to ban", required=True),
            reason=discord.Option(str, "The reason for the ban", required=False)
    ):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned for {reason}.')


def setup(bot):
    bot.add_cog(Ban(bot))
