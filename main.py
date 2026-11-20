import discord
import os # default module
from dotenv import load_dotenv

load_dotenv("token.env") # load all the variables from the env file
bot = discord.Bot()
token = os.getenv("TOKEN")


# Command Part

@bot.slash_command(name ="presentation", description="Present who I am and what's my purpose")
async def presentation(ctx):
    embed = discord.Embed(title="This is my own presentation 🎤!", color=discord.Color.orange())
    embed.add_field(name="Who am I", value="I'm a simple ring, and a new discord bot made with ❤️", inline=False) 
    embed.add_field(name="My purpose", value="To be fair with you, the goal of this bot is only improving my python. I found it very fun to make and really increase my skill, thank u HackClub! 🤖", inline=False)
    embed.add_field(name="Who made it", value="My creator is a 15 (almost 16) y/o teenager in France, after switching language every 2 weeks: he found peace in python by learning complex notion with easy syntax!", inline=False)
    embed.set_footer(text="If you are reading that, I hope you will pass a great day")
    await ctx. respond (embed=embed)






# The best part, RUNNING THE BOT !!!
bot.run(token)