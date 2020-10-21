import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.command(name='getvotes')
async def getVotes(ctx):
    mems = discord.utils.get(ctx.guild.channels, id=759489613260783670)
    print(mems.members)

bot.run(TOKEN)