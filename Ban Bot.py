import discord.ext
from discord.ext import commands
import asyncio

prefix = ";"
#You can change the Prefix!

client=commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
	print('Bot is ready to Ban!')
	print('--------------------------')
	print('Bot by EC2★Darky#9770')
	print('-------------------------------')

client.remove_command("help")
	
@client.command(aliases=["Ban"])
async def ban(ctx):
	for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has failed to be banned from {ctx.guild.name}")
	
client.run("BOT TOKEN")
#Enter your Bot Token!
