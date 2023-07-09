import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

token = os.getenv("TOKEN")

# Create the Discord bot instance with required intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix="!", intents=intents)

# Event handler for when the bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")  # Print bot's username
    print(f"Bot ID: {bot.user.id}")  # Print bot's ID
    print("------")

# Example command: !ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot using your bot token
bot.run(token)
