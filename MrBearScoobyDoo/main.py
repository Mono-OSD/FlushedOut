# BEFORE LOOKING AROUND, GO TO README.MD
import discord
from discord.ext import commands
import os
import json
from pretty_help import DefaultMenu, PrettyHelp
from keep_alive import keep_alive
	
def check_owner(ctx):
	return ctx.author.id == 604609864681127956 or ctx.author.id == 60263568446062592
		
def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

client = commands.Bot(command_prefix="flu!", status=discord.Status.idle,activity=discord.Game("Type 'flu!help' for help! || beta-v0.9.2"), help_command=PrettyHelp())

menu = DefaultMenu('⬅️', '➡️', '❌') 
client.help_command = PrettyHelp(navigation=menu, no_category="DevTools", active_time="120s", remove="❌", show_index=True, color=discord.Colour.gold())

#Events/Utility
@client.event
async def on_command_error(msg, error):
	if isinstance(error, commands.CheckFailure):
		await msg.channel.send("You don't have permission to run this command. You're not the *leader*.")
		
@client.event
async def on_start():
  print('Bot is online')

@client.command()
@commands.check(check_owner)
async def botenable(ctx, extension):
		"Enables categories/cogs for the entire bot."
		client.load_extension(f"cogs.{extension}")
		await ctx.send(f"Enabled: {extension}")

@client.command()
@commands.check(check_owner)
async def botdisable(ctx, extension):
		"Disables categories/cogs for the entire bot."
		client.unload_extension(f"cogs.{extension}")
		await ctx.send(f"Disabled: {extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
	if message.author == client.user:
		return
    
	if message.content.startswith("<@882057940834582588>"):
		await message.channel.send("My prefix is `flu!` For some commands, run `flu!help`.")

keep_alive()
client.run(os.environ['token'])
