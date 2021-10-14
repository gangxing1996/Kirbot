import discord
from discord.ext import commands
from .cog_t import Cog_T
class basis(Cog_T):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{int(self.bot.latency*1000)}(ms)")
    @commands.command()
    async def pic(self,ctx):
        await ctx.send(self.bot.pic_names)
def setup(bot):
    bot.add_cog(basis(bot))
if __name__=="__main__":
    pass