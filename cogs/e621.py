from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import discord

import random
import requests


class e621(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="e621",
        description="Get an image from e621",
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def e621(
        self, 
        ctx: ApplicationContext,
        tags: str = None,
        min_score: bool = False,
    ):
        # so discord doesn't forget about us
        await ctx.defer()
        print(tags, min_score)
        # user agent header so we won't get 403
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        if tags:
            tags = tags.replace(" ", "+")
        if tags and min_score:
            formula = f"?tags={tags}+order%3Ascore"
        elif tags:
            formula = f"?tags={tags}"
        elif min_score and tags == "":
            formula = f"?tags=order%3Ascore"
        else:
            formula = ""
        r = requests.get(
            f"https://e621.net/posts.json{formula}+-rating:safe+-rating:questionable+-futa+-loli+-shota+-cub+-vore+-guro+-scat+-watersports+-intersex",
            headers=header
        )
        query = r.url
        if r.status_code == 200:
            data = r.json()
            # if data is empty, don't do anything
            if len(data['posts']) == 0:
                await ctx.respond(content="No results found.")
                return
            post = random.choice(data['posts'])
                
                
            # if it's mp4 or webm, make url empty
            surl=""
            if post['file']['ext'] == 'mp4' or post['file']['ext'] == 'webm':
                url = ''
                surl = post['file']['url']
            else:
                url = post['file']['url']

            post_url = f"https://e621.net/posts/{post['id']}"
            
            # if description none, place placeholder
            if post['description'] == None or post['description'] == '' or len(post['description']) == 100:
                title = 'horny posting on top!'
            else:
                title = ""
            
            # score in format x (y/z)
            score = f"score: {post['score']['total']} ({post['score']['up']}/{post['score']['down']})"
            
            embed = Embed(
                # get the title from url
                title=title,
                description=score+"\n"+query,
                color=0x9932cc
            )
            embed.set_image(url=url)
            embed.set_footer(text=post_url)
            await ctx.respond(embed=embed)
            if surl or surl == '':
                await ctx.respond(surl)
        else:
            await ctx.respond(
                "Something went wrong. Please try again later."
            )

        return


def setup(bot):
    bot.add_cog(e621(bot))  