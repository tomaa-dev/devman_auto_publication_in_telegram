# Космический Телеграм
Данный скрипт представляет собой консольное приложение на Python, которое собирает фотографии в созданные директории с использованием API и публикует их в Telegram-канал. Утилита позволяет пользователю автоматизировать сбор фотографий космоса и дальнейшую публикацию в Telegram.

## Как установить
Операционная система: любая, где доступен Python 3 (Windows, macOS, Linux). Используем 'pip' для установки зависимостей (requests, python-dotenv):
```
pip install -r requirements.txt
```
Рекомендуется использовать virtualenv/env для изоляции проекта.

## Примеры запуска скриптов

1) Автоматизация сбора SpaceX-фотографий через API в указанную директорию:

```
python python fetch_nasa_spacex_images.py
```

[![kstefana-spacex.gif](https://i.postimg.cc/HLnfG0Mz/kstefana-spacex.gif)](https://postimg.cc/Ty8kgDC5)

2) Автоматизация сбора APOD-фотографий через API в указанную директорию:

```
python python fetch_nasa_apod_images.py
```

[![kstefana-apod.gif](https://i.postimg.cc/QNFxg5nX/kstefana-apod.gif)](https://postimg.cc/0rqsP6s3)

3) Автоматизация сбора EPIC-фотографий через API в указанную директорию:

```
python python fetch_nasa_epic_images.py
```

[![kstefana-epic.gif](https://i.postimg.cc/Jnm4cdvL/kstefana-epic.gif)](https://postimg.cc/948hc1c8)

4) Публикация указанной фотографии в канал выглядит следующим образом:

```
python publish_the_image.py --photo nasa_apod_2.jpg
```

[![kstefana-1.gif](https://i.postimg.cc/vBLj9C3n/kstefana-1.gif)](https://postimg.cc/2by2N9pj)

Если “какую” не указано, публикует случайную фотографию:

```
python publish_the_image.py
```

[![kstefana-2.gif](https://i.postimg.cc/bwxF47fG/kstefana-2.gif)](https://postimg.cc/18zHqYtP)

5) Публикация всех фотографий из директории в бесконечном цикле выглядит следующим образом:

```
python publish_all_images.py
```

[![kstefana-3.gif](https://i.postimg.cc/NFbR6X0r/kstefana-3.gif)](https://postimg.cc/6427wyn9)

6) Вспомогательный скрипт предоставляет функциональность для загрузки изображений по заданным URL и сохранения их в указанной директории на локальной файловой системе. Он включает методы для создания директорий, загрузки изображений и извлечения расширений.

## Переменные окружения
Программа использует нестандартные переменные окружения для настройки. Эти переменные не могут быть автоматически обнаружены и должны быть указаны в файле `.env` перед запуском программы.

**SPACEX_ID** - уникальный идентификатор запуска SpaceX, необходим для получения информации о конкретном запуске через API SpaceX. Форматом является строка (например, `5eb87d47ffd86e000604b38b`).

**NASA_APOD_TOKEN** - Токен доступа к API NASA Astronomy Picture of the Day (APOD), необходим для выполнения запросов к API и получения данных о астрономическом изображении. Форматом является строка (например, `goXWkWeKl7JdgJuct2NtY3vU4Utbr8pVJxG2qNtT` или демонстрационный ключ `DEMOKEY`). Без этого токена функции, связанные с API запросами, не будут работать, и программа завершит выполнение с ошибкой.

**TELEGRAM_SPACE_TOKEN** - токен доступа к Telegram-боту, необходимый для выполнения запросов к HTTP API. Форматом является строка (например, `9253428621:AAFTmI5GYUN3Zd3lfYOWLgbNIS036CNuZQo`). Без этого токена бот не будет работать, и программа завершит выполнение с ошибкой.

**TELEGRAM_ID** - ссылка к Telegram-каналу, чтобы направлять туда запросы. Форматом является строка (например, `@kstefana`).
