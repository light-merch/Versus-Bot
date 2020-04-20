import discord
from discord.ext import commands

from my_token import discord_token 

bot = commands.Bot(command_prefix='vs ')
activity = discord.Game(name="with the API")


@bot.command(pass_context=True) # разрешаем передавать агрументы
async def test(ctx, arg): # создаем асинхронную фунцию бота
    await ctx.send(arg) # отправляем обратно аргумент

bot.run(discord_token)
