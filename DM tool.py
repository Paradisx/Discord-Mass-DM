import discord
import os

client = discord.Client()
os.system('title DM Tool By Dassidy')
token = input("[\x1b[38;5;207m?\033[39m] Token \x1b[38;5;207m>\033[39m ")

@client.event
async def on_connect():
    message = input("[\x1b[38;5;207m?\033[39m] Message \x1b[38;5;207m>\033[39m ")
    for channel in client.private_channels:
        try:
            await channel.send(message)
            print(f"[\x1b[38;5;119m!\033[39m] Sent Direct Message To \x1b[38;5;207m[\033[39m{channel}\x1b[38;5;207m]\033[39m")
        except:
            print(f"[\x1b[38;5;160m!\033[39m] Unable To DM \x1b[38;5;207m[\033[39m{channel}\x1b[38;5;207m]\033[39m")


client.run(token, bot=False)
