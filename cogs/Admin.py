from discord.ext import commands


from util import check_admin
class Admin(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    @check_admin
    async def load(self,ctx,extension):
        self.bot.load_extension(extension)
        await ctx.send(f'{ctx.author.mention} Loaded {extension}')

    @commands.command()
    @check_admin
    async def reload(self,ctx,extension):
        self.bot.reload_extension(extension)
        await ctx.send(f'{ctx.author.mention} Reloaded {extension}')

    @commands.command()
    @check_admin
    async def unload(self,ctx,extension):
        self.bot.unload_extension(extension)
        await ctx.send(f'{ctx.author.mention} Unloaded {extension}')

def setup(bot):
    bot.add_cog(Admin(bot))
if __name__=="__main__":
    pass