import discord
from discord.ext import commands

class TriggerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if ">amphydead" in message.content:
            await message.channel.send("Thanks Elon")

def setup(bot):
    bot.add_cog(TriggerCog(bot))  