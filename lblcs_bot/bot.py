import logging
from discord.ext import commands, tasks
import models
from cogs.scraper import Scraper
from cogs.tournaments import Tournament


class Bot(commands.Bot):
    def __init__(self,guild_id,intents):
        super().__init__('$',intents=intents)
        self.guild_id = guild_id

    async def on_ready(self):
        logging.info(f'Logged in as {self.user} GUILD_ID: {self.guild_id}')
        # guild = self.get_guild(self.guild_id)
        # print(f'{guild}')
        # members = guild.members
        # for member in members:
        #     print(f'{member.roles}')
        logging.info("Syncing application commands...")
        await self.tree.sync(guild=self.get_guild(self.guild_id))

    async def setup_hook(self):
        logging.info('Loading cogs...')
        await self.add_cog(Tournament(self))
        await self.add_cog(Scraper(self))
