import discord
from discord.ext import commands

# Set up the bot
bot = commands.Bot(command_prefix="!")

# When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# A simple command that responds with "Hello, World!"
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, World!")

# Run the bot
bot.run("YOUR_BOT_TOKEN")
