import json
import time
from cogs.utils import checks
import discord
from discord.ext import commands

class WarnCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def add_warning(self, member, rst, issuer):
        with open("warnings.json", "r") as f:
            rsts = json.load(f)
        if str(member.id) not in rsts:
            rsts[str(member.id)] = {"warns": []}
        rsts[str(member.id)]["name"] = str(member)
        timestamp = time.strftime("%Y-%m-%d %H%M%S", time.localtime())
        rsts[str(member.id)]["warns"].append({"issuer_id": issuer.id, "issuer_name":issuer.name, "reason":rst, "timestamp":timestamp})
        with open("warnings.json", "w") as f:
            json.dump(rsts, f)

    async def remove_warning(self, member, count):
        with open("warnings.json", "r") as f:
            rsts = json.load(f)
        if str(member.id) not in rsts:
            return -1
        warn_count = len(rsts[str(member.id)]["warns"])
        if warn_count == 0:
            return -1
        if count > warn_count:
            return -2
        if count < 1:
            return -3
        warn = rsts[str(member.id)]["warns"][count-1]
        embed = discord.Embed(color=discord.Color.dark_red(), title="Deleted Warn: {} on {}".format(count, warn["timestamp"]),
                              description="Issuer: {0[issuer_name]}\nReason: {0[reason]}".format(warn))
        del rsts[str(member.id)]["warns"][count-1]
        with open("warnings.json", "w") as f:
            json.dump(rsts, f)
        return embed

    @commands.command(name="warnings")
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def listwarns(self, ctx, member:discord.Member):
        """Lists warnings for a user"""
        if member == None:
            member = ctx.message.author
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.set_author(name="Warns for {}#{} | {}".format(member.display_name, member.discriminator, member.id), icon_url=member.avatar_url)
        with open("warnings.json", "r") as f:
            warns = json.load(f)
        try:
            if len(warns[str(member.id)]["warns"]) == 0:
                embed.description = "There are none! Feel free to add some <:slowpokeyay:725511078594871397>"
                embed.color = discord.Color.green()
            else:
                for idx, warn in enumerate(warns[str(member.id)]["warns"]):
                    embed.add_field(name="{}: {}".format(idx + 1, warn["timestamp"]), value="  Moderator: {}\n  Reason: {}".format(warn["issuer_name"], warn["reason"]), inline=False)
        except KeyError:  # if the user is not in the file
            embed.description = "There are none!"
            embed.color = discord.Color.green()
        await ctx.send(embed=embed)

    @commands.command(name="warn")
    @commands.guild_only()
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def warn(self, ctx, member:discord.Member, *, reason=""):
        """Warn a user. Staff only."""
        issuer = ctx.message.author
        await self.add_warning(member, reason, issuer)
        with open("warnings.json", "r") as f:
            rsts = json.load(f)
            warn_count = len(rsts[str(member.id)]["warns"])
        msg_title = "**You have been warned in Zeraora\'s Emporium.**"
        if reason != "":
            msg_desc = "**Reason:** " + reason 
 
        embedVar = discord.Embed(title=msg_title, description=msg_desc, color=0xe74c3c)

        try:
            await member.send(embed=embedVar)
        except discord.errors.Forbidden:
            pass # dont fail incase user has blocked the bot
        msg = "`{}` warned {} (warn `#{}`) |".format(ctx.message.author.name, member.mention, warn_count)
        if reason != "":
            msg += " Reason: " + reason
        await ctx.send(msg)
    
    @commands.command(name="delwarn")
    @commands.guild_only()
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def delwarn(self, ctx, member:discord.Member, idx:int):
        """Remove a specific warning from a user. Staff only."""
        returnvalue = await self.remove_warning(member,idx)
        with open("warnings.json", "r") as f:
            rsts = json.load(f)
            warn_count = len(rsts[str(member.id)]["warns"])
        error = isinstance(returnvalue, int)
        if error:
            if returnvalue == -1:
                await ctx.send("{} has no warns!".format(member.mention))
            elif returnvalue == -2:
                await ctx.send("Warn index is higher than warn count ({})!".format(warn_count))
            elif returnvalue == -3:
                await ctx.send("Warn index below 1!")
            return
        else:
            msg = "**Deleted warn**: {} removed warn #{} from {}".format(ctx.message.author.name, idx, str(member))
            await ctx.send(msg)

    @commands.command(name="clearwarns")
    @commands.guild_only()
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def clearwarns(self, ctx, member:discord.Member):
        """Clears warns of a specific member"""
        with open("warnings.json", "r") as f:
            warns = json.load(f)
        if str(member.id) not in warns:
            await ctx.send("{} has no warns!".format(member.mention))
            return
        warn_count = len(warns[str(member.id)]["warns"])
        if warn_count == 0:
            await ctx.send("{} has no warns!".format(member.mention))
            return
        warns[str(member.id)]["warns"] = []
        with open("warnings.json", "w") as f:
            json.dump(warns, f)
        await ctx.send("{} no longer has any warns!".format(member.mention))
        msg = "**Cleared warns**: {} cleared {} warns from {}".format(ctx.message.author.name, warn_count, str(member))
        await ctx.send(msg)

    @warn.error
    @listwarns.error
    @delwarn.error
    @clearwarns.error
    async def note_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('Member is not found')

def setup(bot):
    bot.add_cog(WarnCog(bot))
