#these were people harassing me. This is the oldest botban code I had

from discord.ext import commands
from hazebot import banned_users

DTM = 719351307814830160

class staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        me = self.bot.get_user(597829930964877369)
        if message.author.id in banned_users:
            if me.mentioned_in(message):
                await message.channel.send(f"Unfortunately, {me} has mentionbanned you. If this was a mistake, use `hz!sendpm MESSAGE`", delete_after=10)
                await message.delete()

def setup(bot):
    bot.add_cog(staff(bot))
