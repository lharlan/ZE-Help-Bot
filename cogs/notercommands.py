import json
import time
from cogs.utils import checks
import discord
from discord.ext import commands

class NoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def add_note(self, member, rst, issuer):
        with open("notes.json", "r") as f:
            rsts = json.load(f)
        if str(member.id) not in rsts:
            rsts[str(member.id)] = {"notes": []}
        rsts[str(member.id)]["name"] = str(member)
        timestamp = time.strftime("%Y-%m-%d %H%M%S", time.localtime())
        rsts[str(member.id)]["notes"].append({"issuer_id": issuer.id, "issuer_name":issuer.name, "reason":rst, "timestamp":timestamp})
        with open("notes.json", "w") as f:
            json.dump(rsts, f)

    async def remove_note(self, member, count):
        with open("notes.json", "r") as f:
            rsts = json.load(f)
        if str(member.id) not in rsts:
            return -1
        note_count = len(rsts[str(member.id)]["notes"])
        if note_count == 0:
            return -1
        if count > note_count:
            return -2
        if count < 1:
            return -3
        note = rsts[str(member.id)]["notes"][count-1]
        embed = discord.Embed(color=discord.Color.dark_red(), title="Deleted Note: {} on {}".format(count, note["timestamp"]),
                              description="Issuer: {0[issuer_name]}\nNote: {0[reason]}".format(note))
        del rsts[str(member.id)]["notes"][count-1]
        with open("notes.json", "w") as f:
            json.dump(rsts, f)
        return embed

    @commands.command(name="notes")
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def listnotes(self, ctx, member:discord.Member):
        """Lists notes for a user"""
        if member == None:
            member = ctx.message.author
        embed = discord.Embed(color=discord.Color.dark_red())
        embed.set_author(name="Notes for {}#{} | {}".format(member.display_name, member.discriminator, member.id), icon_url=member.avatar_url)
        with open("notes.json", "r") as f:
            notes = json.load(f)
        try:
            if len(notes[str(member.id)]["notes"]) == 0:
                embed.description = "There are none!"
                embed.color = discord.Color.green()
            else:
                for idx, note in enumerate(notes[str(member.id)]["notes"]):
                    embed.add_field(name="{}: {}".format(idx + 1, note["timestamp"]), value="  Moderator: {}\n  Note: {}".format(note["issuer_name"], note["reason"]), inline=False)
        except KeyError:  # if the user is not in the file
            embed.description = "There are none!"
            embed.color = discord.Color.green()
        await ctx.send(embed=embed)

    @commands.command(name="note")
    @commands.guild_only()
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def note(self, ctx, member:discord.Member, *, reason=""):
        """Adds a note for a user. Staff only."""
        issuer = ctx.message.author
        await self.add_note(member, reason, issuer)
        with open("notes.json", "r") as f:
            rsts = json.load(f)
            note_count = len(rsts[str(member.id)]["notes"])

        msg = "{} added a note for {} (note #{}) |".format(issuer.name, member.name, note_count)
        if reason != "":
            msg += " Note: " + reason
        await ctx.send(msg)
    
    @commands.command(name="delnote")
    @commands.guild_only()
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def delnote(self, ctx, member:discord.Member, idx:int):
        """Remove a specific note from a user. Staff only."""
        returnvalue = await self.remove_note(member,idx)
        with open("notes.json", "r") as f:
            rsts = json.load(f)
            note_count = len(rsts[str(member.id)]["notes"])
        error = isinstance(returnvalue, int)
        if error:
            if returnvalue == -1:
                await ctx.send("{} has no notes!".format(member.name))
            elif returnvalue == -2:
                await ctx.send("Note index is higher than note count ({})!".format(note_count))
            elif returnvalue == -3:
                await ctx.send("Note index below 1!")
            return
        else:
            msg = "**Deleted note**: {} removed note #{} from {}".format(ctx.message.author.name, idx, str(member))
            await ctx.send(msg)

    @commands.command(name="clearnotes")
    @commands.guild_only()
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def clearnotes(self, ctx, member:discord.Member):
        """Clears notes of a specific member"""
        with open("notes.json", "r") as f:
            notes = json.load(f)
        if str(member.id) not in notes:
            await ctx.send("{} has no notes!".format(member.name))
            return
        note_count = len(notes[str(member.id)]["notes"])
        if note_count == 0:
            await ctx.send("{} has no notes!".format(member.name))
            return
        notes[str(member.id)]["notes"] = []
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        await ctx.send("{} no longer has any notes!".format(member.name))
        msg = "**Cleared notes**: {} cleared {} notes from {}".format(ctx.message.author.name, note_count, str(member))
        await ctx.send(msg)

    @note.error
    @listnotes.error
    @delnote.error
    @clearnotes.error
    async def note_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('Member is not found')

def setup(bot):
    bot.add_cog(NoteCog(bot))