import discord
from discord.ext import commands

class Example(commands.Cog): 
    """Some commands you can use to test if the bot is working."""

    def __init__(self, client):

        self.client = client
        
        # Remove this after you clone this cog for use. vvv
    def check_owner(ctx):
    	return ctx.author.id == 604609864681127956 or ctx.author.id == 60263568446062592
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is Online.")
    	
    @commands.command()
    # Remove the @commands.check(check_owner) after cloning.
    @commands.check(check_owner)
    async def testping(self, ctx):
      "Example."
      await ctx.reply("pong!")

def setup(client):
    client.add_cog(Example(client))