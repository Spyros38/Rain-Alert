import requests
import os
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv()
load_dotenv(env_path)


# # For Open Weather Map API KEY
api_key = os.getenv("api_key")


parameters = {"lat": 37.983810,
              "lon": 23.727539,
              "appid": api_key,
              "units": "metric",
              "cnt": 4
              }

response = requests.get(url=" https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print(response.status_code)
response.raise_for_status()
data = response.json()
# # We can use a online json viewer to read the output of the data, such as: https://jsonviewer.stack.hu/
print(data)

# # Getting the weather code for the first entry
print(data["list"][0]["weather"][0]["id"])
# # Create an empty list to store the data:
weather_conditions_day = []
# # Length of observations, in a day we are going to have 4 observations
range_of_data = (len(data["list"]))
# # Get the weather data for each report:
for number in range(range_of_data):
    weather_conditions_day.append(data["list"][number]["weather"][0]["id"])
print(weather_conditions_day)


# # Bot!
def telegram_bot_sendtext(bot_message):
    bot_token = os.getenv("bot_token")
    # # From: https://api.telegram.org/{BOT_TOKEN}}/getupdates
    # , https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python
    bot_chatID = os.getenv('bot_chatID')
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    response.close()

    return response.json()


# test = telegram_bot_sendtext("Testing again!")
# print(test)


# # Print umbrella if codes are < 700:
for code in weather_conditions_day:
    if int(code) < 700:
        telegram_bot_sendtext("Its going to rain today. Get an umbrella!☔")
