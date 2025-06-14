from discord import (ApplicationContext, Embed, IntegrationType,
                     InteractionContextType)
from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup
import pytube
import urllib.parse


class Web(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='web',
        description='searches web using duck duck go',
        integration_types=[
            IntegrationType.user_install
        ],
        contexts=[
            InteractionContextType.bot_dm,
            InteractionContextType.private_channel,
            InteractionContextType.guild,
        ]
    )
    async def web(
            self,
            ctx: ApplicationContext,
            query: str
    ):
        await ctx.defer(ephemeral=True)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        url = f"https://duckduckgo.com/html/?q={query}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', class_='result__a')
            if links:
                embed = Embed(title="Search Results", description=f"Top results for: {query}", color=0x1E90FF)
                view = discord.ui.View(disable_on_timeout=True)
                for i, link in enumerate(links[:5], start=1):
                    title = link.text
                    if link.get('href').startswith('https://www.youtube.com/'):
                        try:
                            parsed_url = urllib.parse.urlparse(link.get('href'))
                            video_id = urllib.parse.parse_qs(parsed_url.query).get('v', [None])[0]
                            if video_id:
                                yt = pytube.YouTube(f'https://www.youtube.com/watch?v={video_id}')
                                title = yt.title
                        except Exception:
                            pass
                    embed.add_field(name=f"Result {i}", value=f"[{title}]({link.get('href')})", inline=False)
                    button = discord.ui.Button(label=f"Send Result {i}")

                    async def button_callback(interaction: discord.Interaction, link=link):
                        await interaction.response.send_message(link.get('href'))

                    button.callback = button_callback
                    view.add_item(button)
                await ctx.respond(embed=embed, view=view, ephemeral=True)
            else:
                await ctx.respond(content="No results found.", ephemeral=True)
        else:
            await ctx.respond(content=f"Error: {response.status_code}", ephemeral=True)


def setup(bot):
    bot.add_cog(Web(bot))
