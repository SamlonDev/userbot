from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Attachment)
import discord
from discord.ext import commands
import requests
from io import BytesIO
from PIL import Image


class speechbubble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='speechbubble',
        description='Generate a speech bubble',
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def speechbubble(
        self,
        ctx: ApplicationContext,
        image: Attachment
    ):
        
        response = requests.get(image.url)
        original_img = Image.open(BytesIO(response.content))
        overlay = Image.open('resources/speechbubble.png').convert("RGBA")
        overlay = overlay.resize((original_img.width, original_img.height), Image.Resampling.BICUBIC)
        combined_img = Image.alpha_composite(original_img.convert("RGBA"), overlay)
        with BytesIO() as image_binary:
            combined_img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.respond(file=discord.File(fp=image_binary, filename='speechbubble.png'))

            return
        
def setup(bot):
    bot.add_cog(speechbubble(bot))