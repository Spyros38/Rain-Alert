import os
from dotenv import load_dotenv, find_dotenv
import requests

env_path = find_dotenv()
load_dotenv(env_path)

token = os.getenv("token")


def telegram_bot_sendtext(bot_message):

   bot_token = os.getenv("bot_token")
   # # From: https://api.telegram.org/{insert_bot_token_here}/getupdates
   # , https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python
   bot_chatID = os.getenv("bot_chatID")
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID +\
               '&parse_mode=Markdown&text=' + bot_message
   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)
print(test)