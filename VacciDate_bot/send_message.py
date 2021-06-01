import requests
import json
import telegram
import os
from datetime import datetime
from utils.load_config import load_configuration

today = datetime.now()
timestamp = today.timestamp()

config = load_configuration(config_path="data/config.yml")
token = config.get("TELEGRAM").get("BOT")
url = "https://api.telegram.org/bot" + token
chat_id = config.get("TELEGRAM").get("CHAT_ID")


def delete_message(message_id: str):
    params = {"chat_id": chat_id, "message_id": message_id}
    response = requests.post(url + "/deleteMessage", data=params)


def send_message(text):
    try:
        params = {"chat_id": chat_id, "text": text}
        response = requests.post(url + "/sendMessage", data=params)
        resp_text = json.loads(response.text)
        print(response.status_code)
        OriginalMessageid = resp_text["result"]["message_id"]
        print(f"{OriginalMessageid=}")
        ErrorMessageid = OriginalMessageid + 1
        print(f"{ErrorMessageid=}")
        # if response.status_code == 400:
        delete_message(message_id=ErrorMessageid)
        resp_dict = json.loads(response.text)
        data = {"timestamp": timestamp, "response": resp_dict}
        with open("data/message_sent.json", "w+") as f:
            json.dump(data, f)
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
