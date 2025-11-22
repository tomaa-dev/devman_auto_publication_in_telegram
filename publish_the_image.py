import os
import telegram
from dotenv import load_dotenv 
import random
import argparse


def publish_for_telegram(directory, photo, tg_space_token, tg_chat_id):
    bot = telegram.Bot(token=tg_space_token)
    with open(f'{directory}/{photo}', 'rb') as document:
        bot.send_document(chat_id=tg_chat_id, document=document)


def take_files(directory):
    lst_of_images = []
    filesindir = os.listdir(directory)
    for filename in filesindir:
        lst_of_images.append(filename)
    return lst_of_images


if __name__ == "__main__":
    directory = os.path.join(os.path.dirname(__file__), 'images')

    load_dotenv()
    tg_space_token = os.environ["TELEGRAM_SPACE_TOKEN"]
    tg_chat_id = os.environ["TELEGRAM_ID"]

    parser = argparse.ArgumentParser(description="""Публикует указанную фотографию в канал. 
                                    Если “какую” не указано, публикует случайную фотографию.""")
    parser.add_argument('--photo', type=str)
    args = parser.parse_args()

    images = take_files(directory)

    if args.photo:
        if args.photo in images:
            publish_for_telegram(directory, args.photo, tg_space_token, tg_chat_id)
    else:
        random.shuffle(images)
        random_photo = images[0]
        publish_for_telegram(directory, random_photo, tg_space_token, tg_chat_id)