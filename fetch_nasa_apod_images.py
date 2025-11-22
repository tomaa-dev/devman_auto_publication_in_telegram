import requests
import os
from image_downloader import create_directory, download_the_image, get_file_extension
from dotenv import load_dotenv


def fetch_nasa_apod(directory, url_params):
    url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(url, params=url_params)
    response.raise_for_status()
    data_of_nasa_images = response.json()

    for url_number, img_data in enumerate(data_of_nasa_images):
        img = img_data['url']
        file_extension = get_file_extension(img)
        filename = f'nasa_apod_{url_number}{file_extension}'
        filepath_to_nasa = os.path.join(directory, filename)

        response_apod_image = requests.get(img)
        response_apod_image.raise_for_status()
        download_the_image(response_apod_image, filepath_to_nasa)


if __name__ == "__main__":
    load_dotenv()
    nasa_apod_token = os.environ["NASA_APOD_TOKEN"]

    url_params = {
        "api_key": nasa_apod_token,
        "start_date":"2025-06-10",
        "end_date": "2025-07-10",
    }

    directory = os.path.join(os.path.dirname(__file__), 'images')
    create_directory(directory)

    fetch_nasa_apod(directory, url_params)