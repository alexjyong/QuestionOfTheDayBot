# Question of the Day Bot

Question of the Day Bot! Inspired by https://github.com/KevinNovak/QOTD-Bot-Docs. 

To run on your discord server, set up a bot with [guide](https://discordpy.readthedocs.io/en/stable/discord.html).

Clone this repo onto the server that you plan to run the bot out of. Within the repo, create a `.env` file.

With your favorite editor, add this to the file:
```
TOKEN='tokenFromTheLastStepHere'
BOTAUTHOR='WhatEverYouWantTheNameToBe'
```

(If you don't add in BOTAUTHOR, it will use the name `SysTD` by default.


install discord.py and python-dotenv via pip, then run
`python3 systd.py`

Or run via Docker with
`docker build -t discord-bot .`
then
`docker run -d -t discord-bot` 
