import requests
import json
import random
from datetime import datetime  # Import the datetime module

webhook_url = 'REDACTED' #make this an argument later

# Try to load questions from the JSON file
try:
    with open('questionsList.json', 'r') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("The questionsList.json file was not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error decoding JSON from the file.")
    exit(1)

# Extract the list of questions
questions = data.get('questions', [])

# Check if there are questions in the list
if not questions:
    print("No questions found in the JSON file.")
    exit(1)

# Choose a random question
random_question = random.choice(questions)

# Create an embed for the message
embed = {
    "title": "Question of the Day",
    "description": random_question,
    "color": 0x00ff00,  # Green color
    "timestamp": str(datetime.utcnow()),  # Corrected UTC timestamp
    "footer": {
        "text": "Discord QOTD Bot"
    }
}

# Create the payload with the embed
payload = {
    "embeds": [embed]
}

# Send the POST request to the webhook URL with error handling
try:
    response = requests.post(webhook_url, json=payload)
    response.raise_for_status()  # Raises HTTPError for bad requests
    print("Random question successfully posted to the webhook.")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
