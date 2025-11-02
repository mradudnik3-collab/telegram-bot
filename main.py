import time
import requests

TOKEN = "8563242139:AAHORnBKvtXjufW7potMMsomWz6WDx6iVlI"
CHAT_ID = "@main_news_day"
LAST_SENT = 0

def send_post():
    global LAST_SENT
    now = time.time()
    if now - LAST_SENT < 3 * 60 * 60:  # 3 часа не прошло
        print("⏳ Ещё не прошло 3 часа, пропускаем.")
        return
    LAST_SENT = now

    text = "Автопостинг работает 🚀 (раз в 3 часа)"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    print(response.json())

print("🤖 Бот запущен. Ждём 3 часа перед первым постом.")
time.sleep(3 * 60 * 60)

while True:
    send_post()
    time.sleep(60)  # проверяем раз в минуту
