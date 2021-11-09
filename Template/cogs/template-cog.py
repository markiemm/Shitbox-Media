import discord
from discord.ext import commands


class Service(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def helplol(self, message):
        await message.channel.send("hello this is a test")
        



def setup(client):
    client.add_cog(Service(client))