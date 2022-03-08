###################################################################
# AUTO REMIND
###################################################################

@client.command(aliases=['AR'])
async def ar(ctx):
    checkmark = '✅'
    X_No = '❌'
    hourglass = '⌛'
    message_channel = client.get_channel(941022968534941777) #Channel ID
    seconds = 0
    createEmbed = discord.Embed(title='Have you eaten today?', description=f'{checkmark} Yes\n{X_No} No\n⌛ Remind me in "**X**"')
    message = await ctx.send(embed = createEmbed, delete_after=30)
    await message.add_reaction(f'{checkmark}')
    await message.add_reaction(f'{X_No}')
    await message.add_reaction(f'{hourglass}')

    def check(reaction, user):
        return user == ctx.author and str(
            reaction.emoji) in [checkmark, X_No, hourglass]

    i = 0
    reaction = None

    while True:
        if str(reaction) == f'{checkmark}':
            i = 0
            await ctx.send('Amazing I will let your friends know!', delete_after=30)
            # Add function where it dms users from a list eg. @user ate some food today congratulate them!...
        elif str(reaction) == f'{X_No}':
            if i > 0:
                i -= 1
            await ctx.send('Thats too bad... Try again tomorrow!', delete_after=30)
            # Add function where it dms users from a list eg. @user didnt eat today give them some motivation... 
        elif str(reaction) == f'{hourglass}':
            if i < 2:
                i += 1
            await message_channel.send('Ok! How long until I should remind you again:', delete_after=30)
            def check(m):
                return m.author == message.author and m.channel == message.channel
            mesg = await client.wait_for("message", check=check, timeout=60)
            time = mesg
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
            if str(mesg.content) == time:
                await message_channel.send(f"Alright I will remind you again in {counter}")
                await asyncio.sleep(counter)
            else:
                await message_channel.send(f"There Was an Unexpected Error")
                    
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=10.0, check=check)
        except:
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
