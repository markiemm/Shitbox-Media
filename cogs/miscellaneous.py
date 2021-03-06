import discord
from discord.ext import commands
import os
from main import bot, filename
import time


class miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")


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
        await message.channel.send("Reloading the bot...")
        bot.unload_extension(f'cogs.{filename[:-3]}')
        time.sleep(5)
        bot.load_extension(f'cogs.{filename[:-3]}')
        
        await message.channel.send("Done!")



def setup(client):
    client.add_cog(miscellaneous(client))