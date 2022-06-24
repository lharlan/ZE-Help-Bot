import discord
from discord.ext import commands
import socket
from cogs.utils import checks

class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @checks.is_logan()
    async def cogload(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**ERROR:** {type(e).__name__} - {e}')
        else:
            await ctx.send('Successfully loaded ' + cog)
            print('Successfully loaded ' + cog)

    @commands.command(name='unload', hidden=True)
    @checks.is_logan()
    async def cogunload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('Successfully unloaded ' + cog)
            print('Successfully unloaded ' + cog)

    @commands.command(name='reload', hidden=True)
    @checks.is_logan()
    async def cogreload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**ERROR:** {type(e).__name__} - {e}')
        else:
            await ctx.send('Successfully reloaded ' + cog)
            print('Successfully reloaded ' + cog)

    @commands.command(name='listcogs', hidden=True)
    @commands.has_any_role('Admin', 'Moderator')
    async def listcogs(self, ctx, param=None):

        if param == 'technical' or param == 't':
            await ctx.send('There are {} cogs currently loaded: '.format(len(list(self.bot.cogs))))
            await ctx.send(self.bot.cogs)
        else:
            await ctx.send(list(self.bot.cogs))

    @commands.command('requestlog')
    @commands.has_any_role('Admin', 'Moderator')
    async def requestlog(self, ctx):

        await ctx.message.add_reaction('\u2705')
        try:
            await ctx.author.send(file=discord.File('discord.log'), content="Here is the log file you requested.")
            print(str(ctx.author) + ' requested access to the log file')
        except:
            await ctx.send('Failed in DMing user')

    @commands.command('printip')
    @checks.is_logan()
    async def printip(self, ctx):
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname + ".local")
        await ctx.send('`' + str(ip_addr) + '`')

    @cogload.error
    @cogunload.error
    @cogreload.error
    async def cogowner_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send('This command is not for you regular people. Only staff and enable/disable my extensions.')
        if isinstance(error, commands.CheckFailure):
            return await ctx.send(f'{error}')

def setup(bot):
    bot.add_cog(OwnerCog(bot))
