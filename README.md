# Question of the Day Discord Bot

Question of the Day Discord Bot! Inspired by https://github.com/KevinNovak/QOTD-Bot-Docs and https://github.com/mrrfv/discord-webhook-qotd-bot

Set up a webhook on your discord server with [this guide.](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
Clone this repo onto the server that you plan to run the bot out of. Within the repo, create a `.env` file.

With your favorite editor, add this to the file:
```
WEBHOOK='YourWebHookURLHere'
```

Run `pip install python-dotenv`. Depending on your system, you may or may not need to `pip install` other modules as well.

Then run 
`python3 qotd.py`

This will run the job, read a question from questionsList.json, and add it to usedQuestions.json. (Which it will create if it doesn't exist)  When the number of questions is equal to the used questions, the usedQuestions.json file is nuked, and the bot starts again. Ideally, you would want this to run on a timed schedule, so I would advise creating a cron job to run this on a schedule.

If you are comfortable with Github Actions, go and [fork this repo](https://github.com/alexjyong/QuestionOfTheDayBot/fork), add your webhook url to the secrets section in the settings in the forked repo, and it will automatically post to your server at the time determined by the cron statement in the workflow.  Alternatively, you can manually trigger the job as well from the actions tab. 
