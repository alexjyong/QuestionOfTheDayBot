import requests
import json
import random

# Replace 'YOUR_WEBHOOK_URL' with the actual URL of the webhook
webhook_url = 'YOUR_WEBHOOK_URL'

# Load questions from the JSON file
with open('questionsList.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the list of questions
questions = data.get('questions', [])

# Check if there are questions in the list
if not questions:
    print("No questions found in the JSON file.")
    exit(1)

# Choose a random question
random_question = random.choice(questions)

# Create a dictionary for the payload
payload = {
    "content": f"**Random Question:**\n{random_question}"
}

# Send the POST request to the webhook URL
response = requests.post(webhook_url, json=payload)

# Check the response status code
if response.status_code == 200:
    print("Random question successfully posted to the webhook.")
else:
    print(f"Failed to post the random question. Status code: {response.status_code}")
    print(response.text)
