import discord
from discord.ext import commands
from main import bot, filename


class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, message):
        embed = discord.Embed(title="Help menu")
        embed.set_author(name="Shitbox Media Control Bot")
        embed.add_field(name="Status", value="View the status of the service.", inline=False)
        embed.add_field(name="Media", value="View storage information.", inline=False)
        embed.add_field(name="queue", value="View the download queue.", inline=False)
        await message.send(embed=embed)

    @commands.command()
    async def reload(self, message):
        bot.unload_extension(f'cogs.{filename[:-3]}')
        bot.load_extension(f'cogs.{filename[:-3]}')

    @commands.command()
    async def testnuts(self, message):
        await message.channel.send("this is not a test message")
        

def setup(client):
    client.add_cog(Miscellaneous(client))