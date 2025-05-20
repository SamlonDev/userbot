from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType, Attachment)
import discord
from discord.ext import commands
import requests
from io import BytesIO
from PIL import Image
from PIL import ImageDraw  #salmon import this


class transparentspeechbubble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='transparentspeechbubble',
        description='Generate a transparent speech bubble',
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def transparentspeechbubble(
        self,
        ctx: ApplicationContext,
        image: Attachment
    ):
        
        response = requests.get(image.url)
        original_img = Image.open(BytesIO(response.content)).convert("RGBA")
        
        #make gay mask
        mask = Image.new('L', original_img.size, 255)
        draw = ImageDraw.Draw(mask)
        
        #boubble size meth
        width, height = original_img.size
        bubble_width = width * 2  #wider
        bubble_height = int(height * 0.4)
        
        #were to put the bubble
        offset_y = -bubble_height * 0.7  #higher number = bouble go up higher
        x1 = -width//2  
        y1 = -bubble_height * 1.5 + offset_y  
        x2 = width * 1.5  
        y2 = bubble_height + offset_y  
        
        # Draw bottom half of circle
        draw.ellipse([x1, y1, x2, y2], fill=0)
        
        #salmons cute anal tail x3
        points = []
        for t in range(0, 101, 5):  #smooth swoop
            t = t / 100
            
            x = (1-t)**2 * (0) + 2*(1-t)*t * (width//2) + t**2 * (width//2)  # x curve 
            y = (1-t)**2 * (y2 - height//10) + 2*(1-t)*t * (y2 + height//20) + t**2 * (y2 + height//10)  # y curve
            points.append((int(x), int(y)))
        
        start_width = min(width, height) // 20  
        full_points = []
        for i, (x, y) in enumerate(points[:-1]):
            progress = i / len(points)
            current_width = start_width * (1 - progress)
            full_points.append((x, y + current_width))
        full_points.append(points[-1])
        for i, (x, y) in enumerate(reversed(points[:-1])):
            progress = (len(points) - i - 1) / len(points)
            current_width = start_width * (1 - progress)
            if progress < 0.1:
                current_width = 0
            full_points.append((x, y - current_width))
            
        draw.polygon(full_points, fill=0)
        
        #merge gay mask
        original_img.putalpha(mask)
        
        with BytesIO() as image_binary:
            original_img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.respond(file=discord.File(fp=image_binary, filename='transparentspeechbubble.png'))

            return
        
def setup(bot):
    bot.add_cog(transparentspeechbubble(bot))