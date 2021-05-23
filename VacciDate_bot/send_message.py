import requests
import json
import telegram
from utils.load_config import load_configuration

config = load_configuration(config_path="data/config.yml")
token = config.get("TELEGRAM").get("BOT")
url = "https://api.telegram.org/bot" + token
chat_id = config.get("TELEGRAM").get("CHAT_ID")


def send_message(text):
    try:
        params = {"chat_id": chat_id, "text": text}
        response = requests.post(url + "/sendMessage", data=params)
        resp_dict = json.loads(response.text)
        return True
    except Exception as error:
        print(f"Error in send_message : {error}")
        return False


def send_personal_message(msg, chat_id):
    """
    Send a mensage to a telegram user specified on chatId
    chat_id must be a number!
    """
    try:
        print(f"send message to : {chat_id}")
        bot = telegram.Bot(token=token)
        bot.sendMessage(chat_id=chat_id, text=msg)
        return True
    except Exception as error:
        print(f"Error in send_personal_message : {error}")
        return False
