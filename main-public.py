import discord
import os

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#on command exception
@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    await ctx.respond(f"I am not dead faggot.\n-# {error}", ephemeral=True)

if __name__ == '__main__':
    extensions = [
        'cogs.ping',
        'cogs.rate',
        'cogs.owoify',
        'cogs.web',
        'cogs.slots',
        'cogs.speechbubble',
        'cogs.russian',
        'cogs.ship',
        'cogs.dice',
        'cogs.transparentspeechbubble',
        'cogs.ksi',
        'cogs.kiss',
        'cogs.cuddle',
        'cogs.weather',
        'cogs.hug',
        'cogs.google',
        'cogs.pollinate',
        'cogs.loremipsum',
        'cogs.math',
        'guild.on_member_join',
        'guild.on_member_remove',
        'guild.on_message_edit',
        'guild.on_message_delete',
        'guild.ban',
        'guild.kick',
        'guild.timeout',
    ]

    for extension in extensions:
        bot.load_extension(extension)
        print(f'Loaded {extension}') # so I can know if I am not retarded

bot.run(os.getenv("TOKEN"))