from discord.ext import commands

class AltFinderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        command_ch = 711862338382463067
        mew_log_ch = 778331118420099072
        zera_log_ch = 711875874810757241
        osha_log_ch = 718843355706163262
        amphy_log_ch = 914991253999992843

        if (message.channel.id == osha_log_ch or message.channel.id == zera_log_ch or message.channel.id == mew_log_ch or message.channel.id == amphy_log_ch) and 'Found Link Trade partner: ' in message.content:

            channel = self.bot.get_channel(command_ch)
            banned_users = open('ban_list.txt', 'r')
            banned_data = banned_users.readlines()
            new_banned_data = []

            for user in banned_data:
                new_banned_data.append(user.replace('\n', ''))

            for line in new_banned_data:
                if message.content[-25:] == line[-25:] and len(message.content) > 10:
                    await channel.send('I\'ve found an alt account in <#{}>. Please manually verfiy before banning. The user I have found is `'.format(str(message.channel.id)) + line + '`')
                    await channel.send('Message link containing the user found is here: ' + message.jump_url)
                    return

            banned_users.close()
            return

#        if (message.channel.id == zera_log_ch or message.channel.id == mew_log_ch or message.channel.id == amphy_log_ch) and 'Found Link Trade partner: ' in message.content:
#
#            channel = self.bot.get_channel(command_ch)
#            banned_users = open('ban_list.txt', 'r')
#            banned_data = banned_users.readlines()
#            new_banned_data = []
#            split_user = []
#            user_trainer_info = str(message.content.split(':')[4]).lstrip()
#
#            for user in banned_data:
#                split_user.append(user.split(' '))
#                new_banned_data.append(split_user[0])
#
#            for line in new_banned_data:
#                if user_trainer_info in line:
#                    print('found alt:', end=' ')
#                    print(user_trainer_info)
#                    await channel.send('I\'ve found an alt account in <#{}>. Please manually verfiy before banning. The user I have found is `'.format(str(message.channel.id)) + user_trainer_info + '`')
#                    return

def setup(bot):
    bot.add_cog(AltFinderCog(bot))