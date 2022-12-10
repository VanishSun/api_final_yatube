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

```http://127.0.0.1:8000/api/v1/posts/``` - посты всех авторов; при указании параметров limit и offset ответ будет работтать с пагинацией.

```http://127.0.0.1:8000/api/v1/posts/<post_id>/``` - пост найденный по id

```http://127.0.0.1:8000/api/v1/posts/<post_id>/comments/``` - комментарии к посту

```http://127.0.0.1:8000/api/v1/posts/<post_id>/comments/<comments_id>/``` - комментарий к посту найденный по id

```http://127.0.0.1:8000/api/v1/groups/``` - группы

```http://127.0.0.1:8000/api/v1/follow/``` - подписки юзера

```http://127.0.0.1:8000/redoc/``` - docs проекта в формате redoc

## Примеры тветов API:

```http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2```
#### Ответ:
```
{
    "count": 6,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2",
    "results": [
        {
            "id": 3,
            "author": "string",
            "text": "string",
            "pub_date": "2022-12-07T14:10:40.732810Z",
            "image": "string",
            "group": 0
        },
        {
            "id": 4,
            "author": "string",
            "text": "string",
            "pub_date": "2022-12-07T14:20:04.907578Z",
            "image": "string",
            "group": 0
        }
    ]
}
```

```http://127.0.0.1:8000/api/v1/posts/3/comments/<comments_id>/```
#### Ответ:
```
{
    "id": 3,
    "author": "string",
    "text": "string",
    "created": "2022-12-07T14:11:49.270003Z",
    "post": 3
}
```
