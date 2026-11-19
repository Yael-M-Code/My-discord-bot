import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()
token = os.getenv("TOKEN")


# Command Part

@bot.slash_command(name ="presentation", description="Present who I am and what's my purpose")
async def presentation(ctx):
    embed = discord.Embed(title="This is my own presentation 🎤!", color=discord.Color.blue())
    embed.add_field(name="Who am I", value="I'm Frodo, a new discord bot made with ❤️", inline=True) 
    embed.add_field(name="My purpose", value="To be fair with you, the goal of this bot is only improving my python. I found it very fun to make and really increase my skill, thank u HackClub! 🤖", inline=True)
    embed.set_footer(text="If you are reading that, I hope you will pass a great day")
    await ctx. respond (embed=embed)






# The best part, RUNNING THE BOT !!!
bot.run(token)