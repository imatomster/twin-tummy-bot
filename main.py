# Import OS to refer to filename
import os
# Import discord to run the bot
import discord
from discord.ext import commands
# Importing Discord Token from .env File
from dotenv import load_dotenv
load_dotenv()
TOKEN_DISCORD = os.getenv('TOKEN_DISCORD')


class twin_tummy(commands.Bot):
    """Custom Bot Constructor for my Discord Bot"""

    def __init__(self):
        super().__init__(command_prefix='.')

    # async def on_ready(self):
    #     print('Online as', self.user)
    #     # print('self', dir(self)) to see all commands


# Instancing a Bot
bot_instance = twin_tummy()


@bot_instance.event
async def on_ready():
    """On ready to set status message"""
    print(f'Online as {bot_instance.user}')
    await bot_instance.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Tommy from his room'))


@bot_instance.command(help='Turn on a certain feature in a server')
async def load(ctx, extension):
    """Turn on certain cogs on certain servers (you would type .load 'cogname' on a discord server)"""
    bot_instance.load_extension(f'cogs.{extension}')


@bot_instance.command(help='Turn off a certain feature in a server')
async def unload(ctx, extension):
    """Turn off certain cogs on certain servers (you would type .unload 'cogname' on a discord server)"""
    bot_instance.unload_extension(f'cogs.{extension}')

# Load all Files in the Cog Folder
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        # file[:-3] shaves off .py or the last 3 characters
        bot_instance.load_extension(f'cogs.{file[:-3]}')

# Execute Instance
bot_instance.run(TOKEN_DISCORD)
