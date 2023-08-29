# This is a very old bot which has been replaced by a legacy version called Server Utilities.
# It was almost working like LOA Aspect for those in the LOA server. This runs on discordpy 1.7.3
# with discord-py-interactions 3.0.2. You can try for yourself but I won't guarantee satisfying
# results. The maintainance I had on this bot was extremely bad because it was my 3rd bot to make
# over a short period of time.

import os
import discord
from discord import Embed
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.context import ComponentContext
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow
# from discord.utils import get
from dotenv import load_dotenv

WELCOME_CHANNEL_ID = 762990660084563989
LEAVE_CHANNEL_ID = 762990660084563989
HEAD_OFFICER_ID = 762318708596015114
# participant_id = 910132157614272563

# server list
HAZE = 740584420645535775
dark_theme_memes = 719351307814830160
nells_haram = harem = 853079649072316427

# botbanned users
banned_users = [855824458363306064, 800437162343792680, 804529522082840576]
botbanned_msg = "You cannot use this command because you have been botbanned"

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='hz!', intents=intents)
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)
bot.remove_command('help')
bot.load_extension("HAZE.staff")
bot.load_extension("HAZE.punishment")
bot.load_extension("HAZE.stuff")

bot.load_extension("applied.security")
bot.load_extension("applied.DTM_welcomer")
bot.load_extension("applied.dickheads")


@bot.event
async def on_ready():
    owner = await bot.fetch_user(597829930964877369)
    await bot.change_presence(activity=discord.Game(f'Made by {owner}'))

    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

    channel = bot.get_channel(897473395833315369)
    applymsg = await channel.fetch_message(905369395113639936)
    serverlist = await channel.fetch_message(905369394362875915)

    mutuals = [str(x)
               for x in bot.guilds]
    embed = discord.Embed(color=0xADD8E6)
    embed.add_field(name="Network Servers", value=len(bot.guilds), inline=True)
    embed.add_field(name="Servers under HazeBot Protection", value=" \n".join(
        mutuals), inline=False)
    await serverlist.edit(embed=embed)

    buttons = [
        create_button(
            style=ButtonStyle.red,
            label="Apply for staff (CLOSED)",
        ),
        create_button(
            style=ButtonStyle.URL,
            label="Apply for HazeBot",
            url="https://forms.gle/m1ptMJACyzRnA5nL7"
        ),
        create_button(
            style=ButtonStyle.red,
            label="Participate in contest (CLOSED)",
            custom_id='partic'
        ),
    ]

    action_row = create_actionrow(*buttons)
    apply = Embed(
        description="Want to apply for staff or for the HazeBot or join the contest? Click one of those buttons.")
    await applymsg.edit(embed=apply, components=[action_row])


@slash.component_callback()
async def partic(ctx: ComponentContext):
    ended_contest = "Contest has ended.\nPlease wait for a new contest"
    await ctx.send(content=ended_contest, hidden=True)

    # HAZES=bot.get_guild(HAZE)
    # partic_role=get(HAZES.roles, name="Participant")
    # await ctx.author.add_roles(partic_role)
    # await ctx.send("You are now able to participate in the Art #Contest. Made sure you read the rules in <#910132313915006997> and submit in #<#910132270155853844>.\nGood luck", hidden=True)

load_dotenv()
TOKEN = os.getenv("token")
bot.run(TOKEN)
