import os
import telegram
from dotenv import load_dotenv 
import random
import argparse


def publish_for_telegram(directory, photo, tg_space_token, tg_chat_id):
    bot = telegram.Bot(token=tg_space_token)
    filepath = os.path.join(directory, photo)
    with open(filepath, 'rb') as document:
        bot.send_document(chat_id=tg_chat_id, document=document)


def take_files(directory):
    filesindir = os.listdir(directory)
    lst_of_images = [filename for filename in filesindir]
    return lst_of_images


if __name__ == "__main__":
    directory = os.path.join(os.path.dirname(__file__), 'images')

    load_dotenv()
    tg_space_token = os.getenv("TELEGRAM_SPACE_TOKEN")
    tg_chat_id = os.getenv("TELEGRAM_ID")

    parser = argparse.ArgumentParser(description="""Публикует указанную фотографию в канал. 
                                    Если “какую” не указано, публикует случайную фотографию.""")
    parser.add_argument('--photo', type=str)
    parser.add_argument('--directory', type=str, default=directory)
    args = parser.parse_args()

    images = take_files(args.directory)

    if args.photo:
        if args.photo in images:
            publish_for_telegram(args.directory, args.photo, tg_space_token, tg_chat_id)
    else:
        random_photo = random.choice(images)
        publish_for_telegram(args.directory, random_photo, tg_space_token, tg_chat_id)