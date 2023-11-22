from __future__ import annotations
from dataclasses import dataclass

import discord
from discord.ext import commands

from utils.get_environment import BOT_TOKEN, GENERAL_ID_CHANNEL


@dataclass
class MaxBot(commands.Bot):
    intents: discord.flags.Intents = discord.Intents.all()

    def __post_init__(self: MaxBot):
        super().__init__(command_prefix='!', intents=self.intents)

    async def on_ready(self: MaxBot):
        print(f'{self.user.display_name} is connected to server.')  # type: ignore

    async def on_message(self: MaxBot, message: discord.Message):
        if message.content.lower() == 'ping':
            await message.channel.send('pong', delete_after=5)
        await self.process_commands(message)

    async def on_member_join(self: MaxBot, member: discord.Member):
        if GENERAL_ID_CHANNEL and isinstance(general_channel := self.get_channel(int(GENERAL_ID_CHANNEL)), discord.TextChannel):
            await general_channel.send(f'Bienvenue sur le serveur {member.display_name}!')


max_bot = MaxBot()


@max_bot.command(name='del')
async def delete_messages(ctx: commands.Context, number_of_messages: int = 0):
    counter = 0
    async for message in ctx.channel.history(limit=number_of_messages + 1):
        if ctx.author == message.author and counter <= number_of_messages:
            await message.delete()
            counter += 1

if BOT_TOKEN:
    # bot.run(BOT_TOKEN)
    max_bot.run(BOT_TOKEN)
else:
    print('BOT_TOKEN in .env file can\'t be empty')
