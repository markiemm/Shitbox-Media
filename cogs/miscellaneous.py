import discord
from discord.ext import commands
from utils.db import config


class Miscellaneous(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.client.remove_command("help")  # for the custom help command

    @commands.command()
    async def help(self, message):
        embed = discord.Embed(title="Help menu")
        embed.set_author(name=f"{self.client.user.name}",
                         icon_url=f"{self.client.user.avatar_url}")
        embed.add_field(
            name="status", value="View the status of the service.", inline=False)
        embed.add_field(
            name="media", value="View storage information.", inline=False)
        embed.add_field(
            name="queue", value="View the download queue.", inline=False)

        # If the user can manage the cogs (mentioned in the config.json as a list)
        if message.author.id in config["manage_client_cogs"]:
            embed.add_field(
                name="load <cog-name>", value="Load a cog.", inline=False)
            embed.add_field(
                name="unload <cog-name>", value="Unload a already loaded cog.", inline=False)
            embed.add_field(
                name="reload <cog-name>", value="Reload a cog.", inline=False)

        await message.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Miscellaneous(client))
