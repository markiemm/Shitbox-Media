import asyncio
import json
import os
import sys

import discord
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' file could not be detected!")
else:
    config = json.load(open("config.json", "r", encoding="utf-8"))
    print("Loaded the 'config.json' file")

try:
    config = json.load(open("config.json", "r", encoding="utf-8"))
    print("Loaded the 'config.json' file")
except FileNotFoundError:
    sys.exit("'config.json' file could not be detected!")
except Exception as e:
    sys.exit(f"Error: {e}")

client = commands.Bot(command_prefix=">")
client.remove_command("help")

# Loading all the cogs in the ./cogs folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@commands.command()
async def reload(message, *, extension_name):
    """
    Reload an extension(cog) from the client

    Args:
        message (commands.Context): Passed by default
        extension_name (str): Cogs file name

    Config.json edit:
        {
            manage_client_cogs:[624633250232401961,823400917960753202]
        }
    """
    if message.author.id in config["manage_client_cogs"]:
        clientmsg = await message.channel.send("Reloading the client... - *Please Wait*")
        client.unload_extension(f'cogs.{extension_name[:-3]}')
        # just time.sleep(5) will not work here as intended
        await asyncio.sleep(3)
        client.load_extension(f'cogs.{extension_name[:-3]}')
        await clientmsg.edit(content="**Done!**")
    else:
        await message.channel.send("You do not have permission to use this command")

client.run(config["discord_token"])
