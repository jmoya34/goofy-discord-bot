from asyncio import tasks
from venv import create
import discord, cv2
from discord.ext import tasks
import asyncio
import datetime as dt
import json

token = ''
client = discord.Client()


def get_days_gone() -> int:
    with open ('chached_data.json', 'r') as file:
        temp = json.load(file)
    return temp["days_gone"]


def create_image(days_gone, iftrue: bool):
    '''
    Takes image taken and changes the text everytime the day changes
    '''
    img = cv2.imread('obama.jpg', cv2.IMREAD_ANYCOLOR)

    if days_gone == 0:
        cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, "racial slurs", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, str(days_gone), (290,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)
            
    elif days_gone < 10:
        cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, "racial slurs", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, str(days_gone), (290,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)

    elif days_gone < 100:
        cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, "racial slurs", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, str(days_gone), (290,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)

    elif days_gone < 1000:
        cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, "racial slurs", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, str(days_gone), (290,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)

    elif days_gone < 10000:
        cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, "racial slurs", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
        cv2.putText(img, str(days_gone), (270,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)

    cv2.imwrite("output.png", img, [cv2.IMWRITE_PNG_COMPRESSION])

    if iftrue:
        with open ("chached_data.json", 'w') as file:
            days_gone = 0
            temp = {'days_gone': int(days_gone)}
            file = json.dump(temp, file)
    else:
        with open ("chached_data.json", 'w') as file:
            days_gone += 1
            temp = {'days_gone': int(days_gone)}
            file = json.dump(temp, file)

@tasks.loop(minutes=60*24) # WOULD BE 60 * 24
async def msg1():
    message_channel = client.get_channel(971678103061536768)
    create_image(days_gone=get_days_gone(), iftrue=False)
    with open("output.png", 'rb') as f:
        picture = discord.File(f)
        print(type(picture))
        await message_channel.send(file=picture)


@msg1.before_loop
async def before_msg1():
    for _ in range(60):  # loop the whole day
        if dt.datetime.now().minute == dt.datetime.now().minute + 1:  # 24 hour format
            print('It is time')
            return
        print("The time is", dt.datetime.now().minute)
        await asyncio.sleep(1)# wait a second before looping again. You can make it more 


@client.event
async def on_ready():
    print("Server on")


@client.event
async def on_message(message):
    memberid = message.author
    print(memberid)
    print("Oh no the nono word said and the word is:")

    nono_words = ["Dragon maid was mid"]

    for word in nono_words:
        if message.content.find(word) != -1:
            create_image(days_gone=0, iftrue=True)
            with open("output.png", 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
                await message.channel.send("OH NO " + str(memberid)[0:len(str(memberid))-5] + " SAID A NONO WORD!!")

    if message.content == "i'd peg angelo":
        await message.channel.send("So would I")

msg1.start()
client.run(token)