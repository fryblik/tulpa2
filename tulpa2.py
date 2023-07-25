#!/usr/bin/env python3
import platform
import sys

import nextcord
from nextcord.ext.commands import Bot

from utils.config_loader import get_config, get_bot_token, ConfigLoadError
from utils.logger import logger

intents = nextcord.Intents.all()
bot = Bot(command_prefix=".", description="Jackie Chan Tulpa", intents=intents)
try:
    bot.config = get_config()
    bot.logger = logger
except ConfigLoadError as e:
    print(e)
    sys.exit(1)


@bot.event
async def on_ready():
    print(
        f"Nick: {bot.user} | ID: {str(bot.user.id)} | Guild count: "
        f"{str(len(bot.guilds))}"
    )
    print(
        f"Running nextcord {nextcord.__version__} and Python "
        f"{platform.python_version()}."
    )
    print(
        f"Invite link: https://discord.com/oauth2/authorize?client_id={bot.user.id}"
        "&scope=bot&permissions=469888064"
    )
    bot.logger.info("Connected.")


bot.logger.debug("Running the bot.")
bot.run(get_bot_token())
