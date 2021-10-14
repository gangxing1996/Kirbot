from discord.ext.commands.core import command
from discord.ext import commands
from mybot import MyBot
import json
from worm import get_curr
import re
import discord
import os 
import util
if __name__ == '__main__':

    with open('config.json','r',encoding='utf8') as jfile:
        jdata=json.load(jfile)
    bot = MyBot(command_prefix=jdata["command_prefix"])
    # bot=commands.Bot(command_prefix="]")

    # @bot.command()
    # async def ping(ctx):
    #     await ctx.send(f"{int(bot.latency*1000)}(ms)")

    bot.load_extension("cmds.basis")
    @bot.listen('on_message')
    async def incomming_message(message):
        # don't respond to ourselves
        if message.author == bot.user:
            return
        if message.author.name == "kangkang" and message.content == "kirby":
             await message.channel.send("妈妈")
        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content == '台币':
            await message.channel.send("银联人民币对新台币汇率："+ get_curr())
        if message.content == '孩子' or message.content =='haizi':
            await message.channel.send('孩子')
        if message.content == 'son':
            await message.channel.send('son')
        if message.content.startswith("."):
            if message.content[1:] in bot.pic_names:
                # print(os.path.join(bot.pic_dir,bot.pic_fullnames[bot.pic_names.index(message.content[1:])]))
                f=os.path.join(bot.pic_dir,bot.pic_fullnames[bot.pic_names.index(message.content[1:])])
                pic=discord.File(f)
                await message.channel.send(file=pic)

        if bool(re.search("poyo",message.content,re.IGNORECASE)):
            await message.channel.send(util.poyo())
        
        from util import r_pa
        if bool(re.search("pa",message.content,re.IGNORECASE)):
            await r_pa(message)

        print("received a message from ",message.author.name,message.author.discriminator,message.author.id,message.author.avatar,"\n")

    bot.run(jdata["token"])
    