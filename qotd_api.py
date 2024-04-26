import os
import discord
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')  # Bot token from the Discord Developer Portal
channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))  # Channel ID where the bot will send the ping
user_id = 219143396499914752  # User ID of the person to ping

# Define the required intents
intents = discord.Intents.default()
intents.messages = True  # Enable message intents
intents.guilds = True  # Required to access information about guilds (servers)

# Discord client with intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(channel_id)
    if channel:
        user = await client.fetch_user(user_id)
        if user:
            await channel.send(f"{user.mention}, you've been pinged!")
        else:
            print("User not found.")
    else:
        print("Channel not found.")

    await client.close()  # Optionally close the client after sending the message

client.run(bot_token)
