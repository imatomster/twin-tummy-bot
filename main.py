# Importing my security tokens to use the following APIS
from secret import TOKEN_DISCORD, TOKEN_RIOTWATCHER

# Import discord and then the specific commands from extra discord
from discord.ext import commands
# Import riotwatcher
from riotwatcher import LolWatcher, ApiError

# Setting up LolWatcher (need to refresh every 24 hours)
watcher = LolWatcher(TOKEN_RIOTWATCHER)

# Custom Bot Constructor for my Discord Bot
class twin_tummy(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='/')

    async def on_ready(self):
        # on launch > tell console that I launched
        print('Online as', self.user)
        # print('self', dir(self)) to see all commands

# Instancing a Bot
bot_instance = twin_tummy()

# All Commands
@bot_instance.command(aliases=['TEST', 'TESTER'], help="I am just here to tell you if bot is working")
async def test(ctx):
    await ctx.send('Hey there! Yes, I am working')

@bot_instance.command(aliases=['HELLO', 'hi', 'HI'], help="I am just here to say hi")
async def hello(ctx):
    await ctx.trigger_typing()
    await ctx.reply('Hey bro')

# Aliases not working
@bot_instance.command(aliases=['mmr, MMR, league, OP.GG, OPGG, op.gg'], help="League Summoner Search")
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