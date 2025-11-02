import time
import requests

TOKEN = "8563242139:AAHORnBKvtXjufW7potMMsomWz6WDx6iVlI"
CHAT_ID = "@main_news_day"

def send_post():
    text = "Автопостинг работает 🚀 (раз в 3 часа)"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    print(response.json())

print("Бот запущен. Первый пост через 3 часа.")
while True:
    send_post()
    time.sleep(3 * 60 * 60)  # 3 часа = 10800 секунд
