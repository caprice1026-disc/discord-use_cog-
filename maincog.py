import discord
from discord.ext import commands

class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #議題作成コマンド　引数は議題名、ロール　ヘルプをつけること
    @commands.command()
    async def create_thread(ctx, title: str, role: discord.Role):
     thread = await ctx.channel.threads.create(name=title)
     await thread.send(f'{role.mention}, このスレッドはあなたのために作成されました。')
    #タスク作成コマンド　引数はタスク名、担当者、ヘルプをつけること
    @commands.command()
    async def create_task(ctx, title: str, name: discord.Member):
     thread = await ctx.channel.threads.create(name=title, type=discord.ChannelType.private_thread)
     await thread.send(f'{name.mention}, このスレッドはあなたのために作成されました。')


def setup(bot):
    bot.add_cog(MainCog(bot))