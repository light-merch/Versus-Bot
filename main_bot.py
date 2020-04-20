import discord
from discord.ext import commands

import chain as ch
from my_token import discord_token 
from battle_parser import get_lyrics


# TODO add explict
# TODO save to file
EXPLICT = dict() # show explict content
REGISTERED = []  # list of joined people
RAPPERS = []     # all rappers parsed

def test(user_id):
    return user_id in REGISTERED


def read_data():
    with open('artists.txt', 'r') as f:
        RAPPERS = f.read().split(';')


client = discord.Client()
bot = commands.Bot(command_prefix='vs ')


@bot.event
async def on_ready():
    print('Started!')
    read_data()
    game = discord.Game("GTA Online")
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command(pass_context=True)
async def start(ctx):
    if ctx.author.id in REGISTERED:
        await ctx.send('Already registed')
        return

    EXPLICT[ctx.author.id] = False
    REGISTERED.append(ctx.author.id)

    await ctx.send('Registed')




@bot.command(pass_context=True)
async def punch(ctx):
    if test(ctx.author.id):
        await ctx.send(ch.SendPunch().capitalize() )
    else:
        await ctx.send('Please register by typing <vs start>')


@bot.command(pass_context=True)
async def rappers(ctx):
    if test(ctx.author.id):
        await ctx.send(' '.join(RAPPERS))
    else:
        await ctx.send('Please register by typing <vs start>')


# TODO: write always corect artist name to file 
@bot.command(pass_context=True)
async def add(ctx, arg):
    if test(ctx.author.id):
        if arg in RAPPERS:
            await ctx.send('There is already this rapper in our dataset. See <vs rappers> for more')

        await ctx.send('Started parsing songs')
        get_lyrics(arg)
        RAPPERS.append(arg)
        await ctx.send('Done. See <vs rappers> to choose new rapper')
    else:
        await ctx.send('Please register by typing <vs start>')


@bot.command(pass_context=True)
async def explict(ctx):
    if test(ctx.author.id):
        if EXPLICT[ctx.author.id]:
            EXPLICT[ctx.author.id] = False
        else:
            EXPLICT[ctx.author.id] = True

        ans = f'Explict content set to ' + ['show', 'hide'][not EXPLICT[ctx.author.id]]
        await ctx.send(ans)
    else:
        await ctx.send('Please register by typing <vs start>')


@bot.command(pass_context=True)
async def func(ctx):
    if test(ctx.author.id):
        await ctx.send()
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
