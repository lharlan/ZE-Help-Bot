import discord
from discord.ext import commands

class BotHelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ask')
    async def ask(self, ctx):
        await ctx.send('Just ask your question. Noboby is going to know if they can help unless you ask your question.')

    @commands.command(name='notice')
    async def notice(self, ctx, arg=None):
        await ctx.message.delete()

        if arg == 'questions' or arg == 'q':
            await ctx.send('Questions are not to be asked in this channel. \n<#711870218904928276> is the proper channel for questions.')
        else:
            await ctx.send('Please use this channel for making requests only. File edits are to be posted in <#711870218904928276>. Questions about the SysBots/PKHeX belong in <#711870218904928276>. \nThis is to keep this channel clean to make it easy for people to find their requests. You may include a \"Thank you\" in your request messages, or use <#711875414825631744> to give bot helpers your thanks')

    # encounter database command
    @commands.command(name='ecdb', help='encounter database help')
    async def ecdb(self, ctx):
        await ctx.send('''Use the encounter database in PKHeX (Tools > Data > Encounter Database, or press ctrl + n) enter your search options, then right click > view to send to the main window
It will give you a legal blank slate of a Pokemon that you can use to edit how you want''')

    # mystery gift database
    @commands.command(name='mgdb', help='mystery gift database help')
    async def mgdb(self, ctx):
        await ctx.send('''Use the mystery gift database in PKHeX (Tools > Data > Mystery Gift Database, or press ctrl + g) enter your search options, then right click > view to send to the main window
It will give you all the event pokemon. You can also add new events that have released after a PKHeX update by adding a 
folder in the same folder as your `PKHeX.exe` called `mgdb` and adding `.wc8` files, and restarting PKHeX''')

    # quick link to batch command list, might be useful for helpers
    @commands.command(name='bc', help='Gives a link to the batch command pastebin, say ribbon for the ribbons and command for all commands')
    async def bc(self, ctx, arg):
        if arg == 'command' or arg == 'c':
            await ctx.send('All batch commands: https://pastebin.com/HixDtDxc')
        elif arg == 'ribbon' or arg == 'r':
            await ctx.send('All ribbons/game version values: https://pastebin.com/EwtkQYrx')
        elif arg == 'bdspmet':
            await ctx.send('BDSP Met Location Values: https://pastebin.com/Fk77w1NR\nThis is a WIP and subject to change')
        else:
            await ctx.send('Enter a valid argument')

    # nat test command
    @commands.command(name='nat', help='displays the nat test link and informatio')
    async def nat(self, ctx):
        await ctx.send('Nintendo recommends NAT type A or B for the best trading experience\nhttps://en-americas-support.nintendo.com/app/answers/detail/a_id/22462/~/how-to-use-the-internet-connection-test')

    @commands.command(name='rpl', help='says that ramanas park legends have their HA')
    async def rpl(self, ctx):
        await ctx.send('All Ramanas Park Legendary pokemon have their Hidden Ability')

    @commands.command(name='tryandsee')
    async def tryandsee(self, ctx):
        await ctx.send('https://tenor.com/view/try-it-and-see-give-it-a-try-try-try-and-see-try-it-yourself-gif-24095805')

    @commands.command(name='cl', help='links channels in the server for easy access')
    async def cl(self, ctx, arg):
        if arg == 'mew':
            await ctx.send('<#778329754642022460>')
            return
        elif arg == 'mewtwo' or arg == 'lanbot' or arg == 'lb':
            await ctx.send('<#906881436622159952>')
            return
        elif arg == 'zera':
            await ctx.send('<#711864261952929814>')
            return
        elif arg == 'osha':
            await ctx.send('<#771894077364764712>')
            return
        elif arg == 'belle' or arg == 'acnh':
            await ctx.send('<#907705727647363092>')
            return
        elif arg == 'amphy':
            await ctx.send('<#914994177543143484>')
            return
        elif arg == 'bothelp' or arg == 'bh':
            await ctx.send('<#711870218904928276>')
            return
        elif arg == 'general' or arg == 'gen':
            await ctx.send('<#711869490253529089>')
            return
        elif arg == 'botaccess' or arg == 'ba':
            await ctx.send('<#839412021757214730>')
            return
        else:
            await ctx.send('These are the arguments I accept: general, mew, mewtwo, zera, osha, belle, and bothelp')

        await ctx.message.delete()

    # website linker command
    @commands.command(name='web', help='will link a page on our website given a proper argument\npk8, acnh, egg, lan, lanfaq, intructions, and showdown')
    async def web(self, ctx, arg):
        if arg == 'pk8':
            await ctx.send('https://zeraorasemporium.com/#pk8')
            return
        elif arg == 'acnh' or arg == 'ac':
            await ctx.send('https://zeraorasemporium.com/#acnh')
            return
        elif arg == 'egg':
            await ctx.send('https://zeraorasemporium.com/#egg')
            return
        elif arg == 'lan':
            await ctx.send('https://zeraorasemporium.com/#laninfo')
            return
        elif arg == 'lanfaq' or arg == 'lf':
            await ctx.send('https://zeraorasemporium.com/#lanfaq')
            return
        elif arg == 'instructions' or arg == 'ins':
            await ctx.send('https://zeraorasemporium.com/#instructions')
            return
        elif arg == 'sd' or arg == 'showdown':
            await ctx.send('https://zeraorasemporium.com/#showdown')
            return
        elif arg == 'batch' or arg == 'bc':
            await ctx.send('https://zeraorasemporium.com/#batch')
            return
        elif arg == 'mobile':
            await ctx.send('http://zeraorasemporium.com/#mobile')
            return
        elif arg == 'pkhex':
            await ctx.send('https://projectpokemon.org/home/files/file/1-pkhex/')
            return
        elif arg == 'alm':
            await ctx.send('https://github.com/architdate/PKHeX-Plugins/releases')
            return
        elif arg == 'bdsp':
            await ctx.send('https://zeraorasemporium.com/#bdsp')
            return
        elif arg == 'acnhcodes':
            await ctx.send('https://mpql.net/tools/acnh/codes/item-list/')
            return
        elif arg == 'lanswitch':
            await ctx.send('http://lan-play.com/install-switch')
            return
        elif arg == 'teambuilder' or arg == 'tb':
            await ctx.send('https://play.pokemonshowdown.com/teambuilder')
            return
        elif arg == 'sid' or arg == 'SID':
            await ctx.send('https://zeraorasemporium.com/#sid')
            return
        elif arg == 'plalocations' or arg == 'plal':
            await ctx.send('https://pastebin.com/3pTsquW1')
            return
        elif arg == 'sysbot' or arg == 'sb':
            await ctx.send('https://github.com/kwsch/SysBot.NET')
            return
        else:
            await ctx.send('''https://zeraorasemporium.com\nIf you\'re looking for what agruments I accept: `pk8`, `acnh`, `egg`, 
`lan`, `lanfaq`, `intructions`, `showdown`, `batch`, `mobile`, `pkhex`, `alm`, `bdsp`, `acnhcodes`, `lanswitch`, `teambuilder`, `plalocations`, `sysbot`, and `sid`''')

    @commands.command(name='tbformat', help='links a gif on how to set up teambuilder for BDSP and SwSh')
    async def tbformat(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/764475971272704020/917524293636718602/showdownformat.gif')

    @commands.command(name='helpmenu', help='displays the help menu')
    async def helpmenu(self, ctx):
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
        await ctx.send(embed=embedVar)

    @commands.command(name='bot-help', help='lets the user know the channel is bothelp and not anything else')
    async def bothelp(self, ctx):
        await ctx.message.delete()
        await ctx.send('This channel is for help and discussion regarding the SysBots/PKHeX. Please refrain from using this channel for other topics.')

    @commands.command(name='plaformat')
    async def hisuiforms(self, ctx):
        embedVar = discord.Embed(title="PLA Specific Showdown Formatting", color=0xe74c3c)
        embedVar.add_field(name='For Basculin and Basculegion', value='  Basculin-White\n  Basculegion-M or Basculegion-F', inline=False)
        embedVar.add_field(name='For Hisui Regional Variants', value='  Species-Hisui, Example: Samurott-Hisui', inline=False)
        embedVar.add_field(name='For New Pokemon', value='  Just use their name like normal, Example: Kleavor', inline=False)
        embedVar.add_field(name='For Alpha Pokemon', value='  Alpha: Yes', inline=False)
        embedVar.add_field(name='To Meet Evolution Requirements', value='Certain Pokemon have evolution requirements, such as Basculin-White needing 294 damage, you can add `.FormArgument=XX` to the format, whether it\'s 294 for Basculin-White, or 20 for Stantler\'s Psyshield Bash requirement', inline=False)

        await ctx.send(embed=embedVar)

    @commands.command(name='gvcalc')
    async def gvcalc(self, ctx, IVint=0, GVint=-1):
        # checks there are values
        if IVint == 0 or GVint == -1:
            await ctx.send('You must input values for the IVs and/or GVs, format for this command is `&gvcalc <IV> <GV>`')
            return

        # check values are valid
        if (IVint < 0 or IVint > 31) or (GVint < 0 or GVint > 10):
            await ctx.send('IVs are between 0 and 31, GVs are between 0 and 10')
            return

        if IVint == 31:
            GVdiff = 3
            GVans = GVint - GVdiff
            if GVans < 0:
                await ctx.send('This IV/GV combination is impossible, select new values, format for this command is `&gvcalc <IV> <GV>`')
            else:
                await ctx.send('The GV value you want to set is {}'.format(str(GVans)))

        if IVint <= 30 and IVint >= 26:
            GVdiff = 2
            GVans = GVint - GVdiff
            if GVans < 0:
                await ctx.send('This IV/GV combination is impossible, select new values, format for this command is `&gvcalc <IV> <GV>`')
            else:
                await ctx.send('The GV value you want to set is {}'.format(str(GVans)))

        if IVint <= 25 and IVint >= 20:
            GVdiff = 1
            GVans = GVint - GVdiff
            if GVans < 0:
                await ctx.send('This IV/GV combination is impossible, select new values, format for this command is `&gvcalc <IV> <GV>`')
            else:
                await ctx.send('The GV value you want to set is {}'.format(str(GVans)))

        if IVint <= 19 and IVint >= 0:
            GVdiff = 0
            GVans = GVint - GVdiff
            if GVans < 0:
                await ctx.send('This IV/GV combination is impossible, select new values, format for this command is `&gvcalc <IV> <GV>`')
            else:
                await ctx.send('The GV value you want to set is {}'.format(str(GVans)))

    @commands.command(name='examplepla')
    async def examplepla(self, ctx):
        embedVar = discord.Embed(title="Showdown PLA Format", color=0xe74c3c)
        embedVar.add_field(name="Example:", value="""$trade Growlithe-Hisui
        Adamant Nature
        Alpha: Yes
        Shiny: Yes
        Ball: LAGigaton
        OT: Logan
        OTGender: Female
        TID: 015775
        SID: 2161
        IVs: 0 SpA
        Level: 85
        - Rock Slide
        - Crunch
        - Aerial Ace
        - Iron Tail""")

        await ctx.send(embed=embedVar)

    @commands.command(name='filetype')
    async def filetype(self, ctx):

        embedVar = discord.Embed(title="PKM File Types And Their Supported Games", color=0xe74c3c)
        embedVar.add_field(name='.pk8', value='Sword and Shield', inline=False)
        embedVar.add_field(name='.pb8', value='Brilliant Diamond and Shining Pearl', inline=False)
        embedVar.add_field(name='.pa8', value='Pokemon Legends: Arceus', inline=False)
        embedVar.set_footer(text='Applies only to the games supported by our SysBots, other games have different file types')

        await ctx.send(embed=embedVar)

    @commands.command(name='shinylock')
    async def shinylock(self, ctx, gamearg=None):

        if gamearg == None:
            await ctx.send('Argument missing, valid arguments are `swsh`, `bdsp`, or `pla`')
        elif gamearg == 'swsh':
            await ctx.send('https://cdn.discordapp.com/attachments/711870218904928276/952733767703883876/locked.png')
        elif gamearg == 'bdsp':
            await ctx.send('https://cdn.discordapp.com/attachments/711870218904928276/955107273632538735/locked2-bdsp.png')
        elif gamearg == 'pla':
            await ctx.send('https://cdn.discordapp.com/attachments/711870218904928276/952733768551125083/locked3.jpg')
        else:
            await ctx.send('Invalid argument, valid arguments are `swsh`, `bdsp`, or `pla`')
            return

    @commands.command(name='susact')
    async def susact(self, ctx):
        await ctx.send('Getting a Suspicious Activity message means you\'re trading between two different in-game characters/saves too quickly, intentional or not. Wait a minute or two and try again.')

    @commands.command(name='levelformat')
    async def levelformat(self, ctx):
        await ctx.send('`.CurrentLevel=` should only be used for level 50, and requires the period before hand, any other level needs to use the regular `Level: ` formatting, otherwise the level may be defaulted to 100')

    @commands.command(name='botsbeback')
    async def botsbeback(self, ctx, arg=None):
        await ctx.send('The bots will be back when the owner can fix them, whenever that may be. *I* also sent a message in the bot channel stating the same thing') 

    @commands.command(name='homeupdate')
    async def homeupdate(self, ctx):
        await ctx.send('The SysBots need an update before they can trade pokemon that require a HOME transfer to BDSP and PLA. We do not know when there will be an update, no one in this server is responsible for updating the SysBots.')

    @commands.command(name='pidmethod')
    async def pidmethod(self, ctx, pidtype):
        if pidtype == 'bacd-r' or pidtype == 'bacdr':
            await ctx.send('the BACD_R PID Type is a Reverse Method 1 with a seed between 0x00000000 and 0xFFFF')
        if pidtype == 'Overworld8' or pidtype == 'ow8':
            await ctx.send('Overworld8 is a PID method found on April 1, 2021 by the PKHeX Dev team. I am convinced it is not a real method due to the fact that it has changed nothing, except making it harder to gen overworld pokemon for SwSh')

    @commands.command(name='whoaredevs')
    async def whoaredevs(self, ctx, link=None):
        await ctx.send('No one in this server is responsible for the development of PKHeX, The Pokemon SysBots, or the Animal Crossing Sysbots, no one here can comment on \'When will there be support for this game\' or \'When will this get fixed/changed\'. The devs work on their own time for free, and never provide an ETA on updates/fixed.')

        if link == 'link':
            await ctx.send('https://discord.com/invite/pkhex')
        else:
            pass
        
    @commands.command(name='sid')
    async def sid(self, ctx):

        sid_desc = '''1) Type "$trade <Pokemon>" into one of the bots.
        2) Wait for your DM from the bot with a Link Trade Code.
        3) Once received, enter Link Trade Code in Switch.
        4) Trade a Pokemon you caught yourself in-game to the bot.
        5) Receive the trade request until it's finished.
        6) Upon finishing, the bot will send you a PKM file of what you traded it.
        7) Download the PKM and use PKHeX to view SID (Windows only) or upload the PKM file in one of the bot channels without any commands.'''

        embedVar = discord.Embed(title="HOW TO OBTAIN YOUR SID", description=sid_desc, color=0xe74c3c)
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(BotHelpCog(bot))
