import discord
from discord.ext import commands
import requests
from qbittorrentapi import Client, client
from qbittorrentapi import TorrentStates
from main import config
from variables import public_qbit, private_qbit


class Service(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command()
    async def status(self, message):
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

        if str(status_api_get_services.json()[8]["online"]) == "True":
            service_8_status = ":green_circle:"
        else:
            service_8_status = ":red_circle:"

        ms_convert_8 = status_api_get_services.json()[8]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services.json()[8]["name"]) + " (" + str(ms_convert_8) + "ms) " + str(
            service_8_status), value="Operating at " + str(status_api_get_services.json()[8]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services.json()[9]["online"]) == "True":
            service_9_status = ":green_circle:"
        else:
            service_9_status = ":red_circle:"

        ms_convert_9 = status_api_get_services.json()[9]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services.json()[9]["name"]) + " (" + str(ms_convert_9) + "ms) " + str(
            service_9_status), value="Operating at " + str(status_api_get_services.json()[9]["online_7_days"]) + "% uptime in the last 7 days", inline=False)


        if str(status_api_get_services.json()[10]["online"]) == "True":
            service_10_status = ":green_circle:"
        else:
            service_10_status = ":red_circle:"

        ms_convert_10 = status_api_get_services.json()[10]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services.json()[10]["name"]) + " (" + str(ms_convert_10) + "ms) " + str(
            service_10_status), value="Operating at " + str(status_api_get_services.json()[10]["online_7_days"]) + "% uptime in the last 7 days", inline=False)



        embed.set_thumbnail(
            url="https://support.apple.com/library/content/dam/edam/applecare/images/en_US/itunes/itunes-icloud-status-available-for-download-icon.png")
        await message.send(embed=embed)
        


    @commands.command()
    async def queue(self, message):
        dStr = ''
        downloadStr = public_qbit.torrents_info(status_filter='downloading')
        print(downloadStr)

        if (not downloadStr):
            dStr += 'There is nothing being downloaded.'
        for j in range(len(downloadStr)):
            dStr += (downloadStr[j]['content_path'])[10:] + '\n'
            dStr += 'Progress: '
            dStr += "%" + str((downloadStr[j]['progress'])) + '\n' + '\n'

        embed = discord.Embed(title="Torrent info")
        embed.set_author(name="Shitbox Media Control Bot")
        embed.add_field(name="Queue", value="```" + dStr[:5500] + "```", inline=False)
        await message.send(embed=embed)


def setup(client):
    client.add_cog(Service(client))