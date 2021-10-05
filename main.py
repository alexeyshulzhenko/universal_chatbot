from telegram_bot import TelegramBot
import os

if __name__ == "__main__":
    print(str(os.environ['T_TOKEN']))
    t_bot = TelegramBot()
    t_bot.start_bot()
