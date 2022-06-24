import discord
from discord.ext import commands

class BotHelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        bot_help_ch = 711870218904928276

        if message.channel.id == bot_help_ch and '$trade' not in message.content.lower():

            channel = self.bot.get_channel(bot_help_ch) # set this to whatever channel you want it to read, should be "bot_help_ch" for normal usage

            if ((message.author._roles.has(719622176634044577) or message.author._roles.has(711901391555264514) 
            or message.author._roles.has(711901311234474054) or message.author._roles.has(896746951733805066)) 
            and '!' not in message.content): # bot helper, mod, admin, and founder roles
                return

            if message.author == self.bot.user:
                return

            if message.author.bot: 
                return

            if "how" in message.content.lower() and ("ribbons" in message.content.lower() or "ribbon" in message.content.lower()):
                await message.channel.send(message.author.mention +' Hello! This is an example of adding ribbons to your showdown format. See this link for all ribbons: https://pastebin.com/EwtkQYrx')
                embedVar = discord.Embed(title="Advanced Customization", description="Ribbon Batch Commands Example", color=0xe74c3c)
                embedVar.add_field(name="Ribbon Customization", value="Aerodactyl (M) @ Life Orb \nLevel: 100 \nAdamant Nature \nBall: Moon\n.RibbonEffort=true\n.RibbonBestFriends=true")
                await message.channel.send(embed=embedVar)
                return

            if 'bdsm' in message.content.lower():
                await message.channel.send('I hope you mean \"BDSP\". However since you asked, I am not particularly into that, but whatever floats your boat.')
                await message.channel.send('<:slowshine:727863525007163452>')
                return

            if 'global room' in message.content.lower():
                await message.channel.send(message.author.mention + 'This is how you trade in BDSP')
                await message.channel.send('https://cdn.discordapp.com/attachments/711870218904928276/915333900128112640/ze-pokemon-diamond-pearl-bot-info.png')
                return

            if (("access" in message.content.lower() or "permission" in message.content.lower() or "type" in message.content.lower()) 
                 and "bot" in message.content.lower() or "read only" in message.content.lower()):
                await message.channel.send(message.author.mention +' Welcome to Zeraoras Emporium! <:squirtlewave:847736706433941534> Please go to and read <#872341411733864538>')
                return

            if (('find' in message.content.lower() or 'know' in message.content.lower()) and ("tid" in message.content.lower() or "sid" in message.content.lower())) and 'pkhex' not in message.content.lower() and 'SID:' not in message.content:
                #await message.channel.send(message.author.mention +' Hello! You can find all the information you need on our website https://zeraorasemporium.com/#sid')
                await message.channel.send('Here\'s how you can find your SID: https://zeraorasemporium.com/#sid')
                return

            if (("lets go" in message.content.lower()) or "lgpe" in message.content.lower()) and 'bot' in message.content.lower():
                await message.channel.send(message.author.mention +' Hello! There are no Pokémon: Let\'s Go, Pikachu/Eevee sysbots, maybe google can help you search!')
                return

            if ((' how ' in message.content.lower() and ' do ' in message.content.lower()) or ' can ' in message.content.lower()) and 'lan' not in message.content.lower() and 'acnh' not in message.content.lower() and 'masterball' not in message.content.lower(): 

                if "belle" in message.content.lower() or "acnh" in message.content.lower():
                    await message.channel.send(message.author.mention + ' This is how Belle works: https://zeraorasemporium.com/#acnh')
                    return

                elif 'trade' in message.content.lower() and 'bdsp' in message.content.lower():
                    await message.channel.send(message.author.mention + 'This is how you trade in BDSP')
                    await message.channel.send('https://cdn.discordapp.com/attachments/711870218904928276/915333900128112640/ze-pokemon-diamond-pearl-bot-info.png')
                    return

                #elif ((("trade" in message.content or 'does' in message.content) and 'work' in message.content) or 'bot' in message.content.lower() and 'event' not in message.content.lower() and 'egg' not in message.content.lower() and 'sid' not in message.content.lower()):
                #    await message.channel.send(message.author.mention + ' This is how the bots work: https://zeraorasemporium.com/#instructions')
                #    return

                elif 'egg' in message.content.lower():
                    await message.channel.send(message.author.mention + ' Ahoy! You can trade an egg using the format posted on our website https://zeraorasemporium.com/#egg\nThe BDSP bots will trade eggs in BDSP now using the same format, and you can include egg moves!')
                    return


                #elif ' bots ' in message.content.lower() and 'sid' not in message.content.lower():
                #    await message.channel.send(message.author.mention + ' This is how the bots work: https://zeraorasemporium.com/#instructions')
                #    return

            if (('cancel' in message.content.lower() or 'stop' in message.content.lower() or 'leave' in message.content.lower()) and 
                ('trade' in message.content.lower() or 'queue' in message.content.lower())):
                await message.channel.send(message.author.mention + ' Howdy! The command to leave the queue is `$qc` You can find the bot commands on our website https://zeraorasemporium.com/#bot')
                return

            # bot channel locator
            if 'where' in message.content.lower():
                if 'is' in message.content.lower() and 'osha' in message.content.lower():
                    await message.channel.send(message.author.mention +' Hi there! You can find <@778350518673080370> here: <#771894077364764712>')
                    return

                if 'is' in message.content.lower() and  'zera' in message.content.lower():
                    await message.channel.send(message.author.mention +' Greetings human, You can find <@705163967244533861> here: <#711864261952929814>')
                    return

                if 'is' in message.content.lower() and  'mew' in message.content.lower() and 'somewhere' not in message.content.lower():
                    if 'mewtwo' in message.content.lower():
                        await message.channel.send(message.author.mention +' Howdy! You can find <@905614816520060938> here: <#906881436622159952>')
                        return
                    else:
                        await message.channel.send(message.author.mention +' Hello! You can find <@754194141910532147> here: <#778329754642022460>')
                        return

                if 'is' in message.content.lower() and 'amphy' in message.content.lower():
                    await message.channel.send(message.author.mention + ' Hey! You can find <@915006790628933702> here: <#914994177543143484>')
                    return

                if 'is' in message.content.lower() and 'belle' in message.content.lower():
                    await message.channel.send(message.author.mention +' Hi there! You can find <@907701676205572167> here <#907705727647363092>')
                    return

            if ('which bot' in message.content.lower() or 'what bot' in message.content.lower()) and ('online' in message.content.lower() or 'offline' in message.content.lower()):
                await message.channel.send(message.author.mention +''' here are the sysbot channels:\nA green circle indicates the bot is online, a red circle indicates the bot is offline
<#771894077364764712>\n<#711864261952929814>\n<#778329754642022460>\n<#906881436622159952>\n<#907705727647363092>\n<#914994177543143484>''')
                return

            if ('notrainerfound' in message.content.lower() or (('cant' in message.content.lower() or 'can\'t' in message.content.lower() 
            or 'wont' in message.content.lower() or 'won\'t' in message.content.lower()) and 'trade' in message.content.lower() 
            or 'connect' in message.content.lower())):
                if 'lan' in message.content.lower():

                    lan_reply = '''**__LAN TROUBLESHOOTING__**

**01)** Make sure you have the **lan-play-win64.exe** file running __AS ADMINISTRATOR__ and connect to **emporium.ddns.net:11451.**
**02)** Make sure you have your Switch's current WiFi modified with a random IP between **10.13.0.1 - 10.13.255.254.**
**03)** Make sure your Switch's WiFi's __Subnet Mask__ is set to **255.255.0.0.**
**04)** Make sure your Switch's WiFi __Gateway__ is set to **10.13.37.1.**
**05)** You can set your __Primary DNS__ to **1.1.1.1** and __Secondary DNS__ to **1.0.0.1.**
-- or choose any DNS you'd like, including 90DNS, which blocks connecting to Nintendo's servers, but may cause connection issues.
**06)** In the Switch, go to *System Settings > Internet > Test Connection* to make sure you have 3 green checks.
**07)** Enter Sword/Shield, press **X**, then enter **Options**, then simultaneously push **R-Shoulder + L-Shoulder + L-Stick.**
**08)** Now that you're in LAN Mode, test your connection again like in Step 06.
**09)** You should now see a bunch of text in the **lan-play-win64.exe** window.
**10)** If you see **IConnection::IConnection** in the window in Step 09, you're connected and can begin trading.'''

                    await message.channel.send(lan_reply)
                    return
                else:
                    await message.channel.send('Make sure you\'re connected to the internet, and restart your switch')
                    await message.channel.send('It may also be worth doing a NAT test, Nintendo recommends Type A or B\nhttps://en-americas-support.nintendo.com/app/answers/detail/a_id/22462/~/how-to-use-the-internet-connection-test')
                    #await message.channel.send('If you\'re getting this error for LAN trading, please say \"NoTrainerFound LAN\"')
                    return

            if ('nso ' in message.content.lower() or 'online' in message.content.lower()) and 'need' in message.content.lower():
                await message.channel.send(message.author.mention +' You do need Nintendo Switch Online to trade with the bots, but not for the LAN bot')
                return

            if 'bot is' in message.content.lower() and 'broke' in message.content.lower():
                await message.channel.send('If you suspect a bot is broken, please contact staff using <@575252669443211264>')
                return

            bots_down = ['is the bot down', 'the bot is down', 'are the bots up', 'are the bots working', 'is zera down', 
                         'is mew down', 'is osha down', 'are the bots down', 'bot down', 'is amphy down']

            for down_bot in bots_down:
                if down_bot in message.content.lower():
                    await message.channel.send(message.author.mention +' 🟢 in the channel name means the bot is running, and 🔴 means the bot is down')
                    await message.channel.send('The bots may be down for technical reasons or it is advertising the server')
                    return

            if 'add' in message.content.lower() and ('pokerus' in message.content.lower() or 'pokérus' in message.content.lower()):
                await message.channel.send('Add this text to your format above the moves:\n```\n.PKRS_Infected=true\n.PKRS_Cured=false\n```')
                return

            if 'pid' in message.content.lower() and ('mismatch' in message.content.lower() or 'error' in message.content.lower()):
                await message.channel.send(message.author.mention +' If the pokemon originates from SWSH (Gen 8):')
                await message.channel.send('''use encounter database (ctrl + n) to create the mon, and don\'t change the PID, Height/Weight, IVs, or EC
if you want to make the pokemon from the encounter db shiny, use this tool\nhttps://projectpokemon.org/home/files/file/4447-gen-8-ow-shiny-pid-genner/''')
                await message.channel.send(message.author.mention +' If the pokemon originates from RSE/FRLG/DPPt/HGSS (Gen 3 or 4):') 
                await message.channel.send('see this for resolving the issue\nhttps://docs.google.com/document/d/1ZL5WXaTObn_lJQje4nx_74mXXrMrgTlIHosiYmZVtQ0/edit?usp=sharing')
                return

            if 'how' in message.content.lower() and ('pkhex' in message.content.lower() and 'trade' not in message.content.lower()):
                await message.channel.send(message.author.mention +' See this tutorial for using PKHeX:\nhttps://docs.google.com/document/d/1-7UhGS9SCXhye5ELOlKXg6JUKNGjyWfZpRmLTEOzg74/edit?usp=drivesdk')
                return

            if ('who' in message.content.lower() and 'own' in message.content.lower()) and 'bot' in message.content.lower():
                await message.channel.send(message.author.mention +'\nSimon owns Zera and Osha\nSecludedly owns Mew and Mewtwo\nGenga owns Belle\nCheck out <#711885624348770394> if you\'d like to donate to them!')
                return

            if "ball" in message.content.lower() and ("change" in message.content.lower() or "pick" in message.content.lower()):
                await message.channel.send(message.author.mention +' <:squirtlewave:847736706433941534> Hello! This is how you customize the ball.')
                embedVar = discord.Embed(title="Custom Ball", description="Ball: Moon", color=0xe74c3c)
                embedVar.add_field(name="Example", value="Aerodactyl (M) @ Life Orb \nLevel: 100 \nAdamant Nature \nBall: Moon")
                await message.channel.send(embed=embedVar)
                return

            if (("help" in message.content.lower() and "me" in message.content.lower()) or "i need help" in message.content.lower()) and len(message.content) < 18:
                await message.channel.send('Hello! Here is the help menu, if what you need is not listed below please wait for one of our bot helpers to assist you')
                embedVar = discord.Embed(title="Help Menu", description="Instructions", color=0xe74c3c)
                embedVar.add_field(name="Instruction Video", value="[Video](https://zeraorasemporium.com/#start)")
                embedVar.add_field(name="Showdown Format", value="[Formatting](https://zeraorasemporium.com/#showdown)")
                embedVar.add_field(name="Egg Creation", value="[Eggs](https://zeraorasemporium.com/#egg)")
                embedVar.add_field(name="Create PKM Files", value="[with PKHeX](https://zeraorasemporium.com/#create)")
                embedVar.add_field(name="How to obtain your SID/TID", value="[Secret and Trainer ID](https://zeraorasemporium.com/#sid)")
                embedVar.add_field(name="#Requests", value="[PKM File Requests](https://zeraorasemporium.com/#request)")
                embedVar.add_field(name="Batch Commands", value="[More customization](https://zeraorasemporium.com/#batch)")
                embedVar.add_field(name="Bot Commands", value="[All the bot commands you need](https://zeraorasemporium.com/#bot)")
                embedVar.add_field(name="Locked Pokèmon", value="[Shiny locked and blocked](https://zeraorasemporium.com/#blocked)")
                embedVar.add_field(name="Uploading PKM files using iOS/Android", value="[Mobile device support](https://zeraorasemporium.com/#mobile)")
                await message.channel.send(embed=embedVar)
                return

            if "list" in message.content.lower() and ("acnh" in message.content.lower() or "items" in message.content.lower()):
                embedVar = discord.Embed(title="ACNH Items", description="All items in Animal Crossing", color=0xe74c3c)
                embedVar.add_field(name="Animal Crossing New Horizon item", value="[Item list](https://mpql.net/tools/acnh/codes/item-list)")
                await message.channel.send(embed=embedVar)
                return

            if ("to make" in message.content.lower() or 'i make' in message.content.lower() or 'make it' in message.content.lower()) and 'alpha' in message.content.lower():
                await message.channel.send('The formatting for making a pokemon alpha is `Alpha: Yes`. Please note that capitalization does matter. Please note that certain pokemon have to have a minimum level to be alpha')
                return

def setup(bot):
    bot.add_cog(BotHelpCog(bot))  
