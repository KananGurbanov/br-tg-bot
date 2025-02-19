from telegram.ext import Updater, CommandHandler
from app.bot.telegram_bot import start, screen
from app.constants.constants import TELEGRAM_TOKEN
from app.executor.executor import submit_task, shutdown_executor

def run_bot():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("screen", screen))

    updater.start_polling()
    updater.idle()

def main():
    submit_task(run_bot)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        shutdown_executor()
        print("Executor shut down.")

if __name__ == '__main__':
    main()
