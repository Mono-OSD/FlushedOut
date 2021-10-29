import discord
from discord.ext import commands, tasks
import os
import json
from pretty_help import DefaultMenu, PrettyHelp
from discord_slash import SlashCommand
import random
from random import choice
#from keep_alive import keep_alive
	
def check_owner(ctx):
	return ctx.author.id == 604609864681127956 or ctx.author.id == 60263568446062592

client = commands.Bot(command_prefix="s.", status=discord.Status.idle, activity=discord.Game("Im so bored"), help_command=PrettyHelp())

menu = DefaultMenu('⬅️', '➡️', '❌') 
client.help_command = PrettyHelp(navigation=menu, no_category="DevTools", active_time="120s", remove="❌", show_index=True, color=discord.Colour.gold())

# On Ready
@client.event
async def on_start():
	print('Bot is online')

# Events/Utility
@client.event
async def on_command_error(msg, error):
	if isinstance(error, commands.CheckFailure):
		await msg.channel.send("You don't have permission to run this command. You're not the *leader*.")
		
@client.command()
@commands.check(check_owner)
async def botenable(ctx, extension):
		"Enables categories/cogs for the entire bot."
		client.load_extension(f"cogs.{extension}")
		await ctx.reply(f"Hey dev, I just used the switch and enabled: {extension}")


@client.command()
@commands.check(check_owner)
async def botdisable(ctx, extension):
		"Disables categories/cogs for the entire bot."
		client.unload_extension(f"cogs.{extension}")
		await ctx.reply(f"Hey dev, I just used the switch and disabled: {extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
	if message.author == client.user:
		return
    
	if message.content.startswith("<@882057940834582588>"):
		embed = discord.Embed(title="Hello!", description="For starters, **my prefix is flu!**. Second of all, use **flu!botinfo** for some info on me and **flu!help** for some commands! Thanks!", colour=(0x36393e))
		
		await message.channel.send(embed=embed)

#keep_alive()
client.run(os.environ['token'])
