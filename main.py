import os
import discord
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()





bot.run(os.getenv("DISCORD_TOKEN"))