import discord
from discord.ext import commands

# Define the intents your bot needs
intents = discord.Intents.default()
intents.typing = False
intents.message_content = True    # You can customize these intents based on your bot's needs

# Your bot token
bot_token = "MTEzODMzNDExMzA2NjEzOTcyOQ.GwbEno.rqBMHOKewwiZ1P7FGIJ1DXSSnmh1hJDeqtyEB8"  # Replace "YOUR_BOT_TOKEN" with your actual bot token

# Create a bot instance with specified intents and a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')

@bot.command()
async def hello(ctx):
    """Responds with a friendly greeting."""
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Handle errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Ignore if the command is not found

    # Handle other errors
    await ctx.send(f'An error occurred: {error}')

@bot.command()
async def test(ctx):
    await ctx.send('Test successful!')

# Run the bot using the bot token
bot.run(bot_token)
