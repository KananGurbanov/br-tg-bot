from telegram import Update
from telegram.ext import CallbackContext
from io import BytesIO

from app.gitlab.screenshot import Gitlab


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Use /screen to take a screenshot of the GitLab homepage.')

def screen(update: Update, context: CallbackContext):
    update.message.reply_text("Logging into GitLab and taking a screenshot...")

    try:
        gitlab = Gitlab()
        screenshot_image = gitlab.get_gitlab_screenshot()

        image_stream = BytesIO()
        screenshot_image.save(image_stream, format='PNG')
        image_stream.seek(0)

        update.message.reply_photo(photo=image_stream)

    except Exception as e:
        update.message.reply_text(f"Error occurred: {e}")
