# Yatube API
API социальной сети блогеров.
## Функционал:
Регистрация, создание и редактирование постов, добавление изображения, комментирование. Используется пагинация постов, кэширование главной страницы.

#### Стек:
Python3, Django 2.2, SimpleJWT, pytest
## How start project:

Clone a repository and go to command line:

```sh
git clone git@github.com:menyanet73/api_final_yatube.git
```

```sh
cd api_final_yatube
```

Create and activate virtual environment:

```sh
python3 -m venv env
```
For Windows:
```sh
source env/Scripts/activate  
```
For Linux:
```sh
source env/bin/activate  
```

Install dependencies from a file requirements.txt:

```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

Apply migrations:

```sh
python3 manage.py migrate
```

Start project:

```sh
python3 manage.py runserver
```

### Documentation of API will be aviable in
```sh
127.0.0.1:8000/redoc/
```

### Requests:
##### Get posts
```sh
127.0.0.1:8000/api/v1/posts/
```
| Endpoints | Response |
| ------ | ------ |
| [/api/v1/posts/] | All posts. GET, POST. |
| [/api/v1/posts/1/] | First id post. GET, PUT, PATCH, DELETE. |
| [/api/v1/posts/1/comments/] | Comments for post. GET, POST. |
| [/api/v1/posts/1/comments/1/] | Comment, in first post. GET, PUT, PATCH, DELETE.|
| [/api/v1/groups/] | Groups list. GET |
| [/api/v1/groups/1/] | First group. GET |
| [/api/v1/follow/] | Follow list, for request user. GET, POST. |
| [/api/v1/follow/1/] | First follow. GET, PUT, PATCH, DELETE. |
| [/api/v1/users/] | Users list. GET, CREATE |
| [/api/v1/jwt/create/] | JWT Token create. POST, |


[/api/v1/posts/]: <https://127.0.0.1/api/v1/posts/>
[/api/v1/posts/1/]: <https://127.0.0.1/api/v1/posts/1/>
[/api/v1/posts/1/comments/]: <https://127.0.0.1/api/v1/posts/1/comments/>
[/api/v1/posts/1/comments/1/]: <https://127.0.0.1/api/v1/posts/1/comments/1/>
[/api/v1/groups/]: <https://127.0.0.1/api/v1/groups/>
[/api/v1/groups/1/]: <https://127.0.0.1/api/v1/groups/1/>
[/api/v1/follow/]: <https://127.0.0.1/api/v1/follow/>
[/api/v1/follow/1/]: <https://127.0.0.1/api/v1/follow/1/>
[/api/v1/users/]: <https://127.0.0.1/api/v1/users/>
[/api/v1/jwt/create/]: <https://127.0.0.1/api/v1/jwt/create/>
