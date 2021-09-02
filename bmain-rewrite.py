import discord
from discord.ext import commands
import os
import json
from pretty_help import DefaultMenu, PrettyHelp
from discord_slash import SlashCommand
import random
#from keep_alive import keep_alive
	
def check_owner(ctx):
	return ctx.author.id == 604609864681127956 or ctx.author.id == 60263568446062592
		

def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

client = commands.Bot(command_prefix="s.", status=discord.Status.idle,activity=discord.Game("Used and tested 24/7!"), help_command=PrettyHelp())

menu = DefaultMenu('◀️', '▶️', '❌') 
client.help_command = PrettyHelp(navigation=menu, no_category="Not Categorised // Utility", active_time="120s", remove="❌", show_index=True, color=discord.Colour.gold())

slash = SlashCommand(client, sync_commands=True)

#SlashCommands
@slash.slash(name="SlashTest", description="A slash command test.", guild_ids=[882129837228175430])
async def slashtest(ctx):
    await ctx.send("This is a slash command! (more coming soon)")
    
@slash.slash(name="OwO", description="OwO?", guild_ids=[882129837228175430])
async def _owo(ctx):
    await ctx.send("UwU!")
    
@slash.slash(name="FIRE", description="BURN BABY BURN", guild_ids=[882129837228175430])
async def _burn(ctx):
    await ctx.send(":fire:")
    
@slash.slash(name="Explosion", description="Boom, gone.", guild_ids=[882129837228175430])
async def _explode(ctx):
    await ctx.send(f":boom: {ctx.author} JUST DIED!")

@slash.slash(name="sus", description="sussy imposter..", guild_ids=[882129837228175430])
async def _sussy(ctx):
    await ctx.send(f"{ctx.author} is a sussy imposter :smirk:")

@slash.slash(name="8ball", description="Elaborate your query and the eightball will decide.", guild_ids=[882129837228175430])
async def _eightball(ctx, query):
	responses = [
		"As I see it, yes.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don’t count on it.",
        "It is certain.", "It is decidedly so.", "Most likely.",
        "My reply is no.", "My sources say no.", "Outlook not so good.",
        "Outlook good.", "Reply hazy, try again.", "Signs point to yes.",
        "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.",
        "You may rely on it."
        ]
	response = random.choice(responses)
	await ctx.send(f"The answer to your query is: {response}")

#Events/Utility
@client.event
async def on_command_error(msg, error):
	if isinstance(error, commands.CheckFailure):
		await msg.channel.send("You don't have permission to run this command. Most of the time, only developers can do this.")
	if isinstance(error, commands.CommandOnCooldown):
		await msg.channel.send("Calm down, spam isn't cool fam.".format(error.retry_after))

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

#keep_alive()
client.run(os.environ['token'])
