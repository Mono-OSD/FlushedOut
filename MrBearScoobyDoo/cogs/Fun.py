import discord
from discord.ext import commands
import random
import requests
import asyncio


class Fun(commands.Cog):
    """Gives you some fun commands so that you won't be bored all day."""
    def __init__(self, client):

        self.client = client
    
    @commands.command()
    async def hello(ctx, member : discord.Member):
        "Says hello to a member you specify!"
        await ctx.send(f"{ctx.author.mention} says hello to {member.mention}!")

    @commands.command(aliases=['uwu'])
    async def owo(self, ctx):
        "This send uwu?"
        await ctx.reply("UwU!")

    @commands.command(aliases=['boom', 'explosion'])
    async def explode(self, ctx, member : discord.Member):
        "BOOM!"
        embed = discord.Embed(title="A nuke has been dropped..", description=f":boom: {member} JUST DIED", colour=(0x36393e))
        
        await ctx.send(embed=embed)

    @commands.command(aliases=['amongus', 'sus', 'sussy'])
    async def amogus(self, ctx, member: discord.Member):
    	await ctx.send(f"{member} is a sussy imposter :smirk:")

    @commands.command(aliases=['8ball', '8', 'eight'])
    async def eightball(self, ctx, query):
        "8ball time!"
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
        await ctx.reply(f"The answer to your query is: {response}")

    @commands.command(aliases=['flipcoin', 'flip'])
    async def coinflip(self, ctx):
        "Flip a coin!"
        responses = ["tails!", "heads!"]
        response = random.choice(responses)
        await ctx.reply(f"The coin flipped on {response}")
        
    # Bugged
    @commands.command(aliases=['random'])
    async def rng(ctx, startingNumber: int, endingNumber : int):
    	if int(endingnumber) > int(startingnumber):
    		await ctx.reply(random.randint(int(startingnumber), int(endingnumber)))
    	
    	else:
    		embed = discord.Embed(title="Uh oh!", description="Your first number was higher than your second number, try again!", colour=(0x36393e))
    		
    		await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
