# Import 
import discord
import os
import asyncio
# From
from ast import alias
from asyncio.windows_events import NULL
from cgitb import text
from email import message
from math import remainder
from discord.ext import commands, tasks
from datetime import datetime, timedelta
from itertools import count, cycle
from aiohttp import request
from pyparsing import null_debug_action
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.utils import find

#Prefix '!'
client = commands.Bot(command_prefix='!')

client.remove_command("help")

status = cycle(
    ['Try !help','Prefix - !'])

@client.event
async def on_ready():
    change_status.start()
    print("Bot is Online!")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

###################################################################
#MAIN CODE
###################################################################

###################################################################
# 6HR REMIND
###################################################################

@client.command()
async def reminder(ctx):
    message_channel = client.get_channel(941022968534941777) #Channel ID
    createEmbed = discord.Embed(title='Have you eaten today?', description='✅ Yes\n❌ No\n⌛ Remind me in "**X**"')
    message = await message_channel.send(embed = createEmbed, delete_after=30)
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    await message.add_reaction('⌛')

    i = 0
    reaction = None

    while True:
        if str(reaction) == '✅':
            i = 0
            await message_channel.send('Amazing I will let your friends know!', delete_after=30)
            # Add function where it dms users from a list eg. @user ate some food today congratulate them!...
        elif str(reaction) == '❌':
            if i > 0:
                i -= 1
            await message_channel.send('Thats too bad... Try again tomorrow!', delete_after=30)
            # Add function where it dms users from a list eg. @user didnt eat today give them some motivation... 
        elif str(reaction) == '⌛':
            if i < 2:
                i += 1
            await message_channel.send('Ok! How long until I should remind you again:', delete_after=30)
            time = time
            seconds = 0
            if time.lower().endswith("d"):
                seconds += int(time[:-1]) * 60 * 60 * 24
                counter = f"{seconds // 60 // 60 // 24} Days"
            if time.lower().endswith("h"):
                seconds += int(time[:-1]) * 60 * 60
                counter = f"{seconds // 60 // 60} Hours"
            if time.lower().endswith("m"):
                seconds += int(time[:-1]) * 60
                counter = f"{seconds // 60} Minutes"
            if time.lower().endswith("s"):
                seconds += int(time[:-1])
                counter = f"{seconds} Seconds"
            if seconds == 0 or seconds > 7776000:
                await message_channel.send("Please specify a valid time!")
                msginput = await client.wait_for("message", check=check)
                if str(msginput.content) == time:
                    await message_channel.send(f"Alright I will remind you again in {counter}")
                await asyncio.sleep(counter)
                while(True):
                    if(reminder(input())):
                        break 

#Then loop again in the amount of hours.  

        # else:
        #     reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
        # await message.remove_reaction(reaction, user)

# @client.command(aliases=['stop', 'd'])
# async def deactivate(ctx):
#     deactivateEmbed = discord.Embed(title='Would you like me to stop reminding you?', description='✅ Stop reminding you\n❌ Cancel')
#     msg = await ctx.send(embed=deactivateEmbed, delete_after=30)
#     await msg.add_reaction('✅')
#     await msg.add_reaction('❌')


# # also add a command where when they react with ❌ or ✅ it breaks the loop and starts the next day. 
# @client.event
# async def on_reaction_add(reaction, user):
#     emoji = reaction.emoji
#     global activate
#     activate = False

#     if user.bot:
#         return

#     if emoji == '✅':
#         activate = False
#         await user.send('**I will stop reminding you now.**', delete_after=30)
#         #msg.cancel() #define function that will break loop and start next day

#     elif emoji == '❌':
#         await user.send('**I will continue reminding you.**', delete_after=30)
#         #cancel() #define function that will break loop and start next day

###################################################################
#Discord Bot Token
token = "TOKEN"
client.run(token)
###################################################################
