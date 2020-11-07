#ShabzBot.py
import os
import discord
import random
import datetime
from discord import File

client = discord.Client()
transformersTerms = ["optimus","prime","autobot","decepticon","robot","transform","megatron"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$name'):
        await message.channel.send('Your name is:')
        await message.channel.send(message.author)
    if "$time" in message.content:
        now = datetime.datetime.now()
        await message.channel.send('The current date and time is:')
        await message.channel.send(now)
    if message.content.startswith('hello'):
        await message.channel.send('hello')
    if message.content.startswith('$hello'):
        helloMsg = random.choice(["Hello", "Bongiorno", "Bonjour", "اسلام عليكم", "Hola"])
        await message.channel.send(helloMsg)
    if message.content.startswith('$deny'):
        noMessage = random.choice(["Hell no", "Shhhh", "No", "Quiet", "Negative"])
        await message.channel.send(noMessage)
    if message.content.startswith('$bruh'):
        photoDir = "imageFolder"
        photo = random.choice(os.listdir(photoDir))
        await message.channel.send(file=discord.File(photo))
    for term in transformersTerms:
        if term in message.content.lower():
            await message.channel.send("Transformers is a great movie!")

client.run('YOUR TOKEN HERE: DO NOT UPLOAD TOKEN TO GITHUB. WE WILL ATTACH THE TOKEN BEFORE SENDING THE FILES')
