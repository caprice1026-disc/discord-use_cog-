from discord.ext import commands
import my_cog
import os
import discord
import maincog
import web3cog
import foranoncog

BOT_TOKEN = os.getenv("BOT_TOKEN")
all = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=all, help_command=None)
#road cogs
bot.load_extension('my_cog')
bot.load_extension('maincog')
bot.load_extension('web3cog')
bot.load_extension('foranoncog')

async def on_ready():
    await bot.change_presence(activity=discord.Game(name="/helpでヘルプを表示"))

bot.run(BOT_TOKEN)
