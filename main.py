import telegram
from os import environ as env
from telegram.error import NetworkError, Unauthorized
from time import sleep
from dotenv import load_dotenv, find_dotenv
from constants import *

update_id = None

def main():
    ENV_FILE = find_dotenv()
    if(ENV_FILE):
        load_dotenv(ENV_FILE)

    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot(env.get(BOT_TOKEN))

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            update.message.reply_text(update.message.text)


if __name__ == '__main__':
    main()