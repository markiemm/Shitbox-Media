__author__ = "Markiemm#0001"

import asyncio
import os
import discord
from discord.ext import commands
from utils.db import config


client = commands.Bot(command_prefix=">")


# Loading all the cogs in the ./cogs folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def load(message, *, extension_name):
    """
    Load an extension from the bot

    Args:
        message (commands.Context): Passed by default
        extension_name (str): Cogs file name
    """
    if message.author.id in config["manage_client_cogs"]:
        try:
            client.load_extension(f'cogs.{extension_name[:-3]}')
        except Exception as e:
            await message.channel.send(f"Unable to load {extension_name[:-3]}**: - ```{e}```")
            return
        await message.channel.send(f"Loaded {extension_name[:-3]}**")
    else:
        await message.channel.send("You do not have permission to use this command")


@client.command()
async def unload(message, *, extension_name):
    """
    Unload an extension from the bot

    Args:
        message (commands.Context): Passed by default
        extension_name (str): Cogs file name
    """
    if message.author.id in config["manage_client_cogs"]:
        try:
            client.unload_extension(f'cogs.{extension_name[:-3]}')
        except Exception as e:
            await message.channel.send(f"Unable to unload {extension_name[:-3]}**: - ```{e}```")
            return
        await message.channel.send(f"Unloaded {extension_name[:-3]}**")
    else:
        await message.channel.send("You do not have permission to use this command")


@client.command()
async def reload(message, *, extension_name):
    """
    Reload an extension(cog) from the bot

    Args:
        message (commands.Context): Passed by default
        extension_name (str): Cogs file name

    Config.json edit: (You dont want everyone to reload cogs of the bot)
        {
            manage_client_cogs:[624633250232401961,823400917960753202]
        }
    """
    if message.author.id in config["manage_client_cogs"]:
        clientmsg = await message.channel.send("Reloading the client... - *Please Wait*")
        try:
            client.unload_extension(f'cogs.{extension_name[:-3]}')
        except Exception as e:
            await message.channel.send(f"Unable to unload {extension_name[:-3]}**: - ```{e}```")
            return
        # just time.sleep(5) will not work here as intended
        await asyncio.sleep(3)
        try:
            client.load_extension(f'cogs.{extension_name[:-3]}')
        except Exception as e:
            await message.channel.send(f"Unable to load {extension_name[:-3]}**: - ```{e}```")
            return
        await clientmsg.edit(content="**Done!**")
    else:
        await message.channel.send("You do not have permission to use this command")


client.run(config["discord_token"])
