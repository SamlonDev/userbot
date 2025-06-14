import os

import discord
import requests
from discord import (ApplicationContext, IntegrationType,
                     InteractionContextType)
from discord.ext import commands


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="Weather",
        description="Check the Weather in your city",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild
        ]
    )
    async def weather(
            self,
            ctx: ApplicationContext,
            city=discord.Option(str, "City to check Weather in", required=False)
    ):
        await ctx.defer()
        api_key = os.getenv("WEATHER_API_KEY")
        current = "http://api.openweathermap.org/data/2.5/weather?"

        if city is None or city == "":
            if ctx.author.id == 323081571446030336:
                city = "Kitchener"
            elif ctx.author.id == 1204201769006145556:
                city = "Kiełczów"

        complete_url = current + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = round(y["temp"])
            current_feels_like = round(y["feels_like"])
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["Weather"]
            weather_description = z[0]["description"]
            embed = discord.Embed(
                title=f"Weather in {city}",
                color=0x00ff00
            )
            embed.add_field(name="Temperature", value=f"{current_temperature}°C", inline=True)
            embed.add_field(name="Feels like", value=f"{current_feels_like}°C", inline=True)
            embed.add_field(name="Humidity", value=f"{current_humidiy}%", inline=True)
            embed.add_field(name="Pressure", value=f"{current_pressure}hPa", inline=True)
            embed.add_field(name="Description", value=weather_description, inline=True)
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("404 error faggit", ephemeral=True)


def setup(bot):
    bot.add_cog(Weather(bot))
