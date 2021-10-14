import random
import discord
import os
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
