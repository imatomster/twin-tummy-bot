# Importing my security tokens to use the following APIS
from secret import TOKEN_DISCORD, TOKEN_RIOTWATCHER
import os
# Import discord and then the specific commands from extra discord
import discord
from discord.ext import commands
# Import riotwatcher
from riotwatcher import LolWatcher, ApiError
# Setting up LolWatcher (need to refresh every 24 hours)
watcher = LolWatcher(TOKEN_RIOTWATCHER)

# Import requests to get something from fox website
import requests, random

# Custom Bot Constructor for my Discord Bot
class twin_tummy(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='$')

    # async def on_ready(self):
    #     print('Online as', self.user)
    #     # print('self', dir(self)) to see all commands

# Instancing a Bot
bot_instance = twin_tummy()

# All Events
@bot_instance.event
async def on_ready():
    print('Online as', bot_instance.user)
    await bot_instance.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="CURTIS CUZ I LOVE YOU"))

# All Commands
@bot_instance.command(aliases=['TEST', 'TESTER'], help="I am just here to tell you if bot is working")
async def test(ctx):
    await ctx.send('Hey there! Yes, I am working')

@bot_instance.command(aliases=['HELLO', 'hi', 'HI'], help="I am just here to say hi")
async def hello(ctx):
    await ctx.trigger_typing()
    await ctx.reply('Hey bro')

@bot_instance.command(aliases=['trollSteben', 'steben', 'steven','FOX'], help="Did someone say steben?")
async def fox(ctx):
    picture = requests.get('http://randomfox.ca/floof').json()['image']
    discord_id = '<@383129219326017569>'
    await ctx.send(f'{discord_id}\n{picture}')

@bot_instance.command(aliases=['MEME'], help="Is today monday?")
async def meme(ctx):
    await ctx.trigger_typing()
    picture = requests.get('https://memeapi.pythonanywhere.com/').json()['memes'][0]['url']
    await ctx.send(f'Is today Monday?\n{picture}')

@bot_instance.command(help='This is not rickroll I promise')
async def rickroll(ctx):
    await ctx.send('https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983')

@bot_instance.command(help='Alexa Play despacito')
async def despacito(ctx):
    await ctx.send('https://www.youtube.com/watch?v=whwe0KD_rGw')

@bot_instance.command(aliases=['8ball', 'ASK', 'question'], help='I can predict the future')
async def ask(ctx, *, question):
    responses = ['It is certain :eyes:.',
                 'It is decidedly so :eyes:.',
                 'Without a doubt :eyes:.',
                 'Yes - definitely :eyes:',
                 'You may rely on it :eyes:',
                 'As I see it, yes :eyes:.',
                 'Most likely :eyes:',
                 'Outlook good :eyes:.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@bot_instance.command(aliases=['mmr', 'MMR', 'league', 'OP.GG', 'OPGG', 'op.gg'], help="League Summoner Search")
async def opgg(ctx, *, input):
    await ctx.trigger_typing()

    try:
        # Testing if summoner exists
        user = watcher.summoner.by_name('na1', input)
    except ApiError as errorVariable:
        # If it doesn't > ApiError 404 and we can respond
        print(errorVariable)
        await ctx.send(f'Are you sure {input} exists on the rift?')
    else:
        # Create User and Check Stats
        user = watcher.summoner.by_name('na1', input)
        stats = watcher.league.by_summoner('na1', user['id'])

        # Check if they have enough information for stats
        if len(stats) > 0: # The stats array will be empty if not enough games
            stats = stats[0]
            summonerName = stats['summonerName']
            tier = stats['tier']
            rank = stats['rank']
            lp = stats['leaguePoints']
            userLink = summonerName.replace(' ', '')
            await ctx.send(f'Username: {summonerName}\nRank: {tier} {rank} and {lp} lp \nFor more info: https://na.op.gg/summoner/userName={userLink}')
        else:
            summonerName = user['name']
            userLink = summonerName.replace(' ', '')
            await ctx.send(f'It seems that {summonerName} does not have a rank!\nFor more info: https://na.op.gg/summoner/userName={userLink}')

# Execute Instance
bot_instance.run(TOKEN_DISCORD)