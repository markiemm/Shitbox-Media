import os
import platform

import discord
from discord.ext import commands


class Listeners(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.client.user}")
        print(f"Discord.py API version: {discord.__version__}")
        print(f"Python version: {platform.python_version()}")
        print(
            f"Running on: {platform.system()} {platform.release()} ({os.name})")
        print("-"*22)
        print("Bot is online")
        await self.client.change_presence(activity=discord.Game("Shitbox"))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        await self.client.process_commands(message)


def setup(client: commands.Bot):
    client.add_cog(Listeners(client))
