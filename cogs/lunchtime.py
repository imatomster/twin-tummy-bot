import discord
from discord.ext import commands
# Import requests to get something from fox website
import requests
import random


class LunchTime(commands.Cog, name='Lunch Time Commands'):
    """Constructor for the cog"""

    def __init__(self, bot_instance):
        self.bot_instance = bot_instance

    @commands.command(aliases=['TEST', 'TESTER'], help="I am just here to tell you if bot is working")
    async def test(self, ctx):
        await ctx.send('Hey there! Yes, I am working')

    @commands.command(aliases=['HELLO', 'hi', 'HI'], help="I am just here to say hi")
    async def hello(self, ctx):
        await ctx.trigger_typing()
        await ctx.reply('Hey bro')

    @commands.command(aliases=['trollSteben', 'steben', 'steven', 'FOX'], help="Did someone say steben?")
    async def fox(self, ctx):
        picture = requests.get('http://randomfox.ca/floof').json()['image']
        discord_id = '<@383129219326017569>'
        await ctx.send(f'{discord_id}\n{picture}')

    @commands.command(aliases=['MEME'], help="Is today monday?")
    async def meme(self, ctx):
        await ctx.trigger_typing()
        picture = requests.get(
            'https://memeapi.pythonanywhere.com/').json()['memes'][0]['url']
        await ctx.send(f'Is today Monday?\n{picture}')

    @commands.command(help='This is not rickroll I promise')
    async def rickroll(self, ctx):
        await ctx.send('https://tenor.com/view/rick-astley-rick-roll-dancing-dance-moves-gif-14097983')

    @commands.command(help='Alexa Play despacito')
    async def despacito(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=whwe0KD_rGw')

    @commands.command(aliases=['8ball', 'ASK', 'question'], help='I can predict the future')
    async def ask(self, ctx, *, question):
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


def setup(bot_instance):
    """Adds Cog to Bot"""
    bot_instance.add_cog(LunchTime(bot_instance))
