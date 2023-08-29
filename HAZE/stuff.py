import discord, sys, os
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.errors import NotOwner

from hazebot import HAZE, LEAVE_CHANNEL_ID, WELCOME_CHANNEL_ID, banned_users, botbanned_msg



def restart_bot():
  os.execv(sys.executable, ['python'] + sys.argv)

class staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:        
            embed = discord.Embed(color=0x236ce1)
            embed.add_field(
                name="Ping", value=f'{round(self.bot.latency * 1000)}ms', inline=False)
            await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == HAZE:
            try:
                channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
                try:
                    embed = discord.Embed(colour=discord.Colour.green())
                    embed.set_author(name=member.name,
                                        icon_url=member.guild.icon_url)
                    embed.add_field(
                                name="Welcome", value=f"**Hey,{member.mention}! Welcome to {member.guild.name}\nI hope you enjoy your stay here and thanks for joining**\n Check our <#770263931334950912> and <#777099012863164417> Before you start chatting here.\n\nNow we have **{len(member.guild.members)}** members", inline=False)
                    embed.set_image(url=member.avatar_url)
                    await channel.send(embed=embed)
                except Exception as e:
                    raise e
            except Exception as e:
                raise e


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == HAZE:
            try:
                channel = self.bot.get_channel(LEAVE_CHANNEL_ID)
                try:
                    embed = discord.Embed(colour=discord.Colour.red())
                    embed.set_author(name=member.name,
                                    icon_url=member.guild.icon_url)
                    embed.add_field(
                        name="Good Bye", value=f"**{member.mention} just left us.**\n\nNow we have **{len(member.guild.members)}** members", inline=False)
                    embed.set_image(url=member.avatar_url)
                    await channel.send(embed=embed)
                except Exception as e:
                    raise e
            except Exception as e:
                raise e

    @commands.command()
    @commands.is_owner()
    async def update(self, ctx):
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:        
            await ctx.send(f"Restarting and rolling update across {len(ctx.bot.guilds)} servers")
            restart_bot()


    @update.error
    async def update_error(self, ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send(f"You are not authorised to use this command")

    @commands.command()
    async def sendpm(self, ctx, *, msg):
        me = await self.bot.fetch_user(597829930964877369)

        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:
            privatedm=Embed(description=f"{ctx.author} {ctx.author.id} said:")
            privatedm.add_field(name="Message", value=msg)
            await me.send(embed=privatedm)
            await ctx.delete()
        

def setup(bot):
    bot.add_cog(staff(bot))
