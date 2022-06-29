from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


def download_video(link):
    pass


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def unknown(update: Update, context: CallbackContext):
    link = update.message.text
    print(link)


def help_(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('/hello')


updater = Updater('5385875372:AAEtw98T8PggJiaXyatwc6XeuKfiWOg-fPo')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(CommandHandler('help', help_))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

updater.start_polling()
updater.idle()
