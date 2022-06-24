import discord
from discord.ext import commands
import re
import asyncio
from cogs.utils import checks

class ModCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ban list test command
    @commands.command()
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def banned(self, ctx, arg, arg2=None, arg3=None, arg4=None):

        if arg == 'add' or arg == 'a':
            banned_open = open('ban_list.txt', 'a')
            banned_open.write('\n' + arg2 + ' ' + arg3 + ' ' + arg4)
            banned_open.close()
            await ctx.send('Added `' + arg2 + '` to Banned Users!')

        elif arg == 'search' or arg == 's':
            banned = 0
            not_banned = 0
            with open('ban_list.txt', 'r') as banned_open_read:
                datasearch = banned_open_read.readlines()
            for line in datasearch:
                if arg2 in line:
                    banned = banned + 1
                    break
                else:
                    not_banned = not_banned + 1
            if not_banned >= len(datasearch):
                await ctx.send('`' + arg2 + '` is not a banned user!')
            if banned == 1:
                await ctx.send('`' + arg2 + '` is a banned user!')
            return

        elif arg == 'delete' or arg == 'd':
            with open('ban_list.txt', 'r') as banned_delete:
                datalines = banned_delete.readlines()
            with open('ban_list.txt', 'w') as banned_delete:  
                for line in datalines:
                    if arg2 not in line: #checks OT-TID, change to arg4 to check for nID
                        banned_delete.write(line)
                    else:
                        await ctx.send("Removed `" + line.rstrip() + "` from Banned Users!")
            return

        elif arg == 'list' or arg == 'l' or arg == 'users':
            banned_list = open("ban_list.txt", "r")
            banned_read = banned_list.read().splitlines()
            banned_read_new = list(filter(None, banned_read))

            banned_user = '\n'.join(banned_read_new)
            embed=discord.Embed(title="Banned Users", description=banned_user, color = 0x992d22)
            await ctx.send(embed=embed)
            return
        else: 
            embedVar = discord.Embed(title="Banned List Commands", description="Here are all the arguments I accept!", color=0xe74c3c)
            embedVar.add_field(name="Adding users to the banned list", value="Example: `&banned add OT-TID (ID: nintendo-id)`\nYou can also use `a` instead!", inline=False)
            embedVar.add_field(name="Removing users from the banned list", value="Example: `&banned delete OT-TID (ID: nintendo-id)`\nYou can also use `d` instead!", inline=False)
            embedVar.add_field(name="Searching users in the banned list", value="You don't have to include everything, you can just have the OT, TID, or nintendo-id, or any combination\nExample: `&banned search OT-TID (ID: discord-userid)`\nYou can also use `s` instead!", inline=False)
            embedVar.add_field(name="Viewing the whole banned list", value="Example: `&banned list`\nYou can also use `l` or `users` instead!", inline=False)
            await ctx.send(embed=embedVar)

    #purge command
    @commands.command()
    @commands.has_any_role('Admin') 
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        await ctx.message.delete()
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        print(str(ctx.author) + " purged " + str(limit) + " messages in channel " + str(ctx.channel))

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='removemember', aliases=['kick'])
    async def removemember(self, ctx, member: discord.Member=None, *, kickreason=None):

        if kickreason == None:
            responsereason = 'Reason has not been provided'
        else:
            responsereason = 'Reason: ' + kickreason

        embedVar = discord.Embed(title="You have been kicked from Zeraora\'s Emporium", description=responsereason)
        memberstr = str(member)

        role3 = discord.utils.get(ctx.guild.roles, name="Moderator")
        role4 = discord.utils.get(ctx.guild.roles, name="Admin")

        if member in ctx.guild.members:

            if role3 in member.roles or role4 in member.roles:
                await ctx.send('I will not allow you to kick server staff!')
            else:
                await member.send(embed=embedVar)
                await member.kick()
                await ctx.send(memberstr + ' has been kicked `' + responsereason + '`')

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='banmember', aliases=['ban'])
    async def banmember(self, ctx, member: discord.Member=None, *, banreason=None):

        if banreason == None:
            responsereason = 'Reason has not been provided'
        else:
            responsereason = 'Reason: ' + banreason

        #banmessage = "You have been banned from Zeraora\'s Emporium:\n" + responsereason
        embedVar = discord.Embed(title="You have been banned from Zeraora\'s Emporium", description=responsereason)
        memberstr = str(member)

        role3 = discord.utils.get(ctx.guild.roles, name="Moderator")
        role4 = discord.utils.get(ctx.guild.roles, name="Admin")

        if member in ctx.guild.members:

            if role3 in member.roles or role4 in member.roles:
                await ctx.send('I will not allow you to ban server staff!')
            else:
                await member.send(embed=embedVar)
                await member.ban()
                await ctx.send(memberstr + ' has been banned `' + responsereason + '`')
                print(str(memberstr) + ' has been banned by ' + str(ctx.author))

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='unbanmember', aliases=['unban'])
    async def unbanmember(self, ctx, member_id):

        await ctx.guild.unban(discord.Object(id=member_id))
        await ctx.send(str(member_id) + ' has been unbanned.')
        print(str(member_id) + ' has been unbanned by ' + str(ctx.author))

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='banall')
    async def banall(self, ctx, *, username=None):
        if username == None:
            await ctx.send('I need a username to match!')
            return
        else:
            guild = self.bot.get_guild(709788621896417370)
            member_count = 0
            
            for member in ctx.guild.members:
                if username in member.display_name:
                    try:
                        await member.ban()
                        await ctx.send("Successfully banned " + member.mention)
                        member_count += 1
                        #await ctx.send('just a test no ban')
                    except:
                        await ctx.send("Ban failed for " + member.mention)
                        pass
                else:
                    pass

            await ctx.send("There are " + str(member_count) + " members that have been banned with " + username + " in their display name")

    @commands.has_any_role('Admin', 'Moderator', 'Raid Host 🔆')
    @commands.command(name='raid')
    async def raid(self, ctx):
        await ctx.message.delete()
        await ctx.send('<@&712560512730136616>')

    @commands.has_any_role('Admin', 'Moderator')
    @commands.command(name='mute')
    async def mutemember(self, ctx, member: discord.Member=None, duration=None, *, mute_reason=None):

        roleobject = discord.utils.get(ctx.guild.roles, id=712569905043472426)
        #await ctx.send(roleobject)

        try:
            dur_and_unit = re.split('(\d+)',duration)
            # dur_and_unit[1] is the time
            # dur_and_unit[2] is the unit of time
            # print(dur_and_unit)
        except:
            await ctx.send('An error occured when processing the command! Please ensure you\'ve entered a duration and it\'s correct.')

        #await ctx.send(duration)
        #await ctx.send(dur_and_unit[1])
        #await ctx.send(dur_and_unit[3])

        if mute_reason == None:
            mute_reason = 'No reason Given.'

        # no time given and check to see if time is valid
        if duration == None or len(dur_and_unit) < 3:
            if dur_and_unit[0] == 'inf':
                duration = 'infinite time'
                pass # pass because infinite time has len 1, all other real time has 3
            else:
                await ctx.send('I need a time, for infinite time use `inf`. Time format should be `##hr/m/s` and must be included if you want to include a reason')
                return
        else:
            pass
            #await ctx.send('**Error:** Duration is invalid or the Lenght of `dur_and_unit` is invalid, printing values:')
            #await ctx.send('Duration: ' + str(duration))
            #await ctx.send('Length of `dur_and_unit`: ' + str(len(dur_and_unit)))
            #return
    
        # assigns the mute command
        try:
            await member.add_roles(roleobject)
        except:
            await ctx.send('I could not add the muted role.')
        await ctx.send('{} was muted for `{}` because reason: `{}`'.format(member.mention, duration, mute_reason))

        

        # message user with neat embed
        mute_desc = 'You have been muted for `{}` for reason: '.format(duration) + mute_reason
        mute_embedVar = discord.Embed(title="**You have been muted in Zeraora\'s Emporium:**", description=mute_desc, color=0xe74c3c)
        try:
            await member.send(embed=mute_embedVar)
        except discord.errors.Forbidden:
            pass # dont fail incase user has blocked the bot

        # does time stuff, inf needs to be first otherwise infinite time ends :Thinking:
        if dur_and_unit[0] == 'inf':
            return
        elif dur_and_unit[2] == 's':
            wait = int(dur_and_unit[1])
            await asyncio.sleep(wait)
        elif dur_and_unit[2] == 'm':
            wait = 60 * int(dur_and_unit[1])
            await asyncio.sleep(wait)
        elif dur_and_unit[2] == 'hr':
            wait = 3600 * int(dur_and_unit[1])
            await asyncio.sleep(wait)
        else:
            await ctx.send('Not a valid time unit, use `s` for seconds, `m` for minutes, `hr` for hours.')
            return

        # remove mute role and inform user
        await member.remove_roles(roleobject)
        await ctx.send('{} was unmuted after recieving a `{}` mute because reason: `{}`'.format(member.mention, duration, mute_reason))
        unmute_desc = 'You have been unmuted after `{}`.'.format(duration)
        unmute_embedVar = discord.Embed(title="**You have been unmuted in Zeraora\'s Emporium:**", description=unmute_desc, color=0xe74c3c)
        try:
            await member.send(embed=unmute_embedVar)
        except discord.errors.Forbidden:
            await ctx.send('I could not DM the user!')
            pass # dont fail incase user has blocked the bot

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='unmute')
    async def unmutemember(self, ctx, member: discord.Member=None):
        roleobject = discord.utils.get(ctx.message.guild.roles, id=712569905043472426)

        unmute_embedVar = discord.Embed(title="**You have been unmuted in Zeraora\'s Emporium**", color=0xe74c3c)
        await member.remove_roles(roleobject)

        try:
            await member.send(embed=unmute_embedVar)
        except discord.errors.Forbidden:
            await ctx.send('I could not DM the user!')
            pass # dont fail incase user has blocked the bot

        await ctx.send('{} has been unmuted.'.format(member.mention))

    @removemember.error
    @banmember.error
    @mutemember.error
    @unmutemember.error
    async def removemember_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('User is not in this server or cannot be found.')
            return
        if isinstance(error, IndexError):
            await ctx.send('This function is broken currently, please ping Logan and he will look into it')


    @unbanmember.error
    async def unbanmember_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('You must provide a valid user ID')
            return

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send('This command requires the admin role.')

def setup(bot):
    bot.add_cog(ModCommandsCog(bot))
