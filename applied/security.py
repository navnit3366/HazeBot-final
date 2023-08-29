import discord, re , vt
from vt.error import APIError
from discord import Embed
from discord.ext import commands
from discord.ext.commands import MissingRole, UserNotFound
from hazebot import banned_users, botbanned_msg

HAZE = 740584420645535775
dark_theme_memes=719351307814830160
nells_haram= 853079649072316427
horny_jail= 903387713372319765

HEAD_OFFICER_ID = 762318708596015114

vtapi = ... #my VTAPI was here

try:
    vtclient = vt.Client(vtapi)
except APIError:    
    pass


class punishment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(HEAD_OFFICER_ID)
    async def shareban(self, ctx, user: discord.User, *, reason=None):
        haze=self.bot.get_guild(HAZE)
        dtm=self.bot.get_guild(dark_theme_memes)
        hj=self.bot.get_guild(horny_jail)

        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:          
            if reason==None:
                    await ctx.send('Share-ban aborted. No reason provided')
            else:        
                    try:     
                        await haze.ban(user, reason=reason)
                        await ctx.send(f"{user} is now banned in {haze.name}")
                    except:
                        pass
                    try:     
                        await dtm.ban(user, reason=reason)
                        await ctx.send(f"{user} is now banned in {dtm.name}")
                    except:
                        pass
                    try:   
                        await hj.ban(user, reason=reason)
                        await ctx.send(f"{user} is now banned in {hj.name}")
                    except:
                        pass



    @commands.command(aliases=['sunban'])
    @commands.has_role(HEAD_OFFICER_ID)
    async def shareunban(self, ctx, user: discord.User, *, reason=None):
        haze=self.bot.get_guild(HAZE)
        dtm=self.bot.get_guild(dark_theme_memes)
        hj=self.bot.get_guild(horny_jail)

        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:          
            if reason==None:
                    await ctx.send('Share-unban aborted. No reason provided')
            else:
                    try:     
                        await haze.unban(user, reason=reason)
                        await ctx.send(f"**{user}** is now unbanned in **{haze.name}**")
                    except:
                        pass
                    try:     
                        await haze.unban(user, reason=reason)
                        await ctx.send(f"**{user}** is now unbanned in **{dtm.name}**")
                    except:
            
                        pass
                    try:   
                        await haze.unban(user, reason=reason)
                        await ctx.send(f"{user} is now banned in {hj.name}")
                    except:
                        pass                    

    @shareban.error
    async def shareban_error(self, ctx, error):
            if isinstance(error, UserNotFound):
                    await ctx.send("Share-ban aborted. Invalid User ID given")
            elif isinstance(error, MissingRole):
                    await ctx.send("Share-ban aborted. You are not authorised to use this command, even if you do in the source server", delete_after=10)



    @shareunban.error
    async def shareunban_error(self, ctx, error):
            if isinstance(error, UserNotFound):
                    await ctx.send("Share-unban aborted. Invalid user ID given")
            elif isinstance(error, MissingRole):
                    await ctx.send("Share-unban aborted. You are not authorised to use this command, even if you do in the source server", delete_after=10)
    
    @commands.Cog.listener()
    async def on_message(self, ctx):

        web_links=['http', 'www']

        if any(web_links in ctx.content for web_links in web_links):
            link = re.search("(?P<url>https?://[^\s]+)", ctx.content).group("url")
            url_id = vt.url_id(link)

            url = await vtclient.get_object_async("/urls/{}", url_id)
            analysis = dict(url.last_analysis_stats)
            haze_log=self.bot.get_channel(783245677936771083)
            dtm_log=self.bot.get_channel(730844972353585266)
            hj_log=self.bot.get_channel(905385740588957736)

            haze=self.bot.get_guild(HAZE)
            dtm=self.bot.get_guild(dark_theme_memes)
            hj=self.bot.get_guild(horny_jail)

            if analysis.get('malicious')> 0:

                    await ctx.channel.send(f'MALICIOUS LINK DETECTED!\n\nSender is {ctx.author.mention}', delete_after=60)
                    msg=Embed(title="Malicious Link Detected", description="A malicious link has been detected in one of the networked servers. The sender of that link might have been punished depending on the punishment set by their owner.")
                    msg.add_field(name="URL:", value=f"`{link}`")
                    msg.add_field(name="Malicious:",value=analysis.get('malicious'),inline=False)
                    msg.add_field(name="Suspicious:",value=analysis.get('suspicious'),inline=False)
                    msg.add_field(name="Sender name", value=ctx.author, inline=False)
                    msg.add_field(name="Sender ID", value=ctx.author.id, inline=False)

                    await haze_log.send(embed = msg)
                    await dtm_log.send(embed = msg)
                    await hj_log.send(embed=msg)
                    await ctx.delete()
                    
                    try:
                        await haze.ban(ctx.author, reason="Sending Malicious Links detected by the VirusTotal API")
                    except:
                        pass
                    try:
                        await dtm.ban(ctx.author, reason="Sending Malicious Links detected by the VirusTotal API")
                    except:
                        pass
                    try:
                        await hj.ban(ctx.author, reason="Sending Malicious Links detected by the VirusTotal API") 
                    except:
                        pass

    @commands.command()
    @commands.has_role(HEAD_OFFICER_ID)
    async def send(self, ctx, *, msg):

        haze = self.bot.get_channel(775020961984413696)
        dtm = self.bot.get_channel(849681077094318100)
        hj = self.bot.get_channel(904644396597780551)
        if ctx.author.id in banned_users:
            await ctx.send(botbanned_msg)
        else:          
            if ctx.guild.id == HAZE:
                try:
                    await dtm.send(msg)
                except:
                    pass
                try:
                    await haze.send(msg)
                except:
                    pass
                try:
                    await hj.send(msg)
                except:
                    pass


def setup(bot):
    bot.add_cog(punishment(bot))
