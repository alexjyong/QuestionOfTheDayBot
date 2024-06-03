#question of the day bot that uses webhook urls to post to your server. 
#less functionality than using the discord API, but easier to set up.
import os
import json
import random
from datetime import datetime, timezone
from dotenv import load_dotenv
import requests

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
qotd_footer_text = os.getenv('DISCORD_BOT_FOOTER_TEXT', default="Alex's QOTD Bot")  # Allow footer to be changed so more people can feel the psychological safety needed to contribute to this.
input_questions_list_file_name = os.getenv('DISCORD_INPUT_QUESTIONS_LIST_FILE_NAME', default="questionsList.json")  # Input questions file
used_questions_list_file_name = os.getenv('DISCORD_USED_QUESTIONS_LIST_FILE_NAME', default="usedQuestions.json")  # Input questions file
webhook_url = os.getenv('WEBHOOK_URL')
if not webhook_url:
    print("Webhook URL not found.")
    exit(1)

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
embed = {
    "title": "Question of the Day",
    "description": random_question,
    "color": 0x00ff00,
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "footer": {
        "text": str(qotd_footer_text)
    }
}

# Payload with the embed
payload = {"embeds": [embed]}

# Send the POST request to the webhook URL
try:
    response = requests.post(webhook_url, json=payload)
    response.raise_for_status()
    print("Random question successfully posted to the webhook.")
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
