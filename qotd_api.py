#question of the day bot that uses Discord API to post to the server
#more functionality than the webhook version, but a bit trickier to set up.
import os
import json
import random
from datetime import datetime, timezone
from dotenv import load_dotenv
import discord
import asyncio

# Load environment variables
load_dotenv()
qotd_footer_text = os.getenv('DISCORD_BOT_FOOTER_TEXT', default="Alex's QOTD Bot")  # Allow footer to be changed so more people can feel the psychological safety needed to contribute to this.
input_questions_list_file_name = os.getenv('DISCORD_INPUT_QUESTIONS_LIST_FILE_NAME', default="questionsList.json")  # Input questions file
used_questions_list_file_name = os.getenv('DISCORD_USED_QUESTIONS_LIST_FILE_NAME', default="usedQuestions.json")  # Input questions file
bot_token = os.getenv('DISCORD_BOT_TOKEN')  # Bot token from the Discord Developer Portal
channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))  # Channel ID where the bot will post the message

def load_json_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}.")
        exit(1)

def save_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Load environment variables
load_dotenv()

# Load questions and used questions
questions = load_json_file(input_questions_list_file_name).get('questions', [])
used_questions = load_json_file(used_questions_list_file_name)

# If all questions have been used, reset the used questions
if len(used_questions) >= len(questions):
    used_questions = []

# Choose a question not in used questions
random_question = random.choice([q for q in questions if q not in used_questions])
used_questions.append(random_question)
save_json_file(used_questions_list_file_name, used_questions)

# Create an embed for the message
embed = discord.Embed(
    title="Question of the Day",
    description=random_question,
    color=0x9900FF,
    timestamp=datetime.now(timezone.utc)
)
embed.set_footer(text=qotd_footer_text)

# Define the required intents
intents = discord.Intents.default()
intents.messages = True  # Enable message intents

# Discord client with intents
client = discord.Client(intents=intents)

async def post_question():
    await client.wait_until_ready()
    channel = client.get_channel(channel_id)

    # Check and unpin previous messages pinned by the bot
    pinned_messages = await channel.pins()
    for message in pinned_messages:
        if message.author == client.user:
            await message.unpin()

    # Send the new message and pin it
    new_message = await channel.send(embed=embed)
    await new_message.pin()

    await client.close()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await post_question()

client.run(bot_token)

