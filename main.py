import discord
from discord.ext import commands

from utils.get_environment import BOT_TOKEN, GENERAL_ID_CHANNEL

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='del')
async def delete_messages(ctx: commands.Context, number_of_messages: int = 0):
    counter = 0
    async for message in ctx.channel.history(limit=number_of_messages + 1):
        if ctx.author == message.author and counter < number_of_messages:
            await message.delete()
            counter += 1


@bot.event
async def on_ready():
    print("The Bot is Ready !")


@bot.event
async def on_message(message: discord.Message):
    if message.content.lower() == 'ping':
        await message.channel.send('pong', delete_after=5)
    await bot.process_commands(message)


@bot.event
async def on_member_join(member: discord.Member):
    if GENERAL_ID_CHANNEL and isinstance(general_channel := bot.get_channel(int(GENERAL_ID_CHANNEL)), discord.TextChannel):
        await general_channel.send(f'Bienvenue sur le serveur {member.display_name}!')


if BOT_TOKEN:
    bot.run(BOT_TOKEN)
else:
    print('BOT_TOKEN in .env file can\'t be empty')
