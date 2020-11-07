#bot.py
import os
import discord
import random
import datetime
from discord import File

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    words="shut frick up"
    author=str(message.author)
    badWords=["gamer","gaming","pog","pogchamp","poggers","league","legends","games","game", "among", "sus"]
    userWords=message.content
    for i in badWords:
        if i in userWords.lower():
            response=words+" @"+author
            await message.channel.send(response)
            return

    if message.content.startswith('$name'):
        await message.channel.send('Your name is:')
        await message.channel.send(message.author)
    if "$time" in message.content:
        now = datetime.datetime.now()
        await message.channel.send('The current date and time is:')
        await message.channel.send(now)
    if message.content.startswith('$hello'):
        helloMsg = random.choice(["Hello", "Bongiorno", "Bonjour", "اسلام عليكم", "Hola"])
        await message.channel.send(helloMsg)
    if message.content.startswith('$deny'):
        noMessage = random.choice(["Hell no", "Shhhh", "No", "Quiet", "Negative"])
        await message.channel.send(noMessage)
    if message.content.startswith('$agree'):
        yesMessage = random.choice(["Sure", "Yes", "Why not", "Hell yeah", "Positive"])
        await message.channel.send(yesMessage)
    if message.content.startswith('$bruh'):
        photoDir = "bruhFolder"
        photo = random.choice(os.listdir(photoDir))
        await message.channel.send(file=discord.File(photo))


    if "@everyone" in message.content:
        now = datetime.datetime.now()
        now = now.replace(second = 0, microsecond = 0)
        author : discord.Member= message.author
        await author.kick(reason = "shut frick up")
        await message.channel.send(":skull: Rest In Peace :skull:") 
        await message.channel.send(author.avatar_url)
        await message.channel.send(message.author)
        await message.channel.send('Time of death:')
        await message.channel.send(now)
        await message.channel.send("They sorta deserved it though")

client.run('INSERT TOKEN HERE')




