import requests

class TelegramBot:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_photo(self, file_path):
        url = f"https://api.telegram.org/bot{self.token}/sendPhoto"
        with open(file_path, "rb") as f:
            requests.post(url, data={"chat_id": self.chat_id}, files={"photo": f})

