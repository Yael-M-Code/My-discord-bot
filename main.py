import discord
import os # default module
from dotenv import load_dotenv

load_dotenv("token.env") # load all the variables from the env file
bot = discord.Bot(intents=discord.Intents.all())
token = os.getenv("TOKEN")

# Command Part

@bot.slash_command(name ="presentation", description="Present who I am and what's my purpose")
async def presentation(ctx):
    embed = discord.Embed(title="This is my own presentation 🎤!", color=discord.Color.orange())
    embed.add_field(name="Who am I", value="I'm a simple ring, and a new discord bot made with ❤️") 
    embed.add_field(name="My purpose", value="To be fair with you, the goal of this bot is only improving my python. I found it very fun to make and really increase my skill, thank u HackClub! 🤖")
    embed.add_field(name="Who made it", value="My creator is a 15 (almost 16) y/o teenager in France, after switching language every 2 weeks: he found peace in python by learning complex notion with easy syntax!")
    embed.set_footer(text="If you are reading that, I hope you will pass a great day")
    await ctx.respond(embed=embed)


moderation = bot.create_group("moderation", "All commands to moderate your server")
@moderation.command(name="ban", description="Ban a member, THIS ACTION IS IMPORTANT, to unban: /unban")
@discord.option("member", discord.Member, description="The person who will be banned", required=True)
@discord.option("reason", str, description="Explain why youu want to ban this user", default="No reason given")
@discord.default_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, reason: str):
    await ctx.respond(f"🔍 I'm trying to ban *{member}*")
    await member.ban(reason=reason)
    await ctx.respond(f"✅ All good, **{member}** is banned")


# Event Part
@bot.event

#async def on_member_join(member):
#    welcomeRoom = member.guild.system_channel
#    embed = discord.Embed(title="A plane just land 🛩️", description="You saw that, an embed !", color=discord.Color.blurple())
#    embed.add_field(value=f"Welcome here {member.mention}, here is some information about your invitation:...")
#
# 
#    used = invite
#    embed.add_field(name="You come from", value=f"https://discord.gg/ {discord.used.code}", inline=True)
#    embed.add_field(name="Link made by", value=f"{discord.used(inviter)}, thank you!", inline=True)
#    embed.add_field(name="That have ", value=f"{discord.used(uses)} invites on this server!", inline=True)
#
#    embed.set_thumbnail(url=member.display_avatar.url)
#    await welcomeRoom.send(embed=embed)


async def on_ready():
    ping = round(bot.latency * 1000)
    channel = bot.get_channel(1573272525234774126)
    await channel.send(f"I'm __*ready*__ and __*online*__ with a latence of **{ping} ms** ")
    




# The best part, RUNNING THE BOT !!!
bot.run(token)