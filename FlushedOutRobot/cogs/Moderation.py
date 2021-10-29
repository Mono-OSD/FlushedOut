import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog): 
    """Some commands to get you moderating for people."""
    def __init__(self, client):

        self.client = client
        
    def moderation_check():
    	async def predicate(ctx):
    		return ctx.guild is not None \
				and ctx.author.guild_permissions.manage_channels \
				and ctx.me.guild_permissions.manage_channels 
    	
    	return commands.check(predicate)

    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason=None,):
        "Kicks the specified user out of our beautiful territory. You didn't skip leg day, did you?"
        await member.kick()
        await member.send(f"You have been kicked from {ctx.message.guild.name} for {reason} (and also for being a bad person, naughty naughty)")
        await ctx.send(f'User {member} has been literally and succesfully kicked out of our territory.')


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, reason="not being a gogy stan", ):
        "Banishes the specified user from our beautiful territory."
        if reason == None:
            await ctx.send(f"... You have to provide a reason {ctx.member}")
        else:
            messageok = f"You have been banished from {ctx.message.guild.name} for {reason} (and also for being a really, and by really I mean REALLY and when I mean REALLY I mean LITERALLY AND I MEAN LITERALLY I MEAN YOU'RE SO BAD THAT YOU GOT BANISHED FROM A LITERAL SERVER)"
            await member.send(messageok)
            await member.ban(reason=reason)
            await ctx.send(f"{member} has been banished from our territory for being a bad person, we've also sent them a death threat so they can remember this day that they got banished for {reason}.")
    

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.Member):
        "Undo your banishment contract with your specified user."
        try:
        	await self.guild.unban(member)
        	await ctx.send(f"Succesfully banned {member}")
        except discord.NotFound:
        	await ctx.send("We couldn't find your specific user or they were never banned.")
        	
        	embed = discord.Embed(title="Uh-oh!", description="We couldn't find the specific member you mentioned or they were never banned.", colour=(0xFFD70))
        	await ctx.send(embed=embed)

    @commands.command(aliases=['purge', 'clean'])
    async def clear(self, ctx, amount=5):
      "Clears some messages"
      await ctx.channel.purge(limit=amount)

    #Timed mute this format: 1d, 20s, 30m, etc..
    @commands.command(aliases=['tempmute'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: commands.MemberConverter=None, time=None, *, reason=None):
        if not member:
            await ctx.send("You must mention a member to mute!")
        elif not time:
            await ctx.send("You must mention a time!")
        else:
            if not reason:
                reason="No reason given"
        #Now timed mute manipulation
        try:
            seconds = time[:-1] #Gets the numbers from the time argument, start to -1
            duration = time[-1] #Gets the timed maniulation, s, m, h, d
            if duration == "s":
                seconds = seconds * 1
            elif duration == "m":
                seconds = seconds * 60
            elif duration == "h":
                seconds = seconds * 60 * 60
            elif duration == "d":
                seconds = seconds * 86400
            else:
                await ctx.send("Invalid duration input")
                return
        except Exception as e:
            print(e)
            await ctx.send("Invalid time input")
            return
        guild = ctx.guild
        Muted = discord.utils.get(guild.roles, name="Muted")
        if not Muted:
            Muted = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(Muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        await member.add_roles(Muted, reason=reason)
        muted_embed = discord.Embed(title="Muted a user", description=f"{member.mention} Was muted by {ctx.author.mention} for {reason} to {time}")
        await ctx.send(embed=muted_embed)
        await asyncio.sleep(seconds)
        await member.remove_roles(Muted)
        unmute_embed = discord.Embed(title="Mute over!", description=f'{ctx.author.mention} muted to {member.mention} for {reason} is over after {time}')
        await ctx.send(embed=unmute_embed)

def setup(client):
    client.add_cog(Moderation(client))  