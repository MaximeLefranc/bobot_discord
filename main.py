import discord

from utils.get_environment import BOT_TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('The Bot is ready!')


@client.event
async def on_message(message: discord.Message):
    if message.content.lower() == 'ping':
        await message.channel.send('pong', delete_after=5)


@client.event
async def on_member_join(member: discord.Member):
    if isinstance(general_channel := client.get_channel(1176513829904056321), discord.TextChannel):
        await general_channel.send(f'Bienvenue sur le serveur {member.display_name}!')


if BOT_TOKEN:
    client.run(BOT_TOKEN)
else:
    print('BOT_TOKEN in .env file can\'t be empty')
