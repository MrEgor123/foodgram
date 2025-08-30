## Foodgram

## Описание

**Foodgram** — это сервис для публикации рецептов.  
Пользователи могут делиться рецептами, добавлять их в избранное и формировать список покупок.  

Проект развёрнут в Docker-контейнерах и использует современный стек технологий: Django (DRF), React, Postgres и Nginx.

## Стек использованных технологий

- Python
- Django + Django REST Framework
- React
- PostgreSQL
- Gunicorn
- Nginx
- Docker + Docker Compose

## Как развернуть проект

Клонировать репозиторий:

```
git clone https://github.com/MrEgor123/foodgram
```

## Команды запуска

Создать вирутальное окружение:

```
python3 -m venv venv
```

Активировать виртуальное окржуение (Windows / Linux):

```
venv\Scripts\activate.bat
```

```
source venv/bin/activate
```

Установить зависимости:

```
pip install -r requirements.txt
```

1. Создать файл `.env` рядом с `docker-compose.yml`:

2. Запустить контейнеры:

```
docker compose up -d
```

3. Выполнить миграции и собрать статику:

```
docker compose exec backend python manage.py migrate
```

```
docker compose exec backend python manage.py collectstatic –-noinput
```

```
docker compose exec backend python manage.py createsuperuser
```

## Доступные сервисы

- Frontend: <http://localhost:8000/>  
- Админка: <http://localhost:8000/admin/>  
- Документация API (Redoc): <http://localhost:8000/api/docs/>  

## Содержимое .env

```
DB_ENGINE=
DB_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=
SECRET_KEY=
DEBUG=
```

## Автор

- Чарушин Егор
- Профиль GitHub: <https://github.com/MrEgor123>
