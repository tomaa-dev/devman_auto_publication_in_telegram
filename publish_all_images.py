import os
import telegram
import random
import time
import argparse
from dotenv import load_dotenv 
from publish_the_image import publish_for_telegram, take_files
from telegram.error import NetworkError, TelegramError


def publish_all_images(directory, interval, tg_space_token, tg_chat_id):
    while True:
        images = take_files(directory)
        random.shuffle(images)
        for image in images:
            try:
                publish_for_telegram(directory, image, tg_space_token, tg_chat_id)
                time.sleep(interval)

            except (NetworkError, TelegramError) as e:
                time.sleep(1)
                continue


if __name__ == "__main__":
    directory = os.path.join(os.path.dirname(__file__), 'images')

    load_dotenv()
    tg_space_token = os.environ["TELEGRAM_SPACE_TOKEN"]
    tg_chat_id = os.environ["TELEGRAM_ID"]

    parser = argparse.ArgumentParser(description="""Указать собственную директорию""")
    parser.add_argument('--directory', type=str, default=directory)
    args = parser.parse_args()

    interval = int(os.environ.get("PUBLISH_INTERVAL", 14400))

    publish_all_images(args.directory, interval, tg_space_token, tg_chat_id)