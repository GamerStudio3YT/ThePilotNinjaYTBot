import discord
import asyncio
import requests
import aiohttp
from discord.ext import commands

bot = commands.Bot(command_prefix = "/")
bot.remove_command("help")
WELCOME_CHANNEL_ID = 730532155742093342
LEAVE_CHANNEL_ID = 730542434265595984

#token reader
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

#bot start and status
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("!help"))
    print("Logged in as {0.user}".format(bot))

#Welcome Command
async def on_member_join(member):
    if not member.bot:
        welcomechannel = discord.utils.get(member.guild.channels, id=WELCOME_CHANNEL_ID)
        await welcomechannel.send(f"{member.mention} has joined the server. Thank you for joining the server. I hope you have a great time in my server!")
        print(f"{member} has joined the Offical Server of TPN server.")
        embed = discord.Embed(
            title="Welcome to Offical Server of TPN",
            description="""Hi There. Welcome to Offical Server of TPN. Thank you for joining my server. Don't forget to read the rules and keep the server active. If you have any complains then dm the owner of the server. Have fun in my server!""", color=0x22a7f0)

        if not member.dm_channel:
            await member.create_dm()
            await member.dm_channel.send(embed=embed)

#Leave Command
@bot.event
async def on_member_remove(member):
    leavechannel = discord.utils.get(member.guild.channels, id=LEAVE_CHANNEL_ID)
    await leavechannel.send(f"{member.mention} has left the server. We hope you will come back again :(")
    print(f"{member} has left the Offical Server of TPN server")

#help command
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Gamerz Command Lists",
        description="""
        This bot prefix is /
        /help | This command will show you the this
        /clear | This command will clear the messages (you should have manage messages permission to use this command)
        /ping | This command will ping the bot and show the ms statistic""", inline=false, color=0x22a7f0)
    await ctx.send(embed=embed)

#ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

#clear command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, count = 3):
    await ctx.channel.purge(limit=count, check=is_not_pinned)
    await ctx.channel.send(f'{count} message(s) has been cleared')

#token and run
token = read_token()
bot.run(token)