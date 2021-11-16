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

    @commands.command()
    async def media(self, message):

        download_size = subprocess.check_output(
            ['du', '-s', Dirs.download_dir]).split()[0].decode('utf-8')
        download_size_proper = int(download_size) * 1020

        tv_size = subprocess.check_output(
            ['du', '-s', Dirs.tv_dir]).split()[0].decode('utf-8')
        tv_size_proper = int(tv_size) * 1020

        movie_size = subprocess.check_output(
            ['du', '-s', Dirs.movie_dir]).split()[0].decode('utf-8')
        movie_size_proper = int(movie_size) * 1020

        music_size = subprocess.check_output(
            ['du', '-s', Dirs.music_dir]).split()[0].decode('utf-8')
        music_size_proper = int(music_size) * 1020

        books_size = subprocess.check_output(
            ['du', '-s', Dirs.books_dir]).split()[0].decode('utf-8')
        books_size_proper = int(books_size) * 1020

        total_storage = download_size_proper + tv_size_proper + \
            movie_size_proper + music_size_proper

        embed = discord.Embed(title="Storage and download information")
        embed.set_author(name="Shitbox Media Control Bot")
        embed.set_thumbnail(
            url="https://www.nicepng.com/png/full/502-5024580_business-data-storage-icon.png")
        embed.add_field(name="Downloads (" + str(len(os.listdir(Dirs.download_dir))) + " downloads)", value=str(
            size(download_size_proper, system=alternative)), inline=False)
        embed.add_field(name="TV shows (" + str(len(os.listdir(Dirs.tv_dir))) + " TV shows)", value=str(
            size(tv_size_proper, system=alternative)), inline=False)
        embed.add_field(name="Movies (" + str(len(os.listdir(Dirs.movie_dir))) + " movies)", value=str(
            size(movie_size_proper, system=alternative)), inline=False)
        embed.add_field(name="Music (" + str(len(os.listdir(Dirs.music_dir))) + " albums)", value=str(
            size(music_size_proper, system=alternative)), inline=False)
        embed.add_field(name="Books (" + str(len(os.listdir(Dirs.books_dir + "/Books"))) + " books)", value=str(
            size(books_size_proper, system=alternative)), inline=False)
        embed.add_field(name="Summary", value="```Server is currently using " + str(size(total_storage, system=alternative)) +
                        f" out of 35 TB (" + size(35000000000000 - total_storage, system=alternative) + " left)```", inline=False)
        await message.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(Server(client))
