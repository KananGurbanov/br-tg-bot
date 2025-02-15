from telegram.ext import Updater, CommandHandler

from app.bot.telegram_bot import start, screen
from app.constants.constants import TELEGRAM_TOKEN


def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("screen", screen))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()