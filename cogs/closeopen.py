import discord
from discord.ext import commands
from cogs.utils import checks

staff_cat = 711859799654137866
support_cat = 733268625804492900
log_cat = 711875828455178291
backup_cat = 839409995904319508
important_cat = 711878445579239483

async def informchannel_closed(ctx, channel):
    if ctx.channel.id != channel.id:
        await ctx.send('I have closed {}'.format(channel.mention))
        return

async def informchannel_opened(ctx, channel):
    if ctx.channel.id != channel.id:
        await ctx.send('I have opened {}'.format(channel.mention))
        return

async def staffchannelcheck(ctx, channel):
    if (channel.category.id == staff_cat or channel.category.id == support_cat or channel.category.id == log_cat 
    or channel.category.id == backup_cat or channel.category.id == important_cat):
        await ctx.send('That is a staff channel, and I cannot change typing permissions for them')
        return

class CloseOpenCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['close'])
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def lock(self, ctx, channel: discord.TextChannel = None, *, arg = None):
        if not channel:
            channel = ctx.channel

        zera_bdsp = 711864261952929814
        mew_bdsp = 778329754642022460
        amphy_bdsp = 914994177543143484
        osha_swsh = 771894077364764712
        lanbot_swsh = 906881436622159952
        belle_acnh = 907705727647363092
        def_bot_close = 'There is no ETA for the bot\'s return, the owner of this bot will fix it when they have the time. Please use another bot in the meantime, or wait patiently.'

        await staffchannelcheck(ctx, channel)

        if channel.id == zera_bdsp:
            await channel.edit(name='🔴zera_closed')
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)

            if arg == None:
                embedVar = discord.Embed(title='Zera is closed', description=def_bot_close, color=0xddd453)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Zerabot is closed", description=arg, color=0xddd453)
                await channel.send(embed=embedVar)

            await informchannel_closed(ctx, channel)
            return

        elif channel.id == mew_bdsp:
            await channel.edit(name='🔴mew_closed')
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)

            if arg == None:
                embedVar = discord.Embed(title='Mew is closed', description=def_bot_close, color=0x78bdeb)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Mewbot is closed", description=arg, color=0x78bdeb)
                await channel.send(embed=embedVar)

            await informchannel_closed(ctx, channel)
            return

        elif channel.id == amphy_bdsp:
            await channel.edit(name='🔴amphy_closed')
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)

            if arg == None:
                embedVar = discord.Embed(title='Amphy is closed', description=def_bot_close, color=0xffc9ff)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Amphybot is closed", description=arg, color=0xffc9ff)
                await channel.send(embed=embedVar)

            await informchannel_closed(ctx, channel)
            return

        elif channel.id == osha_swsh:
            await channel.edit(name='🔴osha_closed')
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)

            if arg == None:
                embedVar = discord.Embed(title='Osha is closed', description=def_bot_close, color=0x97d5f0)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Oshabott is closed", description=arg, color=0x97d5f0)
                await channel.send(embed=embedVar)

            await informchannel_closed(ctx, channel)
            return

        elif channel.id == lanbot_swsh:
            await channel.edit(name='🔴muk_lan_closed')
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)

            if arg == None:
                embedVar = discord.Embed(title='Muk is closed', description=def_bot_close, color=0x9be688)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Mukbot is closed", description=arg, color=0x9be688)
                await channel.send(embed=embedVar)

            await informchannel_closed(ctx, channel)
            return

        elif channel.id == belle_acnh:
            await channel.edit(name='🔴bellebot_closed')
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)

            if arg == None:
                embedVar = discord.Embed(title='Belle is closed', description=def_bot_close, color=0xfacb3f)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Bellebot is closed", description=arg, color=0xfacb3f)
                await channel.send(embed=embedVar)

            await informchannel_closed(ctx, channel)
            return

        else: 
            #role = discord.utils.get(ctx.guild.roles, name="Admin")
            #role2 = discord.utils.get(ctx.guild.roles, name="Moderator")   

            ## TODO: Add SysBot Specialist to valid roles and finish if statement for checking staff roles

            #if role in ctx.author.roles or role2 in ctx.author.roles:
            channel = channel or ctx.channel
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)

            if arg == None:
                embedVar = discord.Embed(title='Channel is locked', description='idk what else to say read the embed title <:pepechar:765375372271288341>', color=0x992d22)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Channel is locked", description=arg, color=0x992d22)
                await channel.send(embed=embedVar)

            await informchannel_closed(ctx, channel)
            return

    @commands.command(aliases=['open'])
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def unlock(self, ctx, channel: discord.TextChannel = None, game = None, *, arg = None):

        zera_bdsp = 711864261952929814
        mew_bdsp = 778329754642022460
        amphy_bdsp = 914994177543143484
        osha_swsh = 771894077364764712
        lanbot_swsh = 906881436622159952
        belle_acnh = 907705727647363092
        def_bot_open = 'Enjoy! Be sure to use only one bot at a time as well.'

        await staffchannelcheck(ctx, channel)

        if not channel:
            channel = ctx.channel

        if channel.id == zera_bdsp:

            if game == 'pla':
                gameaddon = 'pla'
            elif game == 'bdsp':
                gameaddon = 'bdsp'
            elif game == 'swsh':
                gameaddon = 'swsh'
            else:
                await ctx.send('You must provide a game! Valid games are `swsh`, `bdsp`, `pla`')
                return

            channel_name = '🟢zera_' + gameaddon

            await channel.edit(name=channel_name)
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)

            if arg == None:
                embedVar = discord.Embed(title='Zera is open for trading!', description=def_bot_open, color=0xddd453)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Zerabot is open", description=arg, color=0xddd453)
                await channel.send(embed=embedVar)

            await informchannel_opened(ctx, channel)
            return

        elif channel.id == mew_bdsp:

            if game == 'pla':
                gameaddon = 'pla'
            elif game == 'bdsp':
                gameaddon = 'bdsp'
            elif game == 'swsh':
                gameaddon = 'swsh'
            else:
                await ctx.send('You must provide a game! Valid games are `swsh`, `bdsp`, `pla`')
                return

            channel_name = '🟢mew_' + gameaddon

            await channel.edit(name=channel_name)
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)

            if arg == None:
                embedVar = discord.Embed(title='Mew is open for trading!', description=def_bot_open, color=0x78bdeb)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Mewbot is open", description=arg, color=0x78bdeb)
                await channel.send(embed=embedVar)

            await informchannel_opened(ctx, channel)
            return

        elif channel.id == amphy_bdsp:

            if game == 'pla':
                gameaddon = 'pla'
            elif game == 'bdsp':
                gameaddon = 'bdsp'
            elif game == 'swsh':
                gameaddon = 'swsh'
            else:
                await ctx.send('You must provide a game! Valid games are `swsh`, `bdsp`, `pla`')
                return

            channel_name = '🟢amphy_' + gameaddon

            await channel.edit(name=channel_name)
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)

            if arg == None:
                embedVar = discord.Embed(title='Amphy is open for trading!', description=def_bot_open, color=0xffc9ff)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Amphybot is open", description=arg, color=0xffc9ff)
                await channel.send(embed=embedVar)

            await informchannel_opened(ctx, channel)
            return

        elif channel.id == osha_swsh:

            if game == 'pla':
                gameaddon = 'pla'
            elif game == 'bdsp':
                gameaddon = 'bdsp'
            elif game == 'swsh':
                gameaddon = 'swsh'
            else:
                await ctx.send('You must provide a game! Valid games are `swsh`, `bdsp`, `pla`')
                return

            channel_name = '🟢osha_' + gameaddon

            await channel.edit(name=channel_name)
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)

            if arg == None:
                embedVar = discord.Embed(title='Osha is open for trading!', description=def_bot_open, color=0x97d5f0)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Oshabott is open", description=arg, color=0x97d5f0)
                await channel.send(embed=embedVar)

            await informchannel_opened(ctx, channel)
            return

        elif channel.id == lanbot_swsh:
            await channel.edit(name='🟢muk_lan_swsh')
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)

            if arg == None:
                embedVar = discord.Embed(title='Muk is open for trading!', description=def_bot_open, color=0x9be688)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Mukbot is open", description=arg, color=0x9be688)
                await channel.send(embed=embedVar)

            await informchannel_opened(ctx, channel)
            return

        elif channel.id == belle_acnh:
            await channel.edit(name='🟢bellebot_acnh')
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)

            if arg == None:
                embedVar = discord.Embed(title='Belle is open for trading!', description=def_bot_open, color=0xfacb3f)
                await channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="Bellebot is open", description=arg, color=0xfacb3f)
                await channel.send(embed=embedVar)

            await informchannel_opened(ctx, channel)
            return

        else: 
            channel = channel or ctx.channel
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)

            if arg == None:
                embedVar = discord.Embed(title='Channel is unlocked', description='Type away!', color=0x992d22)
                await channel.send(embed=embedVar)
            else:

                real_desc = game + ' ' + arg # need this because the way i set up each input for the command
                embedVar = discord.Embed(title="Channel is unlocked", description=arg, color=0x992d22)
                await channel.send(embed=embedVar)

            await informchannel_opened(ctx, channel)
            return

def setup(bot):
    bot.add_cog(CloseOpenCog(bot))  
