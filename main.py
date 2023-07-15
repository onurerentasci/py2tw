import os
import threading

from py2txt import messageCollector
from py2twitter import tweet


def tweet_new_messages(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        last_lines = lines[-2:]
        message = " ".join(line.strip() for line in last_lines)
        tweet(message)
        print("1 mesaj twit atıldı")


def run_collector_and_tweet():
    # iki fonksiyon için threadleri oluştur
    collector_thread = threading.Thread(target=messageCollector)
    tweet_thread = threading.Thread(target=check_for_new_messages)

    # threadi başlat
    collector_thread.start()
    tweet_thread.start()

    # threadlerin tamamlanmasını bekle ve bitir
    collector_thread.join()
    tweet_thread.join()


def check_for_new_messages():
    file_path = "collected_msgs.txt"
    file_size = os.stat(file_path).st_size

    while True:
        # txt dosyasına yeni satır eklenirse tweet_new_messages fonksiyonunu çalıştır
        current_size = os.stat(file_path).st_size
        if current_size > file_size:
            tweet_new_messages(file_path)
            file_size = current_size


# Run
if __name__ == "__main__":
    run_collector_and_tweet()
