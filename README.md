# Question of the Day Bot

Question of the Day Bot! Inspired by https://github.com/KevinNovak/QOTD-Bot-Docs and https://github.com/mrrfv/discord-webhook-qotd-bot

Set up a webhook on your discord server with [this guide.](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
Clone this repo onto the server that you plan to run the bot out of. Within the repo, create a `.env` file.

With your favorite editor, add this to the file:
```
WEBHOOK='YourWebHookURLHere'
```

Run `pip install python-dotenv`. Depending on your system, you may or may not need to `pip install` other modules as well.

Then run 
`python3 qotd.py`

This will run the job, read a question from questionsList.json, and add it to usedQuestions.json.  When the number of questions is equal to the used questions, the usedQuestions.json file is nuked, and the bot starts again.
