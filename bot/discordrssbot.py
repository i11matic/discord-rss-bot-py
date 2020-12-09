import os
import json
from discord.ext import commands
from bot.utils import RssReader


class DiscordRssBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reader = RssReader(os.getenv("RSS_URL"))

        @self.event
        async def on_ready():
            print('Logged in as')
            print(self.user.name)
            print(self.user.id)
            print('-----------')

        @self.command()
        async def list_torrents(ctx, items=10):
            torrents = self.__format_torrents(
                self.reader.get_torrents(self.reader.torrent_dict, items))
            if self.reader.check_content_length(torrents):
                await ctx.send(torrents)
            else:
                await ctx.send("length is greater than 2000 Character")

        @self.command()
        async def get_rss_info(ctx):
            await ctx.send(self.__format_torrents(self.reader.get_rss_info()))

    def __format_torrents(self, torrent_dict: dict):
        torrent_dict = "\n```{}\n```".format(
            json.dumps(torrent_dict, indent=4, sort_keys=True))
        return torrent_dict