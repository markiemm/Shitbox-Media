import os
import subprocess

import discord
from discord.ext import commands
from hurry.filesize import alternative
from hurry.filesize.filesize import size
from utils.vars import Dirs


class Server(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    # results[0]  -->  download_dir
    # results[1]  -->  tv_dir
    # results[2]  -->  movie_dir
    # results[3]  -->  music_dir
    # results[4]  -->  books_dir

    @commands.command()
    async def media(self, message):
        all_dirs = (Dirs.download_dir, Dirs.tv_dir,
                    Dirs.movie_dir, Dirs.music_dir,
                    Dirs.books_dir)

        results = []
        for dir in all_dirs:
            temp1 = subprocess.check_output(
                ['du', '-s', dir]).split()[0].decode('utf-8')
            results.append(int(temp1) * 1020)

        total_storage = 0
        for result in results:
            total_storage += int(result)

        embed = discord.Embed(title="Storage and download information")
        embed.set_author(name="Shitbox Media Control Bot")
        embed.set_thumbnail(
            url="https://www.nicepng.com/png/full/502-5024580_business-data-storage-icon.png")
        embed.add_field(name="Downloads (" + str(len(os.listdir(Dirs.download_dir))) + " downloads)", value=str(
            size(results[0], system=alternative)), inline=False)
        embed.add_field(name="TV shows (" + str(len(os.listdir(Dirs.tv_dir))) + " TV shows)", value=str(
            size(results[1], system=alternative)), inline=False)
        embed.add_field(name="Movies (" + str(len(os.listdir(Dirs.movie_dir))) + " movies)", value=str(
            size(results[2], system=alternative)), inline=False)
        embed.add_field(name="Music (" + str(len(os.listdir(Dirs.music_dir))) + " albums)", value=str(
            size(results[3], system=alternative)), inline=False)
        embed.add_field(name="Books (" + str(len(os.listdir(Dirs.books_dir + "/Books"))) + " books)", value=str(
            size(results[4], system=alternative)), inline=False)
        embed.add_field(name="Summary", value="```Server is currently using " + str(size(total_storage, system=alternative)) +
                        f" out of 35 TB (" + size(35000000000000 - total_storage, system=alternative) + " left)```", inline=False)
        await message.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Server(client))
