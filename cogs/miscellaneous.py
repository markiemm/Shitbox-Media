import discord
from discord.ext import commands


class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, message):
        embed = discord.Embed(title="Help menu")
        embed.set_author(name=f"{self.client.user.name}",
                         icon_url=f"{self.client.user.avatar_url}")
        embed.add_field(
            name="Status", value="View the status of the service.", inline=False)
        embed.add_field(
            name="Media", value="View storage information.", inline=False)
        embed.add_field(
            name="queue", value="View the download queue.", inline=False)
        await message.send(embed=embed)


def setup(client):
    client.add_cog(Miscellaneous(client))
