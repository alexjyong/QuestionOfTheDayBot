import discord
import os
from dotenv import load_dotenv

load_dotenv()
from discord import app_commands
from discord.ui import Button, View
import random
import sqlite3
import asyncio

truths_pg = []  ## Initialize
truths_nsfw = []  ## Initialize
dares_pg = []  ## Initialize
dares_nsfw = []  ## Initialize


def gen_tds():
    """Generate four lists for the Truth or Dares"""
    conn = sqlite3.connect('tds.db')
    c = conn.cursor()
    for row in c.execute('SELECT "What is it?", Type, "Truth or Dare" FROM tds'):
        td = row[0]
        type = row[1]
        value = row[2]
        if td == "Truth":
            if type == "SFW":
                truths_pg.append(value)
            elif type == "NSFW":
                truths_nsfw.append(value)
        elif td == "Dare":
            if type == "SFW":
                dares_pg.append(value)
            elif type == "NSFW":
                dares_nsfw.append(value)

    conn.close()


gen_tds()  ## Run it once on load
# copy all to master lists
truths_pg_master = truths_pg.copy()
truths_nsfw_master = truths_nsfw.copy()
dares_pg_master = dares_pg.copy()
dares_nsfw_master = dares_nsfw.copy()

bot_author = os.getenv("BOTAUTHOR")
print(bot_author)
if bot_author == None: #use this as default name if the user didn't set it.
    bot_author = "SysTD"

def gen_embed(person, color_code, type, nsfw="No"):
    global dares_nsfw, dares_nsfw_master, dares_pg, dares_pg_master, truths_nsfw, truths_nsfw_master, truths_pg, truths_pg_master
    embed = discord.Embed(title=person, color=color_code)
    embed.set_author(name=bot_author)
    if type == "Dare" and nsfw == "Yes":
        from_list = dares_nsfw
    elif type == "Dare" and nsfw == "No":
        from_list = dares_pg
    elif type == "Truth" and nsfw == "Yes":
        from_list = truths_nsfw
    elif type == "Truth" and nsfw == "No":
        from_list = truths_pg
    else:  ## Change this later.
        from_list = truths_pg
    td_value = random.choice(from_list)
    from_list.remove(td_value)
    # If any list got emptied, copy it from the master
    if len(dares_nsfw) < 1:
        dares_nsfw = dares_nsfw_master.copy()
    if len(dares_pg) < 1:
        dares_pg = dares_pg_master.copy()
    if len(truths_nsfw) < 1:
        truths_nsfw = truths_nsfw_master.copy()
    if len(truths_pg) < 1:
        truths_pg = truths_pg_master.copy()
    type_name = ""
    if nsfw == "Yes":
        type_name = "NSFW "
    type_name += type
    embed.add_field(name=f"Your {type_name}:", value=td_value, inline=False)
    embed.set_thumbnail(url='https://sharepointlist.com/images/TD2.png')
    return embed

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

intents = discord.Intents.default()
client = MyClient(intents=intents)

# Event Listener when going online
@client.event
async def on_ready():
    # Counter to track how many servers bot is connected to
    guild_count = 0
    # Loop through servers
    for guild in client.guilds:
        # Print server name and ID
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1
    # Print total
    print("SysTD is in " + str(guild_count) + " servers.")

@client.tree.command()
async def play(interaction: discord.Interaction):
    '''Start the truth or dare activity'''
    global sent_msg, embed, sleep_time, sleep_task
    sleep_time = 150
    color_code = 0x0000FF
    embed = discord.Embed(title=interaction.user.display_name, color=color_code)
    embed.set_author(name=bot_author)
    embed.set_thumbnail(url='https://sharepointlist.com/images/TD2.png')

    async def sleep_timer():
        global sleep_task
        try:
            print("Starting sleep timer")
            await asyncio.sleep(sleep_time)
        except asyncio.CancelledError: # if it was canceled
            # probably don't need the except since I'm not actually doing anything with it
            print("Sleep timer canceled")
            raise
        else: # if it wasn't canceled
            print("Sleep timer expired. Refreshing bot message and restarting sleep timer")
            await sent_msg.edit(embed=embed, view=view)
            sleep_task = asyncio.create_task(sleep_timer())
        #finally: # Don't need a finally atm either
            
    class MyButton(Button):
        async def callback(self, interaction: interaction):
            global sent_msg, embed, style, sleep_task
            # Cancel refresh timer
            sleep_task.cancel()
            await sent_msg.edit(embed=embed, view=None)
            if self.label == "Truth" or self.label == "NSFW Truth":
                color_code = 0x0000FF
                type = "Truth"
                self.style=discord.ButtonStyle.primary
            elif self.label == "Dare" or self.label == "NSFW Dare":
                color_code = 0xFF0000
                type = "Dare"
                self.style=discord.ButtonStyle.danger
            if self.label == "NSFW Truth" or self.label == "NSFW Dare":
                nsfw = "Yes"
            else:
                nsfw = "No"
            person = interaction.user.display_name
            embed = gen_embed(person, color_code, type, nsfw=nsfw)
            await interaction.response.send_message(embed=embed, view=view)
            sent_msg = await interaction.original_response()
            # Restart refresh timer
            sleep_task = asyncio.create_task(sleep_timer())

    view = View()
    labels = ("Truth", "Dare", "NSFW Truth", "NSFW Dare")
    for label in labels:
        if label == "Truth" or label == "NSFW Truth":
            style = discord.ButtonStyle.primary
        else:
            style = discord.ButtonStyle.danger
        view.add_item(MyButton(label=label, style=style))

    await interaction.response.send_message(embed=embed, view=view)
    sent_msg = await interaction.original_response()
    sleep_task = asyncio.create_task(sleep_timer())

client.run(os.getenv("TOKEN"))
