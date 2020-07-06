# internal modules
from os import environ as env

# external modules
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv, find_dotenv
from flask import Flask

# files
from telebot.constants import *

# initialize server
# server = Flask(__name__)




# Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


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

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(env.get(BOT_TOKEN), use_context=True)
    updater.start_webhook(listen="0.0.0.0", port=int(env.get('PORT', '5555')), url_path=BOT_TOKEN)
    updater.bot.set_webhook(HEROKU_URL + BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


'''
@server.route('/{}'.format(BOT_TOKEN), methods=['POST'])
def inbox():
    update = Update.de_json(request.get_json(force=True), bot)


@server.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    webhook = updater.bot.setWebhook('{URL}{TOKEN}'.format(URL=HEROKU_URL, TOKEN=BOT_TOKEN))
    if webhook:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@server.route('/')
def index():
    return '.'
'''


if __name__ == '__main__':
    main()
    #server.run(host="0.0.0.0", port=int(env.get('PORT', 5555)))