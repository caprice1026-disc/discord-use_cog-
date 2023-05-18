from discord.ext import commands
import discord

class ForanonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#メッセージを受け取った際に匿名メッセージをギルドに送信する
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        #ギルドを探す
        if message(message.channel, discord.DMChannel):
         guild = discord.utils.get(self.bot.guilds, name='GuildName')
         if guild is not None:
                channel = discord.utils.get(guild.text_channels, name='YourChannelName')
                if channel is not None:
                    await channel.send(f'メッセージが届きました。送信者：{message.author}\n内容:{message.content}')
                else:
                    print(f"チャンネルが見つからないよ 'YourChannelName'")
         else:
                print(f"サーバーが見つからないよ 'GuildName'")

def setup(bot):
    bot.add_cog(ForanonCog(bot))

#匿名用なのでautherは書き出さないように変更しておく。また、匿名メッセージを送信するチャンネル名を変更すること。
#匿名ようだからと言って悪用しないように一応どこかにログを残しておくこと。ログの管理は姉さんに任せる。