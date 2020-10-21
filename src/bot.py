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

# build a string then return it of the voters
def buildVoteString(name, members):
    message = "**Votes for {name} - {voteNum}**".format(name=name, voteNum=len(members))
    for member in members:
        message += ("\n")
        message += member.display_name
    return message

@bot.command(name='getvotes')
async def getVotes(ctx):
    # troy for president
    pres = discord.utils.get(ctx.guild.roles, id=768136870537986098).members
    await ctx.send(buildVoteString("Troy Lafond for President", pres))
    vp = discord.utils.get(ctx.guild.roles, id=768136907116511303).members
    await ctx.send(buildVoteString("Zachary Recine for Vice President", vp))
    treasurer = discord.utils.get(ctx.guild.roles, id=768136954251706389).members
    await ctx.send(buildVoteString("Anthony Millsci for Treasurer", treasurer))
    sec1 = discord.utils.get(ctx.guild.roles, id=768136996664639498).members
    await ctx.send(buildVoteString("Pierre Demers for Secretary", sec1))
    sec2 = discord.utils.get(ctx.guild.roles, id=768137052809723906).members
    await ctx.send(buildVoteString("Sasha Wilkinson for Secretary", sec2))
    poli = discord.utils.get(ctx.guild.roles, id=768137090327379968).members
    await ctx.send(buildVoteString("Neyder Fernández for Political Outreach Director", poli))



bot.run(TOKEN)