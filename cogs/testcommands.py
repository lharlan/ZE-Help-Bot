import discord
from discord.ext import commands
from discord.utils import get

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='rolelist')
    async def rolelist(self, ctx, member: discord.Member=None):
        
        for role in member.roles:
            role_list = ('`' + ", ".join([role.name for role in member.roles[1:]]) + '`')

        await ctx.send(role_list)

    @commands.has_any_role('Admin', 'Moderator')
    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    async def check_permissions(self, ctx, *, member: discord.Member=None):

        if not member:
            member = ctx.author

        perms = ', '.join(perm for perm, value in member.guild_permissions if value)

        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))
        embed.add_field(name='\uFEFF', value=perms)     #\uFEFF is a Zero-Width Space
        await ctx.send(content=None, embed=embed)

    @commands.command()
    async def addrole(self, ctx):
        member = ctx.message.author
        role = get(member.guild.roles, name="Growlithe")
        #await self.bot.add_roles(user, role)
        await member.add_roles(discord.Object(id=905179085515399229))
        await ctx.send('added role')


def setup(bot):
    bot.add_cog(TestCog(bot))  
