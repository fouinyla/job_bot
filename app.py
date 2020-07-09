# internal modules
from os import environ as env
import asyncio

# external modules
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv, find_dotenv

# files
from telebot.constants import *


# Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

# First task: add /saymehi
def saymehi(update, context):
    """Send a message when the command /saymehi is issued."""
    first_name = update.message.chat.first_name
    update.message.reply_text('Hi, {}'. format(first_name))

def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)



def main():
    ENV_FILE = find_dotenv()
    if(ENV_FILE):
        load_dotenv(ENV_FILE)

    if (env.get(ENV) == 'LOCAL'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    elif (env.get(ENV) == 'HEROKU'):
        asyncio.set_event_loop(asyncio.SelectorEventLoop())

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(env.get(BOT_TOKEN), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("saymehi", saymehi))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # set webhook
    updater.start_webhook(listen=env.get(IP), port=env.get(PORT), url_path=env.get(BOT_TOKEN))

    # check environment
    url = None

    if(env.get(ENV) == 'LOCAL'):
        url = env.get(LOCAL_URL)
    elif(env.get(ENV) == 'HEROKU'):
        url = env.get(HEROKU_URL)
    print(f'{url}{env.get(BOT_TOKEN)}')
    updater.bot.set_webhook(f'{url}{env.get(BOT_TOKEN)}')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    #updater.idle()



if __name__ == '__main__':
    main()