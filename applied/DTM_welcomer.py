#I would not advise to join the Dark Theme Meme server for the sake of your sanity!
#This is just an example

import discord
from discord.ext import commands

DTM = 719351307814830160
WELCOME_CHANNEL_ID = 730843317268381837


class staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == DTM:
            try:
                channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
                try:
                    embed = discord.Embed(colour=discord.Colour.blue())
                    embed.set_author(name=member.name,
                                     icon_url=member.guild.icon_url)
                    embed.add_field(
                        name="Greetings",
                        value=f"Welcome to {member.guild.name}**\nBefore you can do 'random bullshit go', check out our <#730838968135843856> sponsored by a very cool bruh, <@!709901312980156477>!\n If you break out of them, you are going to Gulag or Brazil!\nEnjoy your stay.\nAlso make sure you join this ban appeal server if you wanna get out of Brazil: https://discord.gg/RPuzv3HBMc",
                        inline=False)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_image(url="https://media.discordapp.net/attachments/913051824095916145/918953413667065856/unknown.png")
                    await channel.send(f"New comrade, {member.mention}!!!", embed=embed)
                except Exception as e:
                    raise e
            except Exception as e:
                raise e

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == DTM:
            try:
                channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
                try:
                    embed = discord.Embed(colour=discord.Colour.red())
                    embed.set_author(name=member.name,
                                     icon_url=member.guild.icon_url)
                    embed.add_field(
                        name="Well shit...",
                        value=f"**{member.mention} went to Gulag to serve the soviet union.**",
                        inline=False)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_image(
                        url="https://media.discordapp.net/attachments/913051824095916145/918954173427507210/60093225.png")
                    await channel.send(embed=embed)
                except Exception as e:
                    raise e
            except Exception as e:
                raise e


def setup(bot):
    bot.add_cog(staff(bot))
