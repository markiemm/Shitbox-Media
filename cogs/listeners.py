from discord.ext import commands
from main import bot


class listeners(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")


def setup(client):
    client.add_cog(listeners(client))