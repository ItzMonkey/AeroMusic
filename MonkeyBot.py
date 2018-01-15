import discord
from discord.ext import commands
from discord.voice_client import VoiceClient


startup_extensions = ["Music"]
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print("Bot online")

class Main_Commands():
    def __init__(self, bot):
     self.bot = bot

     
#botDM
#@bot.command(pass_context = True)
#async def dm(ctx, member : discord.Member, *, content: str):
    #await bot.send_message(member, content)

	 
#Ping
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong")
    
#purge
#@bot.command(pass_context=True)
#async def purge(context, number : int):
	#"""Clear a specified number of messages in the chat"""
	#deleted = await bot.purge_from(context.message.channel, limit=number)
	#await bot.send_message(context.message.channel, 'Deleted {} message(s)'.format(len(deleted)))
	
#Shows id of rolls
#@bot.command(pass_context=True)
#async def roles(context):
	#"""Displays all of the roles with their ids"""
	#roles = context.message.server.roles
	#result = "The roles are "
	#for role in roles:
		#result += role.name + ": " + role.id + ", "
	#await bot.say(result)

	

#info   
@bot.command(pass_context=True)
async def Info(ctx):
    embed = discord.Embed(title="Made by ItzMonkey", description="Version 1.0", color=0x00ff00)
    embed.set_footer(text="Any questions about this bot DM me Monkey#5620")
    embed.set_author(name="AeroBot")
    embed.add_field(name="What can this bot do?", value="This bot was made to play some DANK Tunes", inline=True)
    await bot.say(embed=embed)

#Wave
@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("Hi :wave:")
#Kick
#@bot.command(pass_context = True)
#async def kick(ctx, userName: discord.User):
    #await bot.kick(userName)
    #await bot.say("__**Successfully User Has Been Kicked!**__")



if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load Extension {}\n{}'.format(extension, exc))

bot.run("NDAyMzU4OTcwNzk2MjEyMjI0.DT3luw.CpW6y7u6vtY6eKQjOsBDVdkmiqA")
