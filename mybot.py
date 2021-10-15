import discord
from discord.ext import commands
from worm import get_curr
import re
import util
import os
class MyBot(commands.Bot):
    def __init__(self,**kwargs):
        super().__init__(command_prefix=kwargs["command_prefix"])
        # self.pic_dir="./pic"
        # self.pic_fullnames=os.listdir(self.pic_dir)
        # self.pic_names=[name.split(".")[0] for name in self.pic_fullnames]

    async def on_ready(self):
        print('Logged on as', self.user,"\n")

    # async def on_message(self, message):
    #     # don't respond to ourselves
    #     if message.author == self.user:
    #         return
    #     if message.author.name == "kangkang" and message.content == "kirby":
    #          await message.channel.send("妈妈")
    #     if message.content == 'ping':
    #         await message.channel.send('pong')
    #     if message.content == '台币':
    #         await message.channel.send("银联人民币对新台币汇率："+ get_curr())
    #     if message.content == '孩子' or message.content =='haizi':
    #         await message.channel.send('孩子')
    #     if message.content == 'son':
    #         await message.channel.send('son')
    #     if message.content.startswith("."):
    #         if message.content[1:] in self.pic_names:
    #             # print(os.path.join(self.pic_dir,self.pic_fullnames[self.pic_names.index(message.content[1:])]))
    #             f=os.path.join(self.pic_dir,self.pic_fullnames[self.pic_names.index(message.content[1:])])
    #             pic=discord.File(f)
    #             await message.channel.send(file=pic)

    #     if bool(re.search("poyo",message.content,re.IGNORECASE)):
    #         await message.channel.send(util.poyo())
        
    #     from util import r_pa
    #     if bool(re.search("pa",message.content,re.IGNORECASE)):
    #         await r_pa(message)

    #     print("received a message from ",message.author.name,message.author.discriminator,message.author.avatar,"\n")

if __name__=="__main__":
    pass