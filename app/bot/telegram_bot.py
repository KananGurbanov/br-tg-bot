from telegram import Update
from telegram.ext import CallbackContext
from io import BytesIO

from app.gitlab.screenshot import HD_Film_Cehennemi


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! Use /screen to take a screenshot of the HD Film Cehennemi homepage.')

def screen(update: Update, context: CallbackContext):
    update.message.reply_text("Logging into HD Film Cehennemi and taking a screenshot...")

    try:
        website = HD_Film_Cehennemi()
        screenshot_image = website.get_hd_film_cehennemi_screenshot()

        image_stream = BytesIO()
        screenshot_image.save(image_stream, format='PNG')
        image_stream.seek(0)

        update.message.reply_photo(photo=image_stream)

    except Exception as e:
        update.message.reply_text(f"Error occurred: {e}")
