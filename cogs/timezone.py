from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Attachment)
import discord
from discord.ext import commands
import datetime

class timezone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="timezone",
        description="Get the timezone of a location",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild
        ]
    )
    async def timezone(
        self,
        ctx: ApplicationContext,
        time: str = None,
        top: bool = False
    ):
        author = ctx.author
        if author.id == 323081571446030336:
            top = True
        
        subtract_time = 0
        if time == None or time == "":
            # get current time
            time = str(datetime.datetime.now().strftime("%H:%M"))
            if top == True:
                subtract_time = 6
            else:
                subtract_time = 0
        
        minutes = "00"
        new_time = 0
        # if am or pm is in time
        if ":" in time:
            gen_time = time.split(":")
            time = gen_time[0]
            minutes = gen_time[1]
        
        if "am" in time.lower():
            new_time = time.lower().replace("am", "").strip()
            time = new_time
            
        elif "pm" in time.lower():
            new_time = time.lower().replace("pm", "").strip()
            new_time = int(new_time) + 12
            time = new_time
        
        if subtract_time != 0:
            new_time = new_time + subtract_time
            time = int(time) - subtract_time
        
        if int(time) > 24:
            time = int(time) - 24
        
        if int(time) < 0:
            time = 24 + int(time)
        
        if top == False:
            bottom = "top's"
            # subtract 6 hours
            new_time = int(time) - 6

            if new_time < 0:
                new_time = 24 + new_time
              
        else:
            bottom = "bottom's"
            # add 6 hours
            new_time = int(time) + 6

            if new_time > 24:
                new_time = new_time - 24
        
        embed = discord.Embed(
            title="timezone",
            description=f"Your {time}:{minutes}, is yours {bottom} {new_time}:{minutes}",
            color=discord.Color.blue()
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(timezone(bot))