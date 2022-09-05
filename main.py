import discord
from discord.ext import commands
from decouple import config

from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

TOKEN = (config("TOKEN"))

bot.run(TOKEN)
