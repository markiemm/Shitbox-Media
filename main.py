import discord
from hurry.filesize.filesize import size
import requests
import json
import os
import subprocess
from discord import channel
#from discord.ext.commands.core import T, group
from discord.member import flatten_user
from discord.utils import valid_icon_size
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from hurry.filesize import alternative
import platform
import sys
import config

if not os.path.isfile("config.json"):
    sys.exit("'config.json' file could not be detected!")
else:
    with open("config.json") as file:
        config = json.load(file)
print("Loaded the 'config.json' file")




bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    await bot.change_presence(activity=discord.Game("Shitbox"))


bot.remove_command("help")


bot.run(config["discord_token"])


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
