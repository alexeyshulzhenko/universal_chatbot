import logging
import os
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from bot_core import Message

class TelegramBot:

    # Enable logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    logger = logging.getLogger(__name__)


    def __init__(self):
        self.messge_class = Message()
        self.token = str(os.environ['T_TOKEN'])
        self.user_id = str(os.environ['USER_ID'])

        if(self.token == '' or self.user_id == ''):
            raise Exception("No Environment Varibales")

    # Define a few command handlers. These usually take the two arguments update and
    # context.
    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        update.message.reply_markdown_v2(
            fr'Hi {user.mention_markdown_v2()}\!',
            reply_markup=ForceReply(selective=True),
        )


    def help_command(self, update: Update, context: CallbackContext) -> None:
        """Send a message when the command /help is issued."""
        update.message.reply_text('Help! Need help')


    def echo(self, update: Update, context: CallbackContext) -> None:
        """Echo the user message."""
        update.message.reply_text(update.message.text + " Language: " + self.messge_class.check_language(update.message.text))


    def check_user_id(self):

        return True


    def start_bot(self) -> None:
        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        updater = Updater(self.token)

        
        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher

        # on different commands - answer in Telegram
        dispatcher.add_handler(CommandHandler("start", self.start, Filters.user(username=self.user_id)))
        dispatcher.add_handler(CommandHandler("help", self.help_command, Filters.user(username=self.user_id)))

        # on non command i.e message - echo the message on Telegram
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo, Filters.user(username=self.user_id)))

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()
