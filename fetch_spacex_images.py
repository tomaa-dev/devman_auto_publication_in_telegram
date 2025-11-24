import requests
import os
import argparse
from image_downloader import create_directory, download_the_image, get_file_extension


def fetch_spacex_last_launch(directory, spacex_id):
    space_x_url = f'https://api.spacexdata.com/v5/launches/{spacex_id}'

    response_spacex = requests.get(space_x_url)
    response_spacex.raise_for_status()
    spacex_image_urls = response_spacex.json()["links"]["flickr"]["original"]

    for url_number, url in enumerate(spacex_image_urls):
        file_extension = get_file_extension(url)
        filename = f'spacex_{url_number}{file_extension}'
        filepath_to_spacex = os.path.join(directory, filename)

        response_spacex_image = requests.get(url)
        response_spacex_image.raise_for_status()
        download_the_image(response_spacex_image, filepath_to_spacex)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Скачивает фото запуска SpaceX")
    parser.add_argument('--id', type=str, default='latest', help='SpaceX launch ID')
    args = parser.parse_args()

    directory = os.path.join(os.path.dirname(__file__), 'images')
    create_directory(directory)

    fetch_spacex_last_launch(directory, args.id)