import discord
from discord.ext import commands
import os
import json
from keep_alive import keep_alive


def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
    
    
  return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix, status=discord.Status.dnd,activity=discord.Game("Used for testing and run 24/7!"))

@bot.event
async def on_guild_join(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
    
    prefixes[str(guild.id)] = 's.'
  
  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))
    
  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)

@bot.event
async def on_start():
  print('Woah! It\'s ready!')

@bot.command()
async def setprefix(ctx, prefix):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)
    
    
  prefixes[str(ctx.guild.id)] = prefix
  
  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)
  await ctx.send('Prefix set to your desired prefix!')
  

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! You have {round(bot.latency * 1000)} ms')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Successfully banned the naughty {member.mention}!')

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')
  
  for ban_entry in banned_users:
    user = ban_entry.user
    
    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Successfully unbanned {user.name}#{user.discriminator}!')

@bot.command()
async def owo(ctx):
    await ctx.send('OwO')

@bot.command()
async def info(ctx):
    await ctx.send('Hey there! I\'m :flushed: and I am a bot made by Dabido201 and this is also a testing bot. The only commands you can use right now are `s.ping`, `s.owo` and this command, `s.info`. For mod commands, run `s!modinfo`!')

@bot.command()
async def modinfo(ctx):
    await ctx.send('You must be looking for the moderation commands, right? Well, you\'re in for a treat! Some mod commands you can use are `s.kick`, `s.clear`,`s.ban` and `s.unban`!')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

keep_alive()
bot.run(os.environ['token'])
