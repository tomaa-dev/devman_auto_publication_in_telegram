import os
import telegram
import random
import time
from dotenv import load_dotenv 
from publish_the_image import publish_for_telegram, take_files


def publish_all_images(directory, interval, tg_space_token, tg_chat_id):
    while True:
        images = take_files(directory)
        random.shuffle(images)
        for image in images:
            publish_for_telegram(directory, image, tg_space_token, tg_chat_id)
            time.sleep(interval)


if __name__ == "__main__":
    directory = os.path.join(os.path.dirname(__file__), 'images')

    load_dotenv()
    tg_space_token = os.environ["TELEGRAM_SPACE_TOKEN"]
    tg_chat_id = os.environ["TELEGRAM_ID"]

    interval = int(os.environ.get("PUBLISH_INTERVAL", 14400))

    publish_all_images(directory, interval, tg_space_token, tg_chat_id)