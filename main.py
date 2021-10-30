import discord
import requests
import json
import os
import platform
import sys
import subprocess
import aiohttp
# import config
from discord import channel
#from discord.ext.commands.core import T, group
from discord.member import flatten_user
from discord.utils import valid_icon_size
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from hurry.filesize import alternative
from hurry.filesize.filesize import size
from qbittorrentapi import Client, client
from qbittorrentapi import TorrentStates
from nude import Nude  # pip3 install nudepy
from io import BytesIO

if not os.path.isfile("config.json"):
    sys.exit("'config.json' file could not be detected!")
else:
    config = json.load(open("config.json", "r", encoding="utf-8"))
    print("Loaded the 'config.json' file")


public_qbit = Client(host='qbit.shitbox.media',
                     username=config["public_qbit"]["username"], password=config["public_qbit"]["password"])

private_qbit = Client(host='secure-qbit.shitbox.media',
                      username=config["private_qbit"]["username"], password=config["private_qbit"]["password"])

bot = commands.Bot(command_prefix=config)
bot.remove_command("help")


@bot.event
async def on_ready():
    # bot.user instead of bot.user.name to print the bot with the discriminator
    print(f"Logged in as {bot.user}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-"*22)
    await bot.change_presence(activity=discord.Game("Shitbox"))


@bot.command()
async def status(message):
    status_api_get_services = requests.get(
        "http://status.shitbox.media/api/services?api=" + config["status_api_key"])
    embed = discord.Embed(title="Status for shitbox.media")
    embed.set_author(name="Shitbox Media Control Bot", url="https://shitbox.media",
                     icon_url="https://media.discordapp.net/attachments/889169391038627872/891019443755421746/shitbox_logo_main.png?width=471&height=426")

    if str(status_api_get_services.json()[1]["online"]) == "True":
        service_1_status = ":green_circle:"
    else:
        service_1_status = ":red_circle:"

    ms_convert_1 = status_api_get_services.json()[1]["avg_response"] / 1000
    embed.add_field(name=str(status_api_get_services.json()[1]["name"]) + " (" + str(ms_convert_1) + " ms) " + str(
        service_1_status), value="Operating at " + str(status_api_get_services.json()[1]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

    if str(status_api_get_services.json()[2]["online"]) == "True":
        service_2_status = ":green_circle:"
    else:
        service_2_status = ":red_circle:"

    ms_convert_2 = status_api_get_services.json()[2]["avg_response"] / 1000
    embed.add_field(name=str(status_api_get_services.json()[2]["name"]) + " (" + str(ms_convert_2) + " ms) " + str(
        service_2_status), value="Operating at " + str(status_api_get_services.json()[2]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

    if str(status_api_get_services.json()[3]["online"]) == "True":
        service_3_status = ":green_circle:"
    else:
        service_3_status = ":red_circle:"

    ms_convert_3 = status_api_get_services.json()[3]["avg_response"] / 1000
    embed.add_field(name=str(status_api_get_services.json()[3]["name"]) + " (" + str(ms_convert_3) + " ms) " + str(
        service_3_status), value="Operating at " + str(status_api_get_services.json()[3]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

    if str(status_api_get_services.json()[4]["online"]) == "True":
        service_4_status = ":green_circle:"
    else:
        service_4_status = ":red_circle:"

    ms_convert_4 = status_api_get_services.json()[4]["avg_response"] / 1000
    embed.add_field(name=str(status_api_get_services.json()[4]["name"]) + " (" + str(ms_convert_4) + " ms) " + str(
        service_4_status), value="Operating at " + str(status_api_get_services.json()[4]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

    if str(status_api_get_services.json()[5]["online"]) == "True":
        service_5_status = ":green_circle:"
    else:
        service_5_status = ":red_circle:"

    ms_convert_5 = status_api_get_services.json()[5]["avg_response"] / 1000
    embed.add_field(name=str(status_api_get_services.json()[5]["name"]) + " (" + str(ms_convert_5) + " ms) " + str(
        service_5_status), value="Operating at " + str(status_api_get_services.json()[5]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

    if str(status_api_get_services.json()[6]["online"]) == "True":
        service_6_status = ":green_circle:"
    else:
        service_6_status = ":red_circle:"

    ms_convert_6 = status_api_get_services.json()[6]["avg_response"] / 1000
    embed.add_field(name=str(status_api_get_services.json()[6]["name"]) + " (" + str(ms_convert_6) + " ms) " + str(
        service_6_status), value="Operating at " + str(status_api_get_services.json()[6]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

    if str(status_api_get_services.json()[7]["online"]) == "True":
        service_7_status = ":green_circle:"
    else:
        service_7_status = ":red_circle:"

    ms_convert_7 = status_api_get_services.json()[7]["avg_response"] / 1000
    embed.add_field(name=str(status_api_get_services.json()[7]["name"]) + " (" + str(ms_convert_7) + "ms) " + str(
        service_7_status), value="Operating at " + str(status_api_get_services.json()[7]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

    embed.set_thumbnail(
        url="https://support.apple.com/library/content/dam/edam/applecare/images/en_US/itunes/itunes-icloud-status-available-for-download-icon.png")
    await message.send(embed=embed)


@bot.command()
async def media(message):
    download_dir = "/home/data/downloads"
    tv_dir = "/home/data/tv"
    movie_dir = "/home/data/movies"
    music_dir = "/home/data/music"

    download_size = subprocess.check_output(
        ['du', '-s', download_dir]).split()[0].decode('utf-8')
    download_size_proper = int(download_size) * 1020

    tv_size = subprocess.check_output(
        ['du', '-s', tv_dir]).split()[0].decode('utf-8')
    tv_size_proper = int(tv_size) * 1020

    movie_size = subprocess.check_output(
        ['du', '-s', movie_dir]).split()[0].decode('utf-8')
    movie_size_proper = int(movie_size) * 1020

    music_size = subprocess.check_output(
        ['du', '-s', music_dir]).split()[0].decode('utf-8')
    music_size_proper = int(music_size) * 1020

    total_storage = download_size_proper + tv_size_proper + \
        movie_size_proper + music_size_proper

    embed = discord.Embed(title="Storage and download information")
    embed.set_author(name="Shitbox Media Control Bot")
    embed.set_thumbnail(
        url="https://www.nicepng.com/png/full/502-5024580_business-data-storage-icon.png")
    embed.add_field(name="Downloads", value=str(
        size(download_size_proper, system=alternative)), inline=False)
    embed.add_field(name="TV shows", value=str(
        size(tv_size_proper, system=alternative)), inline=False)
    embed.add_field(name="Movies", value=str(
        size(movie_size_proper, system=alternative)), inline=False)
    embed.add_field(name="Music", value=str(
        size(music_size_proper, system=alternative)), inline=False)
    embed.add_field(name="Summary", value="```Server is currently using " + str(size(total_storage, system=alternative)) +
                    " out of 35 TB (" + size(35000000000000 - total_storage, system=alternative) + " left)```", inline=False)
    await message.send(embed=embed)


@bot.command()
async def queue(message):

    print(public_qbit.torrents_info(status_filter="downloading"))

    dStr = ''
    downloadStr = public_qbit.torrents_info(status_filter='downloading')
    print(downloadStr)

    if (not downloadStr):
        dStr += 'There is nothing being downloaded.'
    for j in range(len(downloadStr)):
        dStr += "|" + (downloadStr[j]['content_path'])[10:] + '\n' + "|" + '\n'
        dStr += "|" + 'Progress: '
        dStr += "%" + str((downloadStr[j]['progress'])) + '\n' + '\n'

    embed = discord.Embed(title="Torrent info")
    embed.set_author(name="Shitbox Media Control Bot")
    embed.add_field(name="Queue", value="```" + dStr + "```", inline=False)
    await message.send(embed=embed)


@bot.command()
async def testy(message):
    dStr = ''
    downloadStr = public_qbit.torrents_info(status_filter='downloading')
    print(downloadStr)

    dStr += '```DOWNLOADING:\n'
    if (not downloadStr):
        dStr += 'None.'
    for j in range(len(downloadStr)):
        dStr += 'Location and Name:\t'
        dStr += (downloadStr[j]['content_path']) + '\n'
        dStr += 'Progress Decimal Percent:\t'
        dStr += str((downloadStr[j]['progress'])) + '\n'
    dStr += '```'
    await message.channel.send(dStr)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Keep this if you want to restrict the bot to #bot-commands only
    # if message.channel.id == 889177222764703865:
    #     await bot.process_commands(message)

    # Not sure if it works
    if config["moderation"]["nude_detection"] is True:
        if (message.channel.nsfw is not True) and (len(message.attachments) > 0):
            for i in message.attachments:
                if i.filename.endswith((".png", ".jpg", ".jpeg")):
                    async with aiohttp.ClientSession() as session:
                        async with session.get(i.url) as response:
                            image_bytes = await response.read()
                    image_bytes = BytesIO(image_bytes)
                    n = Nude(image_bytes)
                    n.parse()
                    if n.result is True:
                        i.filename = f"SPOILER_{i.filename}"
                        spoiler = await i.to_file()
                        await message.delete()
                        await message.channel.send(f"Do not send nude images to this channel!")


bot.run(config["discord_token"])
