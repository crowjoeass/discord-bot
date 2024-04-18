import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hello, Do you need any help?(Yes/No)')
    if message.content.startswith('hello'):
        await message.channel.send('hello, Do you need any help?(Yes/No)')
    if message.content.startswith('Hi'):
        await message.channel.send('Hi!, Do you need any help?(Yes/No)')
    if message.content.startswith('Yes'):
        await message.channel.send('Ok, clearly state what assistance you need then you will be guided by the MODERATORS')
    if message.content.startswith('yes'):
        await message.channel.send('Ok, clearly state what assistance you need then you will be guided by the MODERATORS')
    if message.content.startswith('No'):
        await message.channel.send('Ok, feel welcomed in the server and famiiarize yourself wit the server rules')
    if message.content.startswith('no'):
        await message.channel.send('Ok, feel welcomed in the server and famiiarize yourself wit the server rules')

        if message.content.lower().startswith('hey'):
            await message.channel.send('Hey there! Need help with something? (Yes/No)')
        elif message.content.lower().startswith('good morning'):
            await message.channel.send('Good morning! How can I assist you today? (Yes/No)')
        elif message.content.lower().startswith('good afternoon'):
            await message.channel.send('Good afternoon! Looking for some help? (Yes/No)')
        elif message.content.lower().startswith('good evening'):
            await message.channel.send('Good evening! How can I be of service? (Yes/No)')


        elif 'how do i' in message.content.lower():
            await message.channel.send(
                'It seems you have a specific question. Could you please provide more details so the MODERATORS can assist you?')
        elif 'info' in message.content.lower() or 'information' in message.content.lower():
            await message.channel.send('Sure, what information are you looking for? Please be as specific as possible.')


        elif message.content.lower().startswith('thank you') or message.content.lower().startswith('thanks'):
            await message.channel.send('You\'re welcome! If you have any more questions, feel free to ask.')


        elif message.content.lower().startswith('what else') or message.content.lower().startswith('anything else'):
            await message.channel.send(
                'Is there anything else I can help you with? Feel free to ask any questions or for assistance on specific topics.')


        elif 'bye' in message.content.lower() or 'goodbye' in message.content.lower():
            await message.channel.send(
                'Goodbye! Don’t hesitate to return if you have more questions in the future. Have a great day!')

       
        else:
            await message.channel.send(
                'I\'m not sure how to respond to that. Could you ask something else, or specify if you need help? (Yes/No)')


client.run('MTIwNDQyMTYyMzU4Mzg3NTA3Mw.GS5Heb.V8ZdbUyFwkYcFzdbheAjg7PbpDOWv2V5W28wAA')