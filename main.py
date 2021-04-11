# Importing my security tokens to use the following APIS
from secret import TOKEN_DISCORD, TOKEN_RIOTWATCHER

# Import discord and then the specific commands from extra discord
from discord.ext import commands
# Import riotwatcher
from riotwatcher import LolWatcher, ApiError

# Setting up LolWatcher (need to refresh every 24 hours)
watcher = LolWatcher(TOKEN_RIOTWATCHER)

# Custom Bot Constructor for my Discord Bot
class DrinkEatFart(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='/')

    async def on_ready(self):
        # on launch > tell console that I launched
        print('Online as', self.user)
        # print('self', dir(self))

# Instancing a Bot
bot_instance = DrinkEatFart()

# All Commands
@bot_instance.command(aliases=['TEST', 'TESTER'], help="I am just here to tell you if bot is working")
async def test(ctx):
    await ctx.reply('Hey there! Yes, I am working')

@bot_instance.command(aliases=['HELLO', 'hi', 'HI'], help="I am just here to say hi")
async def hello(ctx):
    await ctx.trigger_typing()
    await ctx.send('Hey bro')

@bot_instance.command(aliases=['mmr, MMR, league, OP.GG, OPGG, op.gg'], help="League Summoner Search")
async def opgg(ctx, *, input):
    await ctx.trigger_typing()

    try:
        user = watcher.summoner.by_name('na1', input)
    except ApiError as err:
        await ctx.send(f'Sorry bro but something wrong with {input}')
    else:
        user = watcher.summoner.by_name('na1', input) 
        stats = watcher.league.by_summoner('na1', user['id'])[0]
        summonerName = stats['summonerName']
        tier = stats['tier']
        rank = stats['rank']
        lp = stats['leaguePoints']
        await ctx.send(f'Username: {summonerName}\nRank: {tier} {rank} and {lp} lp')

# Execute Instance
bot_instance.run(TOKEN_DISCORD)