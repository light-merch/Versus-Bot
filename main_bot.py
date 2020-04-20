import discord
from discord.ext import commands

from my_token import discord_token 

client = discord.Client()
bot = commands.Bot(command_prefix='vs ')

# messages = await channel.history(limit=123).flatten()
# print(messages)
# messages is now a list of Message...

@bot.event
async def on_ready():
    print('Ready!')
    game = discord.Game("GTA Online")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command(pass_context=True) # разрешаем передавать агрументы
async def test(ctx, arg): # создаем асинхронную фунцию бота
    await ctx.send(arg) # отправляем обратно аргумент

@bot.command(pass_context=True)
async def punch(ctx):
    await ctx.send('punch')

@bot.command(pass_context=True)
async def artists(ctx):
    with open('battle-mc/artists', 'r')
    await ctx.send('')

@bot.command(pass_context=True)
async def add_artists(ctx):
    with open('battle-mc/artists', 'r')
    await ctx.send('')

bot.run(discord_token)
