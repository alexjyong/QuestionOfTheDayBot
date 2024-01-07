# Question of the Day Discord Bot

Question of the Day Discord Bot! Inspired by https://github.com/KevinNovak/QOTD-Bot-Docs and https://github.com/mrrfv/discord-webhook-qotd-bot

## Set up

There are two versions of the bot, the webhook version and the api version. Webhook version is the easiest to set up, but has the least functionality. 

API version has more bells and whistles, but is a bit tricker to set up.

### API Version
Create a discord bot using the guide [here](https://www.upwork.com/resources/how-to-make-discord-bot#creating-a-discord-bot)
You will need to give it enough permissions to read messages and channels, read message history, and send messages. 

During the process, you will get an API token for your bot. Keep it saffe, and add it to the .env file wherever your bot is hosted.

Get the channel ID of wherever you want this bot to post as well. 

Your .env file should look like this:
```
DISCORD_BOT_TOKEN=blahblahblah
DISCORD_CHANNEL_ID=blahblah
```
Run `pip install discord.py python-dotenv`. Depending on your system, you may or may not need to `pip install` other modules as well.
Then run
`python3 qotd_api.py`

This will run the job, read a question from questionsList.json, and add it to usedQuestions.json. (Which it will create if it doesn't exist)  When the number of questions is equal to the used questions, the usedQuestions.json file is nuked, and the bot starts again. Ideally, you would want this to run on a timed schedule, so I would advise creating a cron job to run this on a schedule.

If you are comfortable with Github Actions, go and [fork this repo](https://github.com/alexjyong/QuestionOfTheDayBot/fork), add your channel ID and discord bot token to the secrets section in the settings in the forked repo, and it will automatically post to your server at the time determined by the cron statement in the workflow.  Alternatively, you can manually trigger the job as well from the actions tab. 

### Webhook version

Set up a webhook on your discord server with [this guide.](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
Clone this repo onto the server that you plan to run the bot out of. Within the repo, create a `.env` file.

With your favorite editor, add this to the file:
```
WEBHOOK='YourWebHookURLHere'
```

Run `pip install python-dotenv requests`. Depending on your system, you may or may not need to `pip install` other modules as well.

Then run 
`python3 qotd_webhook.py`

This will run the job, read a question from questionsList.json, and add it to usedQuestions.json. (Which it will create if it doesn't exist)  When the number of questions is equal to the used questions, the usedQuestions.json file is nuked, and the bot starts again. Ideally, you would want this to run on a timed schedule, so I would advise creating a cron job to run this on a schedule.

If you are comfortable with Github Actions, go and [fork this repo](https://github.com/alexjyong/QuestionOfTheDayBot/fork), add your webhook url to the secrets section in the settings in the forked repo, and it will automatically post to your server at the time determined by the cron statement in the workflow.  Alternatively, you can manually trigger the job as well from the actions tab. 
