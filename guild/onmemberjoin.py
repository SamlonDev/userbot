from discord.ext import commands


class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = 1305896857049890878
        await self.bot.get_channel(channel).send(
            f'Welcome {member.mention}! Please read <#1305891767597666324> and have fun using our bot!')


def setup(bot):
    bot.add_cog(OnMemberJoin(bot))
