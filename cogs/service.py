import discord
import requests
from discord.ext import commands
from utils.db import config
from utils.vars import QbitVars


class Service(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def status(self, message):
        status_api_get_services = requests.get(
            "http://status.shitbox.media/api/services?api=" + config["status_api_key"]).json()

        embed = discord.Embed(title="Status for shitbox.media")
        embed.set_author(name=f"{self.client.user.name}",
                         icon_url=f"{self.client.user.avatar_url}")

        if str(status_api_get_services[1]["online"]) == "True":
            service_1_status = ":green_circle:"
        else:
            service_1_status = ":red_circle:"

        ms_convert_1 = status_api_get_services[1]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[1]["name"]) + " (" + str(ms_convert_1) + " ms) " + str(
            service_1_status), value="Operating at " + str(status_api_get_services[1]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services[2]["online"]) == "True":
            service_2_status = ":green_circle:"
        else:
            service_2_status = ":red_circle:"

        ms_convert_2 = status_api_get_services[2]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[2]["name"]) + " (" + str(ms_convert_2) + " ms) " + str(
            service_2_status), value="Operating at " + str(status_api_get_services[2]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services[3]["online"]) == "True":
            service_3_status = ":green_circle:"
        else:
            service_3_status = ":red_circle:"

        ms_convert_3 = status_api_get_services[3]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[3]["name"]) + " (" + str(ms_convert_3) + " ms) " + str(
            service_3_status), value="Operating at " + str(status_api_get_services[3]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services[4]["online"]) == "True":
            service_4_status = ":green_circle:"
        else:
            service_4_status = ":red_circle:"

        ms_convert_4 = status_api_get_services[4]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[4]["name"]) + " (" + str(ms_convert_4) + " ms) " + str(
            service_4_status), value="Operating at " + str(status_api_get_services[4]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services[5]["online"]) == "True":
            service_5_status = ":green_circle:"
        else:
            service_5_status = ":red_circle:"

        ms_convert_5 = status_api_get_services[5]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[5]["name"]) + " (" + str(ms_convert_5) + " ms) " + str(
            service_5_status), value="Operating at " + str(status_api_get_services[5]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services[6]["online"]) == "True":
            service_6_status = ":green_circle:"
        else:
            service_6_status = ":red_circle:"

        ms_convert_6 = status_api_get_services[6]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[6]["name"]) + " (" + str(ms_convert_6) + " ms) " + str(
            service_6_status), value="Operating at " + str(status_api_get_services[6]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services[7]["online"]) == "True":
            service_7_status = ":green_circle:"
        else:
            service_7_status = ":red_circle:"

        ms_convert_7 = status_api_get_services[7]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[7]["name"]) + " (" + str(ms_convert_7) + "ms) " + str(
            service_7_status), value="Operating at " + str(status_api_get_services[7]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services[8]["online"]) == "True":
            service_8_status = ":green_circle:"
        else:
            service_8_status = ":red_circle:"

        ms_convert_8 = status_api_get_services[8]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[8]["name"]) + " (" + str(ms_convert_8) + "ms) " + str(
            service_8_status), value="Operating at " + str(status_api_get_services[8]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services[9]["online"]) == "True":
            service_9_status = ":green_circle:"
        else:
            service_9_status = ":red_circle:"

        ms_convert_9 = status_api_get_services[9]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[9]["name"]) + " (" + str(ms_convert_9) + "ms) " + str(
            service_9_status), value="Operating at " + str(status_api_get_services[9]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        if str(status_api_get_services[10]["online"]) == "True":
            service_10_status = ":green_circle:"
        else:
            service_10_status = ":red_circle:"

        ms_convert_10 = status_api_get_services[
            10]["avg_response"] / 1000
        embed.add_field(name=str(status_api_get_services[10]["name"]) + " (" + str(ms_convert_10) + "ms) " + str(
            service_10_status), value="Operating at " + str(status_api_get_services[10]["online_7_days"]) + "% uptime in the last 7 days", inline=False)

        embed.set_thumbnail(
            url="https://support.apple.com/library/content/dam/edam/applecare/images/en_US/itunes/itunes-icloud-status-available-for-download-icon.png")

        await message.send(embed=embed)

    @commands.command()
    async def queue(self, message):
        dStr = ''
        downloadStr = QbitVars.public_qbit.torrents_info(
            status_filter='downloading')
        print(downloadStr)

        if (not downloadStr):
            dStr += 'There is nothing being downloaded.'
        for j in range(len(downloadStr)):
            dStr += (downloadStr[j]['content_path'])[10:] + '\n'
            dStr += 'Progress: '
            dStr += "%" + str((downloadStr[j]['progress'])) + '\n' + '\n'

        embed = discord.Embed(title="Torrent queue",
                              description="```" + dStr[:4080] + "```")
        embed.set_author(name=f"{self.client.user.name}",
                         icon_url=f"{self.client.user.avatar_url}")
        await message.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Service(client))
