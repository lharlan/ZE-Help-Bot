from gpiozero import CPUTemperature
import psutil
import discord
from discord.ext import commands

class RpiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Rtemp')
    async def Rtemp(self, ctx):

        await ctx.send('Command is now defunct, use `!Rsystem`')

    @commands.command(name='Rsystem')
    async def Rsystem(self, ctx):

        cpu = CPUTemperature()
        cpu_per = psutil.cpu_percent()
        mem_per = psutil.virtual_memory().percent

        await ctx.send('Current CPU usage ' + str(cpu_per) + '%\nCurrent Memory usage ' + str(mem_per) + '%\nCurrent CPU Temperature is ' + str(cpu.temperature) + 'C')


    @commands.command(name="serverslist")
    async def serverslist(self, ctx):
        activeservers = self.bot.guilds
        for guild in activeservers:
            await ctx.send(guild.name)
            print(guild.name)


def setup(bot):
    bot.add_cog(RpiCog(bot))
