import random
import discord
import os
import json
import functools
def check_admin(func):
    with open('config.json','r',encoding='utf8') as jfile:
        jdata=json.load(jfile)
    # def authorited(cmd):
    #     return cmd
    # def unauthorited(cmd):
    #     async def send_unauthorited(ctx):
    #         await ctx.send("You are NOT a administrator!!!")
    #     return send_unauthorited
    # if ctx.author.id in jdata['admin_id']:
    #     return authorited
    # else:
    #     return unauthorited
    @functools.wraps(func)
    async def decorator(*args):
        # print(args[1].author.id ,"\n", jdata['admin_id'])
        if args[1].author.id in jdata['admin_id']:
            await func(*args)
        else:
            await args[1].send(f"{args[1].author.mention}You are NOT a administrator!!!")

    return decorator




async def r_pa(message):
    # print("entered PA /n")
    await message.channel.send("ta~")
    # print("out PA \n")

def poyo():
    ans=("P" if random.random()>0.5 else "p")+"oyo"+"o"*int(random.random()/0.35)+"~"*int(random.random()/0.35)
    return ans

# class Pic():
#     def __init__(self):
#         self.pic_dir="./pic"
#         self.pic_fullnames=os.listdir(self.pic_dir)
#         self.pic_names=[name.split(".")[0] for name in self.pic_fullnames]
if __name__=="__main__":
    # print(random.random())
    print(poyo())
