FROM python:3
FROM gorialis/discord.py

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
COPY . .
RUN pip install python-dotenv

CMD [ "python3", "systd.py" ]