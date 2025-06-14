import os

import discord
import google.generativeai as genai
from discord import (ApplicationContext, IntegrationType,
                     InteractionContextType)
from discord.ext import commands


class Google(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="heygoogle",
        description="google generative ai",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def google(
            self,
            ctx: ApplicationContext,
            text=discord.Option(str, "What do you want to ask Google?", required=True)
    ):
        """
        OOWA this so impressive gwachan >w<
        I can't believe you made this you are so good gwachan :3
        """
        await ctx.defer()
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            text + "\n write it in 50 words",
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=100
            )
        )
        await ctx.respond(response.text)


def setup(bot):
    bot.add_cog(Google(bot))
