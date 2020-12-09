import os
import discord
from bot.discordrssbot import DiscordRssBot

intents = discord.Intents.default()
intents.members = False

description = "Discord RSS Client"

client = DiscordRssBot(
    command_prefix='!', description=description, intents=intents)

client.run(os.getenv("DISCORD_TOKEN"))