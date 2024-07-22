import discord
from discord.ext import commands

from kodland_utils import *
import os, random
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send(pass_gen(10))

@bot.command()
async def subject(ctx):
    await ctx.send(subject_selector())

@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def meme(ctx):
    selected = random.choice(os. listdir('images'))
    with open(f'images/{selected}', 'rb') as f:
        pictures = discord.File(f)
    await ctx.send(file=pictures)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# Daftar Sampah

Organik = ['sayur busuk', 'makanan basi', 'kotoran hewan']
Kertas = ['kardus', 'kertas gorengan', 'paperbag', 'kertas', 'origami']
Plastik = ['kresek', 'kardus', 'botol plastik']
Logam = ['kaleng', 'baterai', 'hp', 'kabel', 'baut', 'besi', 'seng', 'tembaga']

@bot.command()
async def tanya_sampah(ctx):
    await ctx.send('apa sampah yang ingin anda periksa?')
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)

    # pengecekan
    if message.lower() in Organik:
        await ctx.send('That is an Organic trash, blud')
        await ctx.send('You better recycle it')
    elif message.lower() in Kertas:
        await ctx.send('It is a paper trash, did not you learn that in school')
        await ctx.send('Lets turn it into a miniature?')
    elif message.lower() in Plastik:
        await ctx.send('That is plastic trash, bruh is not that obvious?')
        await ctx.send('If we make a flower vase from it, would not it be beautiful?')
    elif message.lower() in Logam:
        await ctx.send('It is a metal trash')
        await ctx.send('Never bury this!')
    else:
        await ctx.send('That is not a trash please...')
