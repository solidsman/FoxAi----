import os

#Discord module
try:
    import discord
except ModuleNotFoundError:
    os.system("pip install discord")
from discord.ext import tasks, commands
from discord.utils import get

#dotenv module
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    os.system("pip install dotenv")

#matplotlib module
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    os.system("pip install matplotlib")

#inbuild modules
from collections import defaultdict
import asyncio
import requests
import io

#For a more secure, we loaded the .env file and assign the token value to a variable 
load_dotenv(".env")
TOKEN = "enter your discord token"
NEWS_API_KEY = "enter your news api key"
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
welcome_channel_id = "enter your welcome id channel server by developer settings !"
polls = defaultdict(dict)


#Intents are permissions for the bot that are enabled based on the features necessary to run the bot.
intents=discord.Intents.all()
intents.members = True

#Comman prefix is setup here, this is what you have to type to issue a command to the bot
prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=intents)

#Removed the help command to create a custom help guide
bot.remove_command('cmd')

#------------------------------------------------Events------------------------------------------------------#

# welcoming inside server
# Customize the guidelines message
guidelines_message = (
    "★ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜᴛᴇʀʜᴇᴀᴠᴇɴ ᴄᴏᴍʀᴀᴅᴇ ! ᴘʟᴇᴀꜱᴇ ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛᴏ ꜰᴏʟʟᴏᴡ ᴛʜᴇꜱᴇ ɢᴜɪᴅᴇʟɪɴᴇꜱ ★ \n"
    "1. ʙᴇ ʀᴇꜱᴘᴇᴄᴛꜰᴜʟ ᴛᴏ ᴏᴜʀ ʙʀᴏᴛʜᴇʀʜᴏᴏᴅ ☮ \n"
    "2. ɴᴏ ꜱᴘᴀᴍᴍɪɴɢ ᴏʀ ᴏᴠᴇʀᴜꜱᴇ ᴏꜰ ᴄᴀᴘɪᴛᴀʟꜱ ☠ ☢.\n"
    "3. ᴍᴀᴋᴇ ᴜꜱᴇ ᴏꜰ ᴛʜᴇ ᴘʀᴏᴘᴇʀ ᴄʜᴀɴɴᴇʟꜱ ᴡʜᴇɴ ʜᴀᴠɪɴɢ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴꜱ🗣.\n"
    "4. ɴᴇᴠᴇʀ ꜱʜᴀʀᴇ ɴꜱꜰᴡ ᴄᴏɴᴛᴇɴᴛ ✖.\n"
    "5. ɪꜰ ʏᴏᴜ ᴀʀᴇ ɪɴᴛᴇʀᴇꜱᴛᴇᴅ ɪɴ ʀᴏʟᴇꜱ ᴅᴍ ᴛʜᴇ ᴀᴅᴍɪɴ ❗. \n"
    "6. ᴜꜱᴇ ᴀɴʏ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ɢɪᴠᴇ ᴏʀᴅᴇʀꜱ ɪꜰ ɴᴇᴄᴇꜱꜱᴀʀʏ—ᴊᴜꜱᴛ ɢɪᴠᴇ !ᴄᴍᴅ  🦾."
)


@bot.event
async def on_member_join(member):
    # Get the welcome channel by its ID
    welcome_channel = member.guild.get_channel(welcome_channel_id)

    if welcome_channel:
        # Send a welcome message with guidelines in the specified welcome channel
        await welcome_channel.send(
            f'ʜᴇʟʟᴏ ᴄᴏᴍʀᴀᴅᴇ ! {member.mention}\n'
            f'{guidelines_message}'
        )
    else:
        print(f"Error: Welcome channel with ID {welcome_channel_id} not found.")

# Command example: !guidelines
@bot.command(name='guidelines', help='Show server guidelines')
async def show_guidelines(ctx):
    await ctx.send(guidelines_message)



# Command example: !greet <user>
@bot.command(name='greet', help='Greet a specific user')
async def greet(ctx, member: discord.Member):
    await ctx.send(f'Hello Comrade {member.mention}!')

# Command example: !info
@bot.command(name='info', help='Get information about the bot')
async def bot_info(ctx):
    info_embed = discord.Embed(title='ꜰᴏxᴀɪ ⚛', description='ᴀ ᴇxᴏꜱᴋᴇʟᴇᴛᴏɴ ᴀɪ ʙᴜɪʟᴛ ꜰᴏʀ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ ᴀɴᴅ ᴍᴏʀᴇ ᴀɴᴀʟʏꜱɪꜱ, ᴠᴇʀ 3.0.', color=discord.Color.blue())
    info_embed.add_field(name='ꜱᴏʟɪᴅɴɪɴᴊᴀ', value='Snake', inline=False)
    info_embed.set_footer(text='Bot created with foxai.py')
    await ctx.send(embed=info_embed)


#Basic Discord Bot Commands: Chat with your bot!
@bot.command(name='hi')
async def msg(ctx):
    if ctx.author == bot.user:
        return
    else:
        await ctx.send("Hello Comrade !")

@bot.command(name='hau')
async def msg(ctx):
    if ctx.author == bot.user:
        return
    else:
        await ctx.send("fine mate ! and have a good day Comrade !")
@bot.command(name='thx')
async def msg(ctx):
    if ctx.author == bot.user:
        return
    else:
        await ctx.send("Your Welcome Comrade ! and have a nice day !")


# News       
async def fetch_news(category_params):
    try:
        # Request news from News API based on the specified category
        params = {'apiKey': NEWS_API_KEY, **category_params}
        response = requests.get(NEWS_API_ENDPOINT, params=params)
        news_data = response.json()

        # Extract relevant information
        articles = news_data['articles']
        news_list = [f"{article['title']} - {article['url']}" for article in articles]

        return news_list

    except Exception as e:
        print(f'Error fetching news: {e}')
        return ['Error fetching news. Please try again later.']

@bot.command(name='headlines', help='Get top headlines')
async def get_headlines(ctx):
    category_params = {'country': 'us', 'pageSize': 5}
    news_list = await fetch_news(category_params)
    await ctx.send('\n'.join(news_list))

@bot.command(name='technews', help='Get technology news')
async def get_tech_news(ctx):
    category_params = {'country': 'us', 'category': 'technology', 'pageSize': 5}
    news_list = await fetch_news(category_params)
    await ctx.send('\n'.join(news_list))

@bot.command(name='sportsnews', help='Get sports news')
async def get_sports_news(ctx):
    category_params = {'country': 'us', 'q': 'sports', 'pageSize': 5}
    news_list = await fetch_news(category_params)
    await ctx.send('\n'.join(news_list))




#graph generator 
@bot.command(name='generate_graph', help='Generate a graph using Matplotlib')
async def generate_graph(ctx, *args):
    try:
        # Separate data points and title
        data_points = args[:-1]
        title = args[-1]

        # Convert data points to pairs (category, value)
        data_pairs = [(data_points[i], int(data_points[i + 1])) for i in range(0, len(data_points), 2)]

        # Plot the graph
        categories, values = zip(*data_pairs)
        plt.bar(categories, values)
        
        # Set the custom title
        plt.title(title)
        
        plt.xlabel('Categories')
        plt.ylabel('Values')

        # Save the plot to an image
        image_stream = io.BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)

        # Send the image in the Discord channel
        await ctx.send(file=discord.File(image_stream, filename='graph.png'))

        # Clear the plot for the next graph
        plt.clf()

    except Exception as e:
        await ctx.send(f'Error: {e}')





#polling system
@bot.command(name='create_poll', help='Create a new poll')
async def create_poll(ctx, question, *options):
    # Check if options are provided
    if len(options) < 2:
        await ctx.send('Please provide at least two options for the poll.')
        return

    # Save the poll in the dictionary
    poll_data = {
        'question': question,
        'options': options,
        'votes': defaultdict(int)
    }
    polls[ctx.guild.id][ctx.channel.id] = poll_data

    # Display the poll
    poll_embed = discord.Embed(title=question, description='\n'.join(f'{i + 1}. {option}' for i, option in enumerate(options)), color=discord.Color.blue())
    message = await ctx.send(embed=poll_embed)

    # Add numerical emoji reactions for voting
    for i in range(len(options)):
        emoji = f'{i + 1}\u20e3'  # Using numerical emoji (1️⃣, 2️⃣, 3️⃣, ...)
        await message.add_reaction(emoji)

    # Update poll data with message ID for reference
    poll_data['message_id'] = message.id

# Event to handle reactions (votes)
@bot.event
async def on_reaction_add(reaction, user):
    # Check if the reaction is added to a message in an active poll
    if user.bot:
        return  # Ignore reactions from other bots

    guild_id = reaction.message.guild.id
    channel_id = reaction.message.channel.id

    if guild_id in polls and channel_id in polls[guild_id]:
        poll = polls[guild_id][channel_id]

        # Check if the message ID matches the poll's message ID
        if reaction.message.id == poll['message_id']:
            # Check if the reaction emoji corresponds to a poll option
            for i, option in enumerate(poll['options']):
                emoji = f'{i + 1}\u20e3'
                if reaction.emoji == emoji:
                    poll['votes'][option] += 1
                    break  # Only count one vote per user

# Command to end the current poll and display results
@bot.command(name='end_poll', help='End the current poll')
async def end_poll(ctx):
    # Check if there is a poll in the current channel
    if ctx.guild.id in polls and ctx.channel.id in polls[ctx.guild.id]:
        poll = polls[ctx.guild.id][ctx.channel.id]

        # Get the message with the poll
        message = await ctx.channel.fetch_message(poll['message_id'])

        # Display the poll results
        results_embed = discord.Embed(title=f'Results for "{poll["question"]}"', color=discord.Color.green())
        for option, votes in poll['votes'].items():
            results_embed.add_field(name=option, value=f'Votes: {votes}')

        await ctx.send(embed=results_embed)

        # Remove the poll from the dictionary
        del polls[ctx.guild.id][ctx.channel.id]

    else:
        await ctx.send('There is no active poll in this channel.')









#Delete the blacklist message and warn the user to refrain them from sending using such words again.
@bot.event
async def on_message(message):
    if prefix in message.content:
        print("This is a command")
        await bot.process_commands(message)
    else:
        try:
            with open("words_blacklist.txt", "r") as bf:
                blacklist = [word.strip().lower() for word in bf.readlines()]
        except Exception:
            blacklist = []
            print(print("File not Found....!"))

        channel = message.channel
        for word in blacklist:
            if word in message.content:
                bot_message = await channel.send("ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴄᴏɴᴛᴀɪɴꜱ ᴀ ʙᴀɴɴᴇᴅ ᴡᴏʀᴅ ✖.")
                await message.delete()
                await asyncio.sleep(3)
                await bot_message.delete()
                
        await bot.process_commands(message)

#-----------------------------------------Moderation---------------------------------------------------------------#

@bot.event
async def on_command_error(context, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await context.send("Oh no! Looks like you have missed out an argument for this command.")
    if isinstance(error, commands.MissingPermissions):
        await context.send("Oh no! Looks like you Dont have the permissions for this command.")
    if isinstance(error, commands.MissingRole):
        await context.send("Oh no! Looks like you Dont have the roles for this command.")
    #bot errors
    if isinstance(error, commands.BotMissingPermissions):
        await context.send("Oh no! Looks like I Dont have the permissions for this command.")
    if isinstance(error, commands.BotMissingRole):
        await context.send("Oh no! Looks like I Dont have the roles for this command.")
    

#|------------------COMMANDS------------------|   
@bot.command()
async def cmd(message):
    helpC = discord.Embed(title="❗ꜰᴏx-ᴀɪ \n ʜᴇʟᴘ ɢᴜɪᴅᴇ❕", description="☢️ꜰᴏx-ᴀɪ ʙᴜɪʟᴛ ꜰᴏʀ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ ☮︎")
    helpC.add_field(name="ᴄʟᴇᴀʀ", value="ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛʏᴘᴇ !ᴄʟᴇᴀʀ ᴀɴᴅ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏꜰ ᴍᴇꜱꜱᴀɢᴇꜱ ʏᴏᴜ ᴡᴏᴜʟᴅ ʟɪᴋᴇ ᴛᴏ ᴅᴇʟᴇᴛᴇ, ᴛʜᴇ ᴅᴇꜰᴀᴜʟᴛ ɪꜱ 5.", inline=False)
    helpC.add_field(name="ᴋɪᴄᴋ/ʙᴀɴ/ᴜɴʙᴀɴ/ꜱᴏꜰᴛʙᴀɴ", value="ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛʏᴘᴇ !ᴋɪᴄᴋ/!ʙᴀɴ/!ᴜɴʙᴀɴ/!ꜱᴏꜰᴛʙᴀɴ ᴛʜᴇɴ ᴍᴇɴᴛɪᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ʏᴏᴜ ᴡᴏᴜʟᴅ ʟɪᴋᴇ ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴏɴ, ɴᴏᴛᴇ: ᴜꜱᴇʀ ᴍᴜꜱᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴꜱ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.", inline=False)
    helpC.add_field(name="ᴘᴏʟʟɪɴɢ_ꜱʏꜱᴛᴇᴍ", value="ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛʏᴘᴇ !ᴄʀᴇᴀᴛᴇᴘᴏʟʟ 'Qᴜᴇꜱᴛɪᴏɴ' ᴏᴘᴛɪᴏɴ1 ᴏᴘᴛɪᴏɴ2 ᴏᴘᴛɪᴏɴ3", inline=False)
    helpC.add_field(name="ʀᴇᴀʟ-ᴛɪᴍᴇ_ɴᴇᴡꜱ", value="ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴛʏᴘᴇ !ʜᴇᴀᴅʟɪɴᴇꜱ , !ꜱᴘᴏʀᴛꜱɴᴇᴡꜱ ᴀɴᴅ !ᴛᴇᴄʜɴᴇᴡꜱ.", inline=False)
    helpC.add_field(name="ꜰʀɪᴇɴᴅʟʏ_ᴄᴏᴍᴍᴀɴᴅꜱ", value="ᴛᴏ ᴜꜱᴇ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ !ɢʀᴇᴇᴛ @ᴜꜱᴇʀ ,!ʜɪ, !ʜᴀᴜ ᴀɴᴅ !ᴛʜx", inline=False)
    helpC.add_field(name="ɢᴇɴᴇʀᴀᴛɪɴɢ_ʙᴀʀɢʀᴀᴘʜꜱ", value="ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ  !ɢᴇɴᴇʀᴀᴛᴇ_ɢʀᴀᴘʜ ᴏᴘᴛɪᴏɴᴀ 20 ᴏᴘᴛɪᴏɴʙ  30 ᴏᴘᴛɪᴏɴᴄ 50 ᴛɪᴛʟᴇ", inline=False)
    await message.channel.send(embed=helpC)

@bot.command()
#Checks whether the user has the correct permissions when this command is issued
@commands.has_permissions(manage_messages=True)
async def clear(context, amount=5):
    await context.channel.purge(limit=amount+1)

#Kick and ban work in a similar way as they both require a member to kick/ban and a reason for this
#As long as the moderator has the right permissions the member will be banned/kicked
@bot.command()
@commands.has_permissions(kick_members=True)   
async def kick(context, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await context.send(f'ᴀ ɪɴᴛʀᴜᴅᴇʀ {member} ᴋɪᴄᴋᴇᴅ ᴀɴᴅ ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ⊹')

@bot.command()
@commands.has_permissions(ban_members=True)   
async def ban(context, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await context.send(f'{member} ʜᴀꜱ ʙᴇᴇɴ ʙᴀɴɴᴇᴅ ☢ ')

#Unbanning a member is done via typing ./unban and the ID of the banned member
@bot.command()
@commands.has_permissions(ban_members=True)   
async def unban(context, id : int):
    user = await bot.fetch_user(id)
    await context.guild.unban(user)
    await context.send(f'{user.name} ʜᴀꜱ ʙᴇᴇɴ ᴜɴʙᴀɴɴᴇᴅ  ⛓')
    
#Bans a member for a specific number of days
@bot.command()
@commands.has_permissions(ban_members=True)
async def softban(context, member : discord.Member, days, reason=None):
    #Asyncio uses seconds for its sleep function
    #multiplying the num of days the user enters by the num of seconds in a day
    days * 36 
    await member.ban(reason=reason)
    await context.send(f'{member} ʜᴀꜱ ʙᴇᴇɴ ꜱᴏꜰᴛʙᴀɴɴᴇᴅ✴')
    await asyncio.sleep(days)
    print("Time to unban")
    await member.unban()
    await context.send(f'{member} ꜱᴏꜰᴛʙᴀɴ ʜᴀꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜰɪɴɪꜱʜᴇᴅ !')

#This command will add a word to the blacklist to prevent users from typing that specific word
@bot.command()
@commands.has_permissions(ban_members=True)
async def blacklist_add(context, *, word):
    try:
        with open("words_blacklist.txt", "a") as f:
            f.write(word+"\n")
    except Exception:
        print("Unknow error occurred....!")

    await context.send(f'Word "{word}" added to blacklist.')

#Run the bot
try:
    bot.run(TOKEN)
except Exception as e:
    print(f"An error occurred: {e}")
