# <----        Importing moduels                        ---->
import os
import discord
from dotenv import load_dotenv
import random
import json

# <----        Reading Token key from dotenv file       ---->
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# <----        Import json dictionary                   ---->


client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to :popcorn: Talks'
    )

# <----        Load list of quotes                     ---->
with open('famous_people_quotes.json') as quotes:
    quotes_list = json.load(quotes)

with open('inspirational_quotes.json') as moti:
    motivation_list = json.load(moti)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elon_musk = quotes_list['Elon Musk']
    steve_jobs = quotes_list['Steve Jobs']
    lao_tzu = quotes_list['Lao Tzu']
    motivation = motivation_list['motivation']
    user_input = motivation_list['user_input']

    if message.content.lower() == 'elon musk':
        response = random.choice(elon_musk)
        await message.channel.send(':popcorn:  ' + response)

    if message.content.lower() == 'steve jobs':
        response = random.choice(steve_jobs)
        await message.channel.send(':popcorn:  ' + response)

    if message.content.lower() == 'lao tzu':
        response = random.choice(lao_tzu)
        await message.channel.send(':popcorn:  ' + response)

    if message.content.lower() in user_input:
        response = random.choice(motivation)
        await message.channel.send(':popcorn:  ' + response)




client.run(TOKEN)

