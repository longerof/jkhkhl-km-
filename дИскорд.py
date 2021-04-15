import discord
import requests
import json
import math
from bs4 import BeautifulSoup

маты = ("мат", "блин", "глек", "дурак", "авенит", "жир", "пися", "*дурак*", "снюс")




client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    global маты

    if message.author == client.user:
        return
    print(message)

    if message.content.lower() == 'бот, скинь хентай':
        await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    @client.event
    async def on_member_join(members):
        for channel in members.guild.channels:
            if channel.name == "основной":
                await members.channel.send(f'Добро пожаловать {members}! !comНапиши  чтобы узнать мои команды.')



    for arr in маты:

        if message.content.lower() == arr:
            file = discord.File("котики.jpg", filename="котики.jpg")
            await message.channel.send("не ругайся!!11!1!1!", file=file)



    arrCommand = message.content.split(" ")


    if arrCommand[0].lower() == "погода":
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={' '.join(arrCommand[1:])}&appid=a6756a7aff9564a61122501b4ad92a9b")
        jsonData = json.loads(r.text)
        temp = math.floor(jsonData["main"]["temp"] - 273.15)
        await message.channel.send(f"{temp} °C {''.join(arrCommand[1])}")

    if message.content == "menu":
        r = requests.get("https://kurgan.shashlikoff.com/")
        bs = BeautifulSoup(r.text, "lxml")
        block = bs.find("section", attrs={"class":"row hits items"})
        for child in block.children:
            title = child.find("h3", attrs={"class": "item-title"})
            print(title.a.text)














    if message.content.lower() == 'бот, привет':
        await message.channel.send('прива))')

    if message.content.lower() == 'ку, жир':
        await message.channel.send('сам')

    if message.content.lower() == 'абоба':
        await message.channel.send('бан дурачку')

    if message.content.lower() == 'амогус':
        await message.channel.send('WHEN THE IMPOSTOR IS SUS')

    if message.content.lower() == "бот, как у тебя дела?":
        file = discord.File("котек.jpg", filename="котек.jpg")
        await message.channel.send("хорошо, только", file=file)

    if message.content.lower() == "бот, пока":
        file = discord.File("пока.png", filename="пока.png")
        await message.channel.send("давай", file=file)



client.run("ODI5NjczMzIyMjMzMDY5NTY4.YG7jfg.vgPRVRENriUTCmgJXPK2xpBztWw")