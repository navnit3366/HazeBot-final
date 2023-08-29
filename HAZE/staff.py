import discord
from discord import Member
from discord.ext import commands
from hazebot import banned_users, botbanned_msg

HAZE = 740584420645535775
HEAD_OFFICER_ID = 762318708596015114
SENIOR_OFFICER_ID = 819210576164028416
OFFICER_ID = 783205193432301578
LEARNER_OFFICER_ID = 795339482693369907

class staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(aliases=['pr'])
    @commands.is_owner()
    async def partner_revoke(self, ctx, member : discord.Member, message):
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:        
            if ctx.guild.id==HAZE:  
                revoked = discord.Embed(title='Partnership Revoked', description='Your Partnership with HAZE has been revoked')
                revoked.add_field(name='Reason', value=message, inline=False)
                await member.send(embed=revoked)

        
            try:
                await ctx.send(f'Message sent to {member}')

            except discord.Forbidden:
                await ctx.send("Message couldn't be sent")
      

    @commands.command()
    @commands.is_owner()
    async def hire(self, ctx, member: Member):
        LEARNER_OFFICER=await ctx.guild.get_role(LEARNER_OFFICER_ID) 
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:            
            if ctx.guild.id==HAZE:      
                hire = discord.Embed(title='You are hired!',
                                        description=f"Congrats, {member},\n\nYour application has been approved and you have been hired as an Offier of HAZE. You will begin as a Learner Officer which has limited permissions and you won't be able to ban anyone until there is a need to promote you.\n\nIf you have any questions, don't be afraid to ask us and we will be happy to answer it.\n\nThank You")
                await member.add_roles(LEARNER_OFFICER)
                await member.send(embed=hire)

                try:
                    await ctx.send(f'Message sent to {member}')

                except discord.Forbidden:
                    await ctx.send("Message couldn't be sent")

    @commands.command()
    @commands.has_role(HEAD_OFFICER_ID)
    async def fire(self, ctx, member: discord.Member, message):
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:          
            if ctx.guild.id==HAZE:      
                fire = discord.Embed(title='You are **fired!**', color=0xff0000)
                fire.add_field(name="Reason", value=message, inline=False)
                fire.add_field(name="Fired by", value=ctx.author, inline=False)
                await member.send(embed=fire)

                try:
                    await ctx.send(f'Message sent to {member}')

                except discord.Forbidden:
                    await ctx.send("Message couldn't be sent")

    @commands.command()
    @commands.has_role(HEAD_OFFICER_ID)
    async def suspend(self, ctx, member: discord.Member, message):
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:          
            if ctx.guild.id==HAZE:      
                suspend = discord.Embed(title='You are **suspended!**', color=0xff0000)
                suspend.add_field(name="Reason", value=message, inline=False)
                suspend.add_field(name="Suspended by", value=ctx.author, inline=False)
                await member.send(embed=suspend)

                try:
                    await ctx.send(f'Message sent to {member}')

                except discord.Forbidden:
                    await ctx.send("Message couldn't be sent")
                                   
    @commands.command()
    @commands.is_owner()
    async def promote(self, ctx, member: discord.Member):
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:          
            if ctx.guild.id==HAZE:      
                promote = discord.Embed(title="You've been promoted!",
                                    description=f"Hi, {member},\n\nWe have decided to promote you from Learner Officer to Officer since we have a reason to give you full moderation permissions")
                await member.send(embed=promote)

                try:
                    await ctx.send(f'Message sent to {member}')

                except discord.Forbidden:
                    await ctx.send("Message couldn't be sent")

    @commands.command()
    @commands.is_owner()
    async def promoteup(self, ctx, member: discord.Member):
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:          
            if ctx.guild.id==HAZE:      
                promoteup = discord.Embed(title="You've been promoted!",
                                        description=f"Hi, {member},\n\nWe have decided to promote you from Officer to Senior Officer. That means you have a status higher that the Officers and you are also in charge of them but don't get too excited as Head Officers are still in charge of you")
                await member.send(embed=promoteup)

                try:
                    await ctx.send(f'Message sent to {member}')

                except discord.Forbidden:
                    await ctx.send("Message couldn't be sent")


    @commands.command()
    @commands.has_role(HEAD_OFFICER_ID)
    async def dm(self, ctx, users: commands.Greedy[discord.User], *, message):
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:  
            for user in users:
                try:
                    await user.send(message)
                    await ctx.send('Message sent')
                except:
                    await ctx.send(f"Failed to send message to {user.id}")

def setup(bot):
    bot.add_cog(staff(bot))
