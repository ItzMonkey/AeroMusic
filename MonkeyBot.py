import discord
import asyncio
from discord.ext import commands
from discord.voice_client import VoiceClient
client = discord.Client()

startup_extensions = ["Music"]
bot = commands.Bot("?")

class Main_commands():
        def __init__(self, bot):
         self.bot = bot

@client.event
async def on_ready():
        print("Logged in as:")
        print(client.user.name)
        print("ID:")
        print(client.user.id)
        print("Ready to use!")

@client.event
async def on_message(message):
    if  message.author == client.user:
        return
    elif message.content.startswith("!ping"):
        await client.send_message(message.channel, "Pong!")

if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extensions(extensions)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{})'.format(extension, exc))
                                

                
client.run("NDAxNjE5NDUyOTY3MjU2MDY0.DTs1Lw.HMvl46cxdUtWrANlnaNTbBPsVw4")
