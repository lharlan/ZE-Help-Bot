import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('TOKEN.env')
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')
bot_testing_ch = 821606211023011852  # my server channel
command_ch = 711862338382463067      # ZE command channel
bot_help_ch = 711870218904928276     # ZE bot-help channel

# termial response that the bot has connected
@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

# hello command
@bot.command(name='hello', help='Says hi back.')
async def hello(ctx):
    response = 'Hi!'
    await ctx.send(response)

# bot auto reposnse
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    bdsp_stfu = ['bdsp bots', 'BDSP bots', 'where is the bdsp bot', 'where is the BDSP bot', 
                 'do you guys have bdsp sysbots', 'where can i find bdsp sysbots', 
                 'bdsp sysbots', 'BDSP sysbots', 'bots for bdsp', 'bots for BDSP', 
                 'what bots work for brilliant diamond', 'what bots work for shining pearl']
    bdsp_send = 'No, there are no BDSP sysbots yet, we do not know when there will be sysbots, just enjoy the game first'
    channel = bot.get_channel(bot_testing_ch)

    for bdsp_message in bdsp_stfu:
        if bdsp_message in message.content:
            await message.channel.send(bdsp_send)


    if 'change ball' in message.content:
        await message.channel.send('add `Ball: Poke` above the moves in your showdown format')

    await bot.process_commands(message)

bot.run(TOKEN)