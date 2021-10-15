from discord.ext import commands
import discord
import os
from dataclasses import dataclass
import asyncio
import random
class Pic(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        class Pic_data():
            def __init__(self) -> None:
                self.dir="./pic"
                self.fullnames=os.listdir(self.dir)
                self.names=[name.split(".")[0] for name in self.fullnames]
                self.new_pic=[]
                self.new_author=[]
                self.new_hash=[]
        self.bot.pic=Pic_data()
        
        # self.bot.dir="./pic"
        # self.bot.fullnames=os.listdir(self.bot.dir)
        # self.bot.names=[name.split(".")[0] for name in self.bot.fullnames]
    @commands.command()
    async def pic(self,ctx):
        await ctx.send(self.bot.pic.names)
    
    @commands.command()
    async def uppic(self,ctx,*args):
        
        # @dataclass
        # class new:
        #     name:str
        #     user_id:str
        # self.bot.pic.new.append(new(name,ctx.author.id))
        if len(args)==0:
            await ctx.send('输入表情名称, eg  "/uppic kirby" ')
            return
        else:
            name=args[0]
        await ctx.send(f"{ctx.author.mention} 准备接收:{name}")
        self.bot.pic.new_pic.append(name)
        self.bot.pic.new_author.append(ctx.author.id)
        new_hash=random.random()
        self.bot.pic.new_hash.append(new_hash)
        # print(type(ctx.author.id))
        # print(self.bot.pic.new)
        await asyncio.sleep(30)
        try:
            index=self.bot.pic.new_hash.index(new_hash)
            del self.bot.pic.new_pic[index]
            del self.bot.pic.new_author[index]
            del self.bot.pic.new_hash[index]
            await ctx.send("up_pic time out")
        except:
            pass

    @commands.Cog.listener('on_message')
    async def save_pic(self,message):

        if (message.attachments) and (len(self.bot.pic.new_pic)>0) :
            # index,new_pic_name = [(i,n.name) for (i,n) in enumerate(self.bot.pic.new) if n.user_id==message.author.id ]
            try: 
                index=self.bot.pic.new_author.index(message.author.id)
                name=self.bot.pic.new_pic[index]
                del self.bot.pic.new_pic[index]
                del self.bot.pic.new_author[index]
                del self.bot.pic.new_hash[index]
                await message.attachments[0].save(os.path.join(self.bot.pic.dir,name+'.'+message.attachments[0].content_type.split("/")[1]))
                self.bot.pic.names.append(name)
                self.bot.pic.fullnames.append(name+"."+message.attachments[0].content_type.split("/")[1])
                print("uploaded picture")
                await message.channel.send(f"{message.author.mention} 上传成功:{name}")
            except:
                pass



            # if new_pic_name:
            #     print("uploaded picture")
            #     print(f"index:{index} , pic_name :{new_pic_name}")
            # pass

    @commands.Cog.listener('on_message')
    async def send_pic(self,message):
        if message.content.startswith("."):
            if message.content[1:] in self.bot.pic.names:
                # print(os.path.join(bot.dir,bot.fullnames[bot.names.index(message.content[1:])]))
                f=os.path.join(self.bot.pic.dir,self.bot.pic.fullnames[self.bot.pic.names.index(message.content[1:])])
                pic=discord.File(f)
                await message.channel.send(file=pic)
    
def setup(bot):
    bot.add_cog(Pic(bot))
if __name__=="__main__":
    pass