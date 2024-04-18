
# This example requires the 'message_content' intent.

import discord
import asyncio
from discord.ext import commands, tasks
from discord import app_commands
from discord.ext import commands
import typing

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



#ban
#Replace 'your_bot_token' with your actual bot token


client = discord.Client(intents=intents)
# Create a bot instance with intents and a command prefix


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


 


#send

client = discord.Client(intents=intents)

async def send_message():
    await client.wait_until_ready()
    channel = client.get_channel(1203941108808425505)  # Replace YOUR_CHANNEL_ID with your channel ID

    while not client.is_closed():
        await channel.send('This is a message sent every 1 minute!')
        await asyncio.sleep(300)  # Sleep for 60 seconds (1 minute)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(send_message())

        




        


client.run('MTIwNDQyMTYyMzU4Mzg3NTA3Mw.GS5Heb.V8ZdbUyFwkYcFzdbheAjg7PbpDOWv2V5W28wAA')
