import requests
import os
from image_downloader import create_directory, download_the_image, get_file_extension
from datetime import datetime


def fetch_nasa_epic(directory):
    url = "https://epic.gsfc.nasa.gov/api/natural"

    response = requests.get(url)
    response.raise_for_status()
    data_of_nasa_epic = response.json()

    for url_number, img_data in enumerate(data_of_nasa_epic):
        img = img_data['image']
        date_str = img_data['date']
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        date_of_image = date.strftime("%Y/%m/%d")

        url_for_nasa_epic = f'https://epic.gsfc.nasa.gov/archive/natural/{date_of_image}/png/{img}.png'
        filename = f'nasa_epic_{url_number}.png'
        filepath_to_nasa = os.path.join(directory, filename)

        response_epic_image = requests.get(url_for_nasa_epic)
        response_epic_image.raise_for_status()
        download_the_image(response_epic_image, filepath_to_nasa)


if __name__ == "__main__":
    directory = os.path.join(os.path.dirname(__file__), 'images')
    create_directory(directory)

    fetch_nasa_epic(directory)