import discord
from discord.ext import commands
from .Cog_t import Cog_T
class Basis(Cog_T):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{int(self.bot.latency*1000)}(ms)")

    # @commands.command()
    # async def pic(self,ctx):
    #     await ctx.send(self.bot.pic_names)
    
    # @commands.command()
    # async def up_pic(self,ctx,pic_name):

    #     pass

def setup(bot):
    bot.add_cog(Basis(bot))
if __name__=="__main__":
    pass