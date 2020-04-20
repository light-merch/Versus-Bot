import discord
from discord.ext import commands

import chain as ch
from my_token import discord_token 


# TODO save to file
EXPLICT = dict() # show explict content
LANG = dict() # language
REGISTERED = []

client = discord.Client()
bot = commands.Bot(command_prefix='vs ')

def test(user_id):
    return user_id in REGISTERED


@bot.event
async def on_ready():
    print('started')
    game = discord.Game("GTA Online")
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command(pass_context=True)
async def start(ctx):
    if ctx.author.id in REGISTERED:
        await ctx.send('Already registed')

    EXPLICT[ctx.author.id] = True
    LANG[ctx.author.id] = 'English'

    REGISTERED.append(ctx.author.id)
    await ctx.send('Registed')




@bot.command(pass_context=True)
async def punch(ctx):
    if test(ctx.author.id):
        await ctx.send(ch.SendPunch())
    else:
        await ctx.send('Please register by typing <vs start>')


@bot.command(pass_context=True)
async def rappers(ctx):
    if test(ctx.author.id):
        with open('battle-mc/artists.txt', 'r') as f:
            await ctx.send(f.read())
    else:
        await ctx.send('Please register by typing <vs start>')


@bot.command(pass_context=True)
async def add(ctx):
    if test(ctx.author.id):
        with open('battle-mc/artists', 'r'):
            await ctx.send('')
    else:
        await ctx.send('Please register by typing <vs start>')


@bot.command(pass_context=True)
async def explit(ctx):
    if test(ctx.author.id):
        await ctx.send('')
    else:
        await ctx.send('Please register by typing <vs start>')


@bot.command(pass_context=True)
async def lang(ctx):
    if test(ctx.author.id):
        await ctx.send(LANG[ctx.author.id])
    else:
        await ctx.send('Please register by typing <vs start>')


@bot.command(pass_context=True)
async def reg(ctx):
    if test(ctx.author.id):
        await ctx.send(REGISTERED)
        return
    else:
        await ctx.send('Please register by typing <vs start>')


bot.run(discord_token)
