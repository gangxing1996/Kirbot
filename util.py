import random
import discord
import os
import json
import functools
import csv 
def check_admin(func):
    with open('config.json','r',encoding='utf8') as jfile:
        jdata=json.load(jfile)

    @functools.wraps(func)
    async def decorator(*args):
        # print(args[1].author.id ,"\n", jdata['admin_id'])
        if args[1].author.id in jdata['admin_id']:
            await func(*args)
        else:
            await args[1].send(f"{args[1].author.mention}You are NOT a administrator!!!")

    return decorator


def read_qa():
    with open('config.json','r',encoding='utf8') as jfile:
        jdata=json.load(jfile)
    file_name=jdata["qa"]
    with open(file_name,mode="r",encoding="utf8") as file:
        rows=rows=list(csv.reader(file))
        file.readline()
        qa_dict={row[0]:row[1:] for row in rows}
    return qa_dict


async def r_pa(message):
    # print("entered PA /n")
    await message.channel.send("ta~")
    # print("out PA \n")

def poyo():
    ans=("P" if random.random()>0.5 else "p")+"oyo"+"o"*int(random.random()/0.35)+"~"*int(random.random()/0.35)
    return ans

def pic_list_web():
    import time
    import os
    dir="./pic"
    fullnames=sorted(os.listdir(dir))
    with open("pic_list.md","w") as f:
        f.write( "---\n")
        f.write("title: Kirbot Sticker List\n")
        f.write(f"date: {time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}\n")
        f.write(f"update: {time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}\n")
        f.write( "---\n")
        问号_url="https://s3.bmp.ovh/imgs/2022/04/07/e2e4ca67565a603a.gif"
        for i,fn in enumerate(fullnames):
            f.write(f"![]({(fn if fn.split('.')[0]!='?' else 问号_url)})\n")
            f.write(f"{fn}\n")
            f.write("---\n")
            if (i==0):
                f.write("<!--More-->\n")

    return


if __name__=="__main__":
    import ipdb
    # import time
    # print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    pic_list_web()
