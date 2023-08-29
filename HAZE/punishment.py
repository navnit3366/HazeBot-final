import discord
from discord.ext import commands
from discord.ext.commands import MissingAnyRole
from discord_slash import cog_ext
from discord_slash.context import ComponentContext
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow

HEAD_OFFICER_ID = 762318708596015114
SENIOR_OFFICER_ID = 819210576164028416
OFFICER_ID = 783205193432301578
LEARNER_OFFICER_ID = 795339482693369907
HAZE = 740584420645535775


class Punishment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(description="Get help on punishing a member", guild_ids=[HAZE])
    @commands.has_any_role(HEAD_OFFICER_ID, SENIOR_OFFICER_ID, OFFICER_ID, LEARNER_OFFICER_ID)
    async def punishment(self, ctx):

        buttons = [
            create_button(
                style=ButtonStyle.red,
                label="Warn",
                custom_id="warn",
            ),
            create_button(
                style=ButtonStyle.red,
                label="Mute",
                custom_id="mute",
            ),
            create_button(
                style=ButtonStyle.red,
                label="Kick",
                custom_id='kick',
            ),
            create_button(
                style=ButtonStyle.red,
                label="Ban",
                custom_id="ban",
            ),
        ]

        action_row = create_actionrow(*buttons)

        embed = discord.Embed(description=
                              "Please click on one of the buttons to view the punishments that you need help with"
                              )
        await ctx.send(embed=embed, components=[action_row], hidden=True)

    @commands.Cog.listener()
    async def on_component(self, ctx: ComponentContext):
        if ctx.guild.id==HAZE: 
            if ctx.custom_id == "warn":
                embed = discord.Embed(
                    title="**Warnable Punishment help**",
                    description=
                    "Commands that can be used:\nRiasBot: rias warn MEMBER REASON (main moderation bot used for warnings since it has the automod set)"
                )
                embed.add_field(
                    name="List of warnable punishments",
                    value=
                    "Unnecessary pinging\n\nAttempting to rob Host/Sponsor of Dank Memer Giveaway\n\nRule 4 broken (reaction commands are excluded but depends on how they were used)\n\nRequesting Dank Memer robbing commands to work\n\nSelf promo outside Promotion\nCopypasta outside of spam or off-topic channel\n\nUsing over 50 cuss words in one message/Loop-holing cuss words\nUse ofinappropriate emoji\n\nFalse reporting\n\nChatting in Promotion channel (ignore the first 2 chats or if its 2 lines in mobile and PC view)\n\nFailed to give earrape/flashing images warning\n\nRacist comment/joke (if a blacklisted word wasnt't used)\n\nOffensive content (kids from Africa for example)\n**NOTE:** If a Dank Memer command was used and it shows this, delete the content but don't warn\n\nInsulted Admin/Mod (This warning will take 2 months to be revoked)\n\nHarassment (This warning will take 2 months to be revoked)\n\nAsking for Sub4Sub or Follow4Follow",
                    inline=False)
                embed.add_field(
                    name="**NOTE**:",
                    value=
                    "All warn punishments except harassment and disrespecting admin or mod can be revoked after 30 days if the member is on good behavior.",
                    inline=False)
                await ctx.edit_origin(embed=embed, hidden=True)

            elif ctx.custom_id == "mute":
                embed = discord.Embed(
                    title="**Mutable Punishment help**",
                    description=
                    "Commands that can be used:\nRiasBot: rias mute MEMBER TIME REASON\nArcane: ^mute MEMBER TIME REASON\nCarlbot: c!mute MEMBER TIME REASON\nDyno: ?mute MEMBER TIME REASON\nVortex: >>mute MEMBER TIME REASON\n\nPurge command if needed:\nRiasBot: rias prune MEMBER\n Jeanne: j!mute MEMBER TIME REASON"
                )
                embed.add_field(
                    name="List of mutable punishments",
                    value=
                    "Disrespectful 3hrs\n\nSpamming outside spam channel 6hr (the messages should be purge but with the member mentioned)\n\nMass Pinging 24hr\n\n5 warnings in total 2hr (if mutable punishment is needed, unmute them and add the extra hours)\n\nAttempted use of NSFW commands 12hr\n\nBroke Rule 12",
                    inline=False)
                await ctx.edit_origin(embed=embed, hidden=True)

            elif ctx.custom_id == "kick":
                embed = discord.Embed(
                    title="**Kickable Punishment help**",
                    description="Commands that can be used:\nRiasBot: rias kick MEMBER REASON\nArcane: ^kick MEMBER  REASON\nCarlbot: c!kick MEMBER REASON\nDyno: ?kick MEMBER REASON\nVortex: >>kick MEMBER REASON\n Jeanne: j!kick MEMBER REASON"
                )
                embed.add_field(
                    name="List of kickable punishments",
                    value="Underage IRL to join Discord\n\nAccount is less than 12 hrs old (if their main was disabled or this is an alt but they don't have the main here, it can stay but must have valid reasons)\n\nIndecent username, avatar or status (no matter how indecent it is)\n**NOTE:** Verbally warn them first to change it within 10 minutes\n\nAlt account (if it's not listed in the blacklist and they have a valid reason why the account is there, it can stay)\n\nDMing unwanted/unnecessary content to another member (not DM advertising)",
                    inline=False)
                embed.add_field(
                    name="**NOTE**:",
                    value="Before kicking them, this invite code (VVxGUmqQhF) must be put in the reason to allow them to come back.",
                    inline=False)
                await ctx.edit_origin(embed=embed, hidden=True)

            elif ctx.custom_id == "ban":
                embed = discord.Embed(
                    title="**Bannable Punishment help**\n**NOTE:** Only Officers and above can ban",
                    description="Commands that can be used:\nRiasBot: rias ban MEMBER REASON\nArcane: ^ban MEMBER  REASON\nCarlbot: c!ban MEMBER REASON\nDyno: ?ban MEMBER REASON\nVortex: >>ban MEMBER REASON\n\nPruneban command if needed:\nRiasBot: rias pruneban MEMBER\nJeanne: j!ban MEMBER REASON"
                )
                embed.add_field(
                    name="List of bannable punishments",
                    value="Bypassing mute punishment*\n\nDoxing\n\nUse of blacklisted words or racial slurs (even bypassing them)\n\nPlans of raiding or nuking this server or other servers, even they did this before (either successful or not)\n\nPosting NSFW content*\n\nDM advertising without permission\n\nInappropriate behaviour, even before\n\n10 Warnings in total\n\nWarned 3 times during the 4 hr period*\n\nWarned 5 times for same reason*\n\nScamming\n\nCatfishing\n\nPosting CP and/or Loli/Shota hentai\n\nBypassing the disabled rob commands\n\nDiscord crashing media\n\nBought or sold servers and/or accounts\n\nUsing a modified Discord for malicious plugins (such as able to see the private channels)*",
                    inline=False)
                embed.add_field(
                    name="**NOTE**:",
                    value="Those that have the `*` means they have a chance to appeal for their ban by including this invite code (qZFhxyhTQh), If they have a modified Discord just for **themes only**, they can stay.",
                    inline=False)
                await ctx.edit_origin(embed=embed, hidden=True)

    @punishment.error
    async def punishment_error(self, ctx, error):
        if isinstance(error, MissingAnyRole):
            if ctx.guild.id==HAZE:
                await ctx.send(
                "For privacy reasons, this command will not be executed because you are not a staff of this server"
                )
            else:
                await ctx.send(
                    "For privacy reasons, this command will not be executed outside the source server", delete_after=20
                )



def setup(bot):
    bot.add_cog(Punishment(bot))
