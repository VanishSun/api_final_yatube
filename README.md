# Сервис api_final_yatube

Данный сервис разработан на Django Rest Frameworks для обмена API социальной сети Yatube.

## Установка

Клонировать репозиторий и перейти в него в командной строке:
````
git clone https://github.com/VanishSun/api_final_yatube.git
cd kittygram
````
Cоздать и активировать виртуальное окружение:
````
python3 -m venv venv
. venv/bin/activate
````
Установить зависимости из файла requirements.txt:
````
python3 -m pip install --upgrade pip
pip install -r requirements.txt
````
Выполнить миграции:
````
python3 manage.py migrate
````
Запустить проект:
````
python3 manage.py runserver
````

## URL's list:

```http://127.0.0.1:8000/admin/``` - администрирование

```http://127.0.0.1:8000/api/v1/``` - API

```http://127.0.0.1:8000/api/v1/posts/``` - посты всех авторов

```http://127.0.0.1:8000/api/v1/posts/<post_id>/comments/``` - комментарии к посту

```http://127.0.0.1:8000/api/v1/groups/``` - группы

```http://127.0.0.1:8000/api/v1/follow/``` - подписки юзера

```http://127.0.0.1:8000/redoc/``` - docs проекта в формате redoc
