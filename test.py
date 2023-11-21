import discord
from discord.ext import commands

from utils.get_environment import BOT_TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def test(ctx):
    print('je suis dans la commande')


if BOT_TOKEN:
    bot.run(BOT_TOKEN)
else:
    print('BOT_TOKEN in .env file can\'t be empty')
