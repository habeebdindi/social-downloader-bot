#!/usr/bin/env python3
import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, \
     MessageHandler, filters, ContextTypes
from helpers import is_tweet, is_ig, is_tiktok

TOKEN: Final = os.environ.get("BOT_TOKEN")
BOT_USERNAME: Final = os.environ.get("BOT_USERNAME")

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Hello, I am a bot that downloads social media videos for you. Just send me the link of the video (Twitter, Tiktok, and Instagram).'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Just send a link bro!')

#Responses
def handle_response(text: str) -> str:
    if is_tweet(text):
        return text.replace("twitter.com", "fxtwitter.com").replace("x.com", "fxtwitter.com");
    elif is_ig(text):
        return text.replace("instagram.com", "ddinstagram.com")
    elif is_tiktok(text):
        return text.replace("lite.tiktok.com", "tfxktok.com").replace("tiktok.com", "tfxktok.com")
    else:
        return text

#Message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot: ', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot..')
    print(os.environ.get("BOT_TOKEN"))
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    print('polling...')
    app.run_polling(poll_interval=1)
