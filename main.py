import discord
import requests
import json
import os
import sys
import subprocess
# import config
from discord import channel
#from discord.ext.commands.core import T, group
from discord.member import flatten_user
from discord.utils import valid_icon_size
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from hurry.filesize import alternative

if not os.path.isfile("config.json"):
    sys.exit("'config.json' file could not be detected!")
else:
    config = json.load(open("config.json", "r", encoding="utf-8"))
    print("Loaded the 'config.json' file")

bot = commands.Bot(command_prefix=">")
bot.remove_command("help")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(config["discord_token"])
