import discord
import os
import dotenv

dotenv.load_dotenv()

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
        'cogs.math',
    ]

    for i, extension in enumerate(extensions, 1):
        bot.load_extension(extension)
        print(f"Loaded {i}/{len(extensions)} extensions")


bot.run(os.getenv("TOKEN"))