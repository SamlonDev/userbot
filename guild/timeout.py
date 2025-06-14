import discord
from discord.ext import commands
from datetime import timedelta


class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    timeout_group = discord.SlashCommandGroup("timeout", "timeout commands")

    @timeout_group.command(description="timeout a member")
    @commands.has_permissions(moderate_members=True)
    async def timeout(
            self,
            ctx: discord.ApplicationContext,
            member: discord.Member,
            days: int = 0,
            hours: int = 0,
            minutes: int = 0,
            reason: str = "yes"
    ):
        await member.timeout(until=discord.utils.utcnow() + timedelta(days=days, hours=hours, minutes=minutes),
                             reason=reason)
        await ctx.respond(f'{member.mention} has been timed out for {reason}.')

    @timeout_group.command(description="untimeout a member")
    @commands.has_permissions(moderate_members=True)
    async def untimeout(
            self,
            ctx: discord.ApplicationContext,
            member: discord.Member,
            reason: str = "yes"
    ):
        await member.remove_timeout()
        await ctx.respond(f'{member.mention} has been untimeouted for {reason}.')


def setup(bot):
    bot.add_cog(Timeout(bot))
