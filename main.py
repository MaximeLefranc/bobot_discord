import discord

from utils.get_environment import BOT_TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('The Bot is ready!')


@client.event
async def on_message(message):
    if message.content.lower() == 'ping':
        await message.channel.send('pong', delete_after=5)

if BOT_TOKEN:
    client.run(BOT_TOKEN)
else:
    print('BOT_TOKEN in .env file can\'t be empty')
