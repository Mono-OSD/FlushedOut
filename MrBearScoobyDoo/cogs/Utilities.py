import discord
from discord.ext import commands

class Utilities(commands.Cog): 
    """Some utility commands to provide information about stuff."""
    def __init__(self, client):

        self.client = client
        
    @commands.command(aliases=['book'])
    async def botinfo(self, ctx):
      "Sends some info about the bot."
      embed = discord.Embed(title="Info", description="Hello! I'm Flushed, I am a multi-purpose bot that includes moderation, fun commands and more coming soon! I'm still a WIP project so please do not rely on me. Here's some more info about me.\n\n<:slash_command_normal:885853559021793280> As of 12th of September, slash commands will run alongside normal commands. On February 2022, we will move to slash commands fully to prepare for the April 2022 move for slash commands.", colour=(0xFFD700))
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877503406456062032/883118110977167360/image0.jpg")
      embed.add_field(name="Created on", value="2021-9-1 (September 1, 2021 AEST)", inline=True)
      embed.add_field(name="Developers", value="Winter78#8711, Neritox#4417", inline=True)
      embed.add_field(name="Planned release date", value="In 3-5 business days", inline=True)
      embed.add_field(name="Release date", value="Partially released", inline=True)
      embed.add_field(name="How many bots are there available?", value="2 bots, one for testing, one is stable (this)", inline=True)
      
      await ctx.reply(embed=embed)

    @commands.command(aliases=['accuratems', 'exactlatency'])
    async def ping(self, ctx):
      "Checks your .ms latency!"
      await ctx.reply(f"Pong! {round(self.client.latency * 1000)} ms!")
      
    @commands.command(aliases=['latency', 'ms'])
    async def pong(self, ctx):
      "Checks your .ms latency in very accurate numbers!"
      await ctx.reply(f"Ping! {self.client.latency * 1000} ms!")
      
    @commands.command(aliases=['inviteme'])
    async def invite(self, ctx):
      "Sends the invite link for the both (oAuth link)."
      await ctx.reply("Here is my invite link: https://discord.com/api/oauth2/authorize?client_id=882057940834582588&permissions=260113181814&scope=bot%20applications.commands")
      
    @commands.command()
    async def userinfo(self, ctx, member : discord.Member=None):
    	"Sends info about a specific user."
    
    	if member == None:
    		embed = discord.Embed(title=f"User info about {ctx.author}!", description=f"Here is some info about this user in {ctx.message.guild.name}!", colour=(0xFFD700))
    		embed.set_thumbnail(url=ctx.author.avatar_url)
    		embed.add_field(name="Name", value=f"{ctx.author.mention}", inline=True)
    		embed.add_field(name="Nickname", value=f"{ctx.author.nick}", inline=True)
    		embed.add_field(name="ID", value=f"{ctx.author.id}", inline=True)
    		embed.add_field(name="Joined on", value=f"{ctx.author.created_at}", inline=True)
    		embed.add_field(name="Note", value="The date you joined is in 24 hour time and american format, example: 2017-07-10 instead of 2017-10-07", inline=True)
    		await ctx.reply(embed=embed)
    
    	else:
    		embed = discord.Embed(title=f"User info about {member}!", description=f"Here is some info about this user in {ctx.message.guild.name}!", colour=(0xFFD700))
    		embed.set_thumbnail(url=member.avatar_url)
    		embed.add_field(name="Name", value=member.mention, inline=True)
    		embed.add_field(name="Nickname", value=member.nick, inline=True)
    		embed.add_field(name="ID", value=member.id, inline=True)
    		embed.add_field(name="Joined on", value=member.created_at, inline=True)
    		embed.add_field(name="Note", value="The date you joined is in 24 hour time and american format, example: 2017-07-10 instead of 2017-10-07", inline=True)
    		await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Utilities(client))