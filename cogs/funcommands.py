import discord
from discord.ext import commands
import random
import os

def randomline(txtfile):
    lines = open(txtfile).read().splitlines()
    return random.choice(lines)


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='convert')
    async def convert(self, ctx, arg, arg2):

        cmeasurement = 0

        if arg2 == 'F' or arg2 == 'f':
            cmeasurement = (float(arg) - 32) * (5 / 9)
            cunit = 'C'
            ctype = 'temperature'

        if arg2 == 'C' or arg2 == 'c':
            cmeasurement = (float(arg) * (9 / 5)) + 32
            cunit = 'F'
            ctype = 'temperature'

        if arg2 == 'M' or arg2 == 'm' or arg2 == 'miles':
            cmeasurement = (float(arg)) * 1.609344
            cunit = 'Km'
            ctype = 'length'

        if arg2 == 'Km' or arg2 == 'km' or arg2 == 'kms':
            cmeasurement = (float(arg)) * 0.62137119
            cunit = 'miles'
            ctype = 'length'

        await ctx.send('Your converted {} is {} {}'.format(ctype, str(round(cmeasurement, 2)), cunit))

    @commands.command(name='bozley')
    async def bozley(self, ctx):

        upload_msg = await ctx.send("uploading image...")
        await ctx.send(file=discord.File("bozley/" + random.choice(os.listdir("bozley"))))
        await upload_msg.delete()

    @commands.command(name='talk4me')
    @commands.has_any_role('Admin', 'Moderator') 
    async def talk4me(self, ctx, channel: discord.TextChannel = None, *, msg = None):

        if '@everyone' in msg or ('<@&' in msg and '>' in msg):
            await ctx.send('You cannot use me to ping everyone or a specific role')
        else:
            msg_author = str(ctx.author)
            await channel.send(msg)
            await ctx.message.delete()
            print(msg_author + " sent the message " + msg + " in channel " + str(channel))

    @commands.command(name='loganbot')
    async def loganbot(self, ctx):
        await ctx.send('Logan is not a bot! But I am')

    #@commands.command(name='suffer')
    #@commands.has_any_role('Admin', 'Moderator') 
    #async def suffer(self, ctx):

    #    await ctx.send('Ok fuck this iam leaving. He was spamming and i was trying to report it. And you say its me thats in the wrong here. This server staff dont know wtf they doing\n-Sufferlord May 27, 2017')

    @commands.command(name='whoisnt')
    async def whoisnt(self, ctx):
        await ctx.send('Shut up Cody')

    @commands.command(name='rps')
    async def rps(self, ctx, player):

        choices = ['rock', 'paper', 'scissors']

        if player.lower() not in choices:
            await ctx.send('That\'s illegal, you forefit')

        computer = random.choice(choices)

        await ctx.send('I\'ve picked ' + computer + ', you\'ve picked ' + player.lower() + '.')

        if computer == player.lower():
            await ctx.send('Tie!')
        
        elif player.lower() == 'rock':
            if computer == 'paper':
                await ctx.send('You lose!')
            if computer == 'scissors':
                await ctx.send('You win!')

        elif player.lower() == 'paper':
            if computer == 'rock':
                await ctx.send('You win!')
            if computer == 'scissors':
                await ctx.send('You lose!')

        elif player.lower() == 'scissors':
            if computer == 'rock':
                await ctx.send('You lose!')
            if computer == 'paper':
                await ctx.send('You win!')

    @commands.command(name='joke')
    async def joke(self, ctx):
        await ctx.send(randomline('jokes.txt'))
    

def setup(bot):
    bot.add_cog(FunCog(bot))
