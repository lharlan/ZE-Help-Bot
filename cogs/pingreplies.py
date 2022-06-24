from discord.ext import commands

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        mod_role = 711901391555264514
        admin_role = 711901311234474054
        helper_role = 808269965589217300
        command_ch = 711862338382463067 
        pkhexuals_ch = 738917733915295774
        staff_ch = 764475971272704020
        gym_challenge_ch = 973852662711844905
        gami_ch = 767842299958132806
        vouch_ch = 711875414825631744

        if message.author == self.bot.user:
            return

        if message.author.bot: 
            return

# ping replies, these will work in any channel that the bot can type in except #command
        # Logan
        if message.channel.id != command_ch and message.channel.id != pkhexuals_ch and message.channel.id != staff_ch and message.channel.id != 973852662711844905 and message.channel.id != gami_ch and message.channel.id != vouch_ch:
            if ('<@!462273017284919326>' in message.content) or ('@462273017284919326' in message.content):
                if message.author._roles.has(mod_role) or message.author._roles.has(admin_role) or message.author._roles.has(helper_role):
                    await message.channel.send('<:slowshine:727863525007163452>')
                    return
                if message.channel.id == 711870218904928276:
                    await message.channel.send('Do not ping staff or bot helpers in this channel.')
                    return
                else:
                    #await message.channel.send('')
                    await message.channel.send('<:PepePingANGRY:812374407635796028>')
                return
        # Simon
            if '<@!686166019802136602>' in message.content or '@686166019802136602' in message.content:
                await message.channel.send('You pinged Sentinel, he will teleport to you shortly.')
                return
        # Zac
            if '<@!243664830592974848>' in message.content or '@243664830592974848' in message.content:
                await message.channel.send('Why did you ping the Master Lurker? He aint lurking here, so go lurk your way to someone else')
                await message.channel.send('<:SquirtleLurk:716251571998031902>')
                return
        # Cody
            if '<@!715239456839565416>' in message.content or '@715239456839565416' in message.content:
                await message.channel.send('<:Codyannoyed:883905727910019132>')
                return
        # Kait
            if '<@!664243806882889798>' in message.content or '@664243806882889798' in message.content:
                if message.author.id == 654910940629958656: # Solex
                    await message.channel.send('Hi Solex! K8 will be with you in a moment')
                elif message.author.id == 388966638965489665: # DJ
                    await message.channel.send('https://tenor.com/view/venom-lick-creepy-tongue-out-gif-16647618')
                if message.author.id == 462273017284919326: # Logan
                    await message.channel.send('<:grapekait:764571906740977764>')
                else:
                    await message.channel.send('Why did you ping the Grape Queen? She has a whole kingdom to run without you annoying her')
                return
        # Sec
            if '<@!571475470940504065>' in message.content or '@571475470940504065' in message.content:
                await message.channel.send('You\'re not supposed to ping staff. You\'re lucky Sec doesn\'t care or you\'d be sleeping with the fishes.')
                return
        # Igor
            if '<@!829091955333922826>' in message.content or '@829091955333922826' in message.content:
                await message.channel.send('Unless you are sitting with me gaming, beer in hand and chatting I can\'t be any use to you')
                await message.channel.send('<:LucaPing:719619275836620841>')
                return
        # Snake
            if '<@!647221346170044514>' in message.content or '@647221346170044514' in message.content:
                await message.channel.send('Snake? Snake?! SNAAAAAKE!')
                return
        # Steve
            if '<@!710957723050836099>' in message.content or '@710957723050836099' in message.content:
                await message.channel.send('Steve\'s watching the super android 13 movie he will be with you in a moment')
                return
        # Kenji
            if '<@!372050875570585601>' in message.content or '@372050875570585601' in message.content:
                await message.channel.send('<:RaichuBruh:873931531633192960>')
                return
        #Azula
            if '<@!352735435014930433>' in message.content or '@352735435014930433' in message.content:
                await message.channel.send('<a:Anezulurk:734145380849025044>')
                return
        # Viv
            if '<@!386801593535692811>' in message.content or '@386801593535692811' in message.content:
                await message.channel.send('<:harold:783526444336283688>')
                return
        # Kad
            if '<@!662067494332268544>' in message.content or '@662067494332268544' in message.content:
                await message.channel.send('<a:bonk:916459525387730944>')
                return
        # DJ
            if '<@!388966638965489665>' in message.content or '@388966638965489665' in message.content:
                await message.channel.send('Why did you ping DJ? Time to get blasted!\nhttps://tenor.com/view/explosion-dragon-ball-anime-planet-gif-16814673')
                return
        # Froggi
            if '<@!348292921163776020>' in message.content or '@348292921163776020' in message.content:
                await message.channel.send('Froggi\'s a hop and a croak away!')
                return
        # Shae
            if '<@!691433780438630401>' in message.content or '@691433780438630401' in message.content:
                if message.author._roles.has(mod_role) or message.author._roles.has(admin_role):
                    await message.channel.send('<:grapeshae:855282710012755968>')

def setup(bot):
    bot.add_cog(PingCog(bot))
