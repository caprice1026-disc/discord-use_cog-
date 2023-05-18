from discord.ext import commands

class Web3Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def my_command(self, ctx):
        await ctx.send('This is my command!')

def setup(bot):
    bot.add_cog(Web3Cog(bot))