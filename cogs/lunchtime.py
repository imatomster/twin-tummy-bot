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
        responses = ['Michael says yes :turtle:',
                     'Ethan decides yes :eyes:',
                     'Curtis has no doubts :coconut:',
                     'Courtney says definitely yes :rocket:',
                     'As Tummy sees it, yes :eye: :lips: :eye:',
                     'If a girl asked this then Fernando says yes  :eyes:',

                     'Gohnshein shakes his head in disapproval:airplane:',
                     'Chicken says no :chicken:',
                     'Isa no for me :deciduous_tree:',
                     'My next line is\nNO :custard:',
                     'Cap thinks outlook bad :kaaba:  ',
                     'Owen says no like the negative pers... ok ok sorry I was joking :eyes:',

                     'No hablo ingles, por favor espanol :eye: :lips: :eye:',
                     'That question is wayyy too hard :eye: :lips: :eye:',
                     'One second, Tommy is pooping :eyes:',
                     'Chicken does not want to talk right now :chicken:',
                     'Tummy is very doubtful :eye: :lips: :eye:',
                     'I think Tommy has the answers :face_with_raised_eyebrow:']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(bot_instance):
    """Adds Cog to Bot"""
    bot_instance.add_cog(LunchTime(bot_instance))
