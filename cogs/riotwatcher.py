from riotwatcher import LolWatcher, ApiError
import discord
from discord.ext import commands, tasks
# Importing Riotwatcher Token from .env File
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN_RIOTWATCHER = os.getenv('TOKEN_RIOTWATCHER')

# Setting up LolWatcher (need to refresh every 24 hours)
watcher = LolWatcher(TOKEN_RIOTWATCHER)


class RiotWatcher(commands.Cog, name='League of Legends Commands'):
    """Constructor for the cog"""

    def __init__(self, bot_instance):
        self.bot_instance = bot_instance
        # Start the Background Task Checkers
        self.check_match.start()

    @commands.command(aliases=['mmr', 'MMR', 'league', 'OP.GG', 'OPGG', 'op.gg'], help="Search someone's op.gg or rank")
    async def opgg(self, ctx, *, input):
        await ctx.trigger_typing()

        try:
            # Testing if summoner exists
            user = watcher.summoner.by_name('na1', input)
        except ApiError as error_variable:
            # If it doesn't > ApiError 404 and we can respond
            print(error_variable)
            if error_variable.response.status_code == 404:
                await ctx.send(f'Are you sure "{input}" exists on the rift?')
        else:
            # Create User and Check Stats
            stats = watcher.league.by_summoner('na1', user['id'])

            # Check if they have enough information for stats
            if len(stats) > 0:  # The stats array will be empty if not enough games
                stats = stats[0]
                summoner_name = stats['summonerName']
                tier = stats['tier']
                rank = stats['rank']
                lp = stats['leaguePoints']
                user_link = summoner_name.replace(' ', '')
                await ctx.send(f'Username: {summoner_name}\nRank: {tier} {rank} and {lp} lp \nFor more info: https://na.op.gg/summoner/userName={user_link}')
            else:
                summoner_name = user['name']
                user_link = summoner_name.replace(' ', '')
                await ctx.send(f'It seems that "{summoner_name}" does not have a rank!\nFor more info: https://na.op.gg/summoner/userName={user_link}')

    @commands.command(aliases=['check', 'ingame'], help="Check if someone is ingame")
    async def spectate(self, ctx, *, input):
        await ctx.trigger_typing()

        try:
            # Testing if summoner exists
            user = watcher.summoner.by_name('na1', input)
        except ApiError as error_variable:
            # If it doesn't > ApiError 404 and we can respond
            print(error_variable)
            if error_variable.response.status_code == 404:
                await ctx.send(f'Are you sure "{input}" exists on the rift?')
        else:
            # Create User
            user = watcher.summoner.by_name('na1', input)
            summoner_name = user['name']

            # Check if in game
            try:
                spectator = watcher.spectator.by_summoner('na1', user['id'])
            except ApiError as error_variable:
                print(error_variable)
                if error_variable.response.status_code == 404:
                    await ctx.send(f'It seems like "{summoner_name}" is not ingame right now')
            else:
                user_link = summoner_name.replace(' ', '')
                game_length = spectator['gameLength'] + 180
                await ctx.send(f'"{summoner_name}" is {game_length//60} minutes & {game_length%60} seconds ingame right now!\nCheck them out here: https://na.op.gg/summoner/userName={user_link}')
                print(spectator)
                

    @tasks.loop(seconds=10, count=1)
    async def check_match(self):
        """Background Task"""
        print("hi")

    @check_match.before_loop
    async def before_check_match(self):
        """Not Running Task until bot_instance is loaded"""
        print('Waiting before looping...')
        await self.bot_instance.wait_until_ready()

    @check_match.after_loop
    async def after_check_match(self):
        """Declaring that Loop is done"""
        print('Done!')


def setup(bot_instance):
    """Adds Cog to Bot"""
    bot_instance.add_cog(RiotWatcher(bot_instance))
