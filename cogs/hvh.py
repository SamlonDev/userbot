from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import discord
import random

class hvh(commands.Cog):
    def __init__(self, bot):    
        self.bot = bot
    
    @commands.slash_command(
        name="hvh",
        description="HvH",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def hvh(
        self, 
        ctx: ApplicationContext,
        member2: discord.Member = None
        ):
        member1 = ctx.author
        if not member2:
            await ctx.respond("Please specify a user")
            return
        if member1 == member2:
            await ctx.respond("Please specify a different user")
            return

        # change it into dictionaries
        member1_values = dict(accuracy=0, health=100)
        member2_values = dict(accuracy=0, health=100)

        # initialize turn
        turn = member1

        view = discord.ui.View()
        Shoot = discord.ui.Button(
            label="Shoot",
        )
        ChangeAA = discord.ui.Button(
            label="Change AA",
        )
        Shittalk = discord.ui.Button(
            label="Shittalk",
        )
        async def shoot_callback(interaction: discord.Interaction):
            nonlocal turn  # use nonlocal keyword to modify turn variable
            if interaction.user != turn:
                await interaction.response.send_message("Not your turn!", ephemeral=True)
                return
            if turn == member1:
                defender = member2
                attacker_values = member1_values
                defender_values = member2_values
            else:
                defender = member1
                attacker_values = member2_values
                defender_values = member1_values
            
            accuracy = random.randint(0, 20)
            
            # apply the values to a dictionary instead
            accuracy += attacker_values["accuracy"]
            if accuracy > 100:
                accuracy = 100
            elif accuracy < 0:
                accuracy = 0
            
            if accuracy == 100:
                damage = 100
                defender_values["health"] -= damage
                turn = member2 if turn == member1 else member1
                embed.description += f"\n{interaction.user.mention} one taps {turn.mention}."
                await interaction.response.edit_message(embed=embed, view=None)
                
            elif accuracy > 25:
                damage = accuracy - 25
                # apply damage
                defender_values["health"] -= damage
                turn = member2 if turn == member1 else member1
                if defender_values["health"] <= 0:
                    embed.description += f"\n# {defender.mention} is dead."
                    await interaction.response.edit_message(embed=embed, view=None)
                    return
                embed.description += f"\n{interaction.user.mention} shoots {turn.mention}. It deals {damage} damage. {turn.mention} has {defender_values['health']}. It's now {turn.mention}'s turn."
                await interaction.response.edit_message(embed=embed)
                
            else:
                # switch turn
                turn = member2 if turn == member1 else member1
                embed.description += f"\n{interaction.user.mention} can't hit supreme AA. It's now {turn.mention}'s turn."
                await interaction.response.edit_message(embed=embed)
                return
            
        Shoot.callback = shoot_callback
        view.add_item(Shoot)
        
        async def changeaa_callback(interaction: discord.Interaction):
            nonlocal turn  # use nonlocal keyword to modify turn variable
            if interaction.user != turn:
                await interaction.response.send_message("Not your turn!", ephemeral=True)
                return

            if turn == member1:
                defender = member2
                attacker_values = member1_values
                defender_values = member2_values
            else:
                defender = member1
                attacker_values = member2_values
                defender_values = member1_values
            
            accuracy = random.randint(0, 20)
            accuracy += attacker_values["accuracy"]
            
            if accuracy > 100:
                accuracy = 100
            elif accuracy < 0:
                accuracy = 0
            
            turn = member2 if turn == member1 else member1
            embed.description += f"\n{interaction.user.mention} fixes his shitty AA. It's now {turn.mention}'s turn."
            await interaction.response.edit_message(embed=embed)
            return
        
        ChangeAA.callback = changeaa_callback
        view.add_item(ChangeAA)
        
        async def shittalk_callback(interaction: discord.Interaction):
            nonlocal turn  # use nonlocal keyword to modify turn variable
            if interaction.user != turn:
                await interaction.response.send_message("Not your turn!", ephemeral=True)
                return
            if turn == member1:
                defender = member2
                attacker_values = member1_values
                defender_values = member2_values
            else:
                defender = member1
                attacker_values = member2_values
                defender_values = member1_values
            
            accuracy = random.randint(0, 20)
            accuracy -= defender_values["accuracy"]
            
            if accuracy > 100:
                accuracy = 100
            elif accuracy < 0:
                accuracy = 0
            
            turn = member2 if turn == member1 else member1
            embed.description += f"\n{interaction.user.mention} shittalks {turn.mention}. It's now {turn.mention}'s turn."
            await interaction.response.edit_message(embed=embed)
            return
        
        Shittalk.callback = shittalk_callback
        view.add_item(Shittalk)

            
        embed = discord.Embed(
            title="HvH",
            description=f"{member1.mention} vs {member2.mention}\nit's {member1.mention} turn",
            color=0xffc0cb,
        )
        await ctx.respond(embed=embed, view=view)
        
def setup(bot):
    bot.add_cog(hvh(bot))