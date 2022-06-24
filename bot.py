import os
import discord
from discord.ext import commands
#import importlib
#import logging
#import random
from dotenv import load_dotenv
import logging

# sets up basic logging in a txt file
#logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()  # All but the two privileged ones
intents.members = True  # Subscribe to the Members intent

bot = commands.Bot(command_prefix='!', intents=intents)
command_ch = 711862338382463067      # ZE command channel (for testing)
bot_help_ch = 711870218904928276     # ZE bot-help channel
spam_ch = 732792223162433646         # ZE spam channel (for testing)
bdsp_ch = 907682560002363472         # bdsp channel
pk8_chat_ch = 738917733915295774     # pk8-chat channel

# termial response that the bot has connected
@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

# Loading Extensions
bot_extensions = ['cogs.eval', 'cogs.errorhandler', 'cogs.modcommands', 'cogs.bothelpcommands', 'cogs.infocommands', 'cogs.funcommands', 'cogs.notercommands', 'cogs.owner', 'cogs.pingreplies', 'cogs.bothelpreplies', 'cogs.warn', 'cogs.botaltfinder', 'cogs.RPiCommands', 'cogs.closeopen']

for extension in bot_extensions:
    bot.load_extension(extension)

# ping command
@bot.command(name='ping', help='pong')
async def ping(ctx):
    await ctx.send(f'pong! Current latency is `{round(bot.latency * 1000)}ms`')

# hello command
@bot.command(name='hello', help='Says hi back.')
async def hello(ctx):
    response = 'Hi! Type `!info` if you\'d like to know more about me!'
    await ctx.send(response)

# bot auto reposnse
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if message.author.bot: 
        return

    if "i love growlithe" in message.content.lower() or "do you love me" in message.content.lower():
        await message.channel.send('Growlithe loves you <:LovePichu:719983283215270001>')
        return

    if 'hey growlithe' in message.content.lower() and message.author.id == 462273017284919326:
        await message.channel.send('Hey Logan. I hope things are going good for you.')
        if 'report' in message.content:
            await message.channel.send('All systems functional and nominal.\nThere are {} cogs currently loaded: '.format(len(list(bot.cogs))))
            await message.channel.send(list(bot.cogs))
        return

    if 'is logan' in message.content.lower() and 'bot' in message.content.lower():
        await message.channel.send('Logan is not a bot, he is a very busy human with his classes and maintaining my framework')
        return

    if 'thanks' in message.content.lower() and 'growlithe' in message.content.lower():
        if message.author.id == 462273017284919326:
            await message.channel.send('Of course Logan, anytime')
        else:
            await message.channel.send('You\'re welcome, lovely human! :)')
        return

    await bot.process_commands(message)

@bot.command(name='logout')
@commands.has_any_role('Admin') 
async def logout(ctx, arg=None):

    if arg == None or arg == 'now':
        await ctx.send('Shutting down.')
        await ctx.bot.close()

    if arg == 'proper' or arg == 'p':
        await ctx.send('Growlithe is beginning the shut down process. First unloading all currently loaded extensions.')
        print('The shut down process has begun, initialized by ' + str(ctx.author))

        for extension in bot_extensions:
            try:
                bot.unload_extension(extension)
            except Exception as e:
                await ctx.send(f'Ignoring: ERROR: {type(e).__name__} - {e}')
                pass
                return

        await ctx.send('All extensions successfully unloaded, shutting down now.')
        await ctx.bot.close()

# assigns Trainer role on member join
@bot.event
async def on_member_join(person):
    Trainer_Role = 711901553568776223
    Announcement_Role = 764524310706257920
    channel = bot.get_channel(711900529722392596)
    await person.add_roles(person.guild.get_role(Trainer_Role))
    await person.add_roles(person.guild.get_role(Announcement_Role))
    await channel.send('Successfully given Trainer and Announcement roles to ' + person.mention)

bot.run(TOKEN)
