import discord
from discord.ext import commands
# Importing my security tokens to use the following APIS
from ..secret import TOKEN_RIOTWATCHER

# Import riotwatcher
from riotwatcher import LolWatcher, ApiError
# Setting up LolWatcher (need to refresh every 24 hours)
watcher = LolWatcher(TOKEN_RIOTWATCHER)

class Riotwatcher(commands.Cog):
    """Constructor for the cog"""

    def __init__(self, bot_instance):
        self.bot_instance = bot_instance

    @commands.command(aliases=['TEST', 'TESTER'], help="I am just here to tell you if bot is working")
    async def test(self, ctx):
        await ctx.send('Hey there! Yes, I am working')

    @commands.command(aliases=['mmr', 'MMR', 'league', 'OP.GG', 'OPGG', 'op.gg'], help="League Summoner Search")
    async def opgg(self, ctx, *, input):
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

def setup(bot_instance):
    """Adds Cog to Bot"""
    bot_instance.add_cog(Riotwatcher(bot_instance))
