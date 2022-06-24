import discord
from discord.ext import commands
from discord.utils import get

logan_id = 462273017284919326
madweeb_id = 734119924464746637

real_admin = 711901311234474054
real_mod = 711901391555264514

def is_logan():
    async def predicate(ctx):
        return ctx.author.id == logan_id
    return commands.check(predicate)

def is_staff():
    async def predicate(ctx):

        mod_role = discord.utils.get(ctx.guild.roles, id=711901391555264514)
        admin_role = discord.utils.get(ctx.guild.roles, id=711901311234474054)

        if mod_role in ctx.author.roles or admin_role in ctx.author.roles:
            return True
    return commands.check(predicate)
        
