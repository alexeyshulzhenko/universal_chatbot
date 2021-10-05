from telegram_bot import TelegramBot
import os

def _conf_check():
    file_check = os.path.exists(
                    os.path.dirname(
                        os.path.abspath(__file__)) + "/auth.txt")
    
    if not file_check:
        raise Exception("You must create/or fill the auth.txt file!")
    
    return 1

if __name__ == "__main__":

    configuration_status = _conf_check()

    if (configuration_status == 1):
        t_bot = TelegramBot()
        t_bot.start_bot()
