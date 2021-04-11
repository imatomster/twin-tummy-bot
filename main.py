from secret import TOKEN
import discord
from discord.ext import commands

class EatFartDrink(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='/')

    async def on_ready(self):
        # on launch > tell console that I launched
        print('Online as', self.user)
        print('self', dir(self))
    
bot_instance = EatFartDrink()

@bot_instance.command(aliases=['TEST', 'TESTER'], help="I am just here to tell you if bot is working")
async def test(ctx):
    await ctx.reply('Hey there! Yes, I am working')

@bot_instance.command(aliases=['hi', 'HELLO'], help="I am just here to say hi")
async def hello(ctx):
    await ctx.trigger_typing()
    await ctx.send('Hey bro')

bot_instance.run(TOKEN)