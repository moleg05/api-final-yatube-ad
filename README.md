# Yatube API

Yatube API — это RESTful API для социальной сети Yatube. Проект предоставляет полный набор эндпоинтов для управления публикациями, комментариями, сообществами и подписками. API использует JWT-аутентификацию и поддерживает пагинацию, поиск и фильтрацию.

## Технологии

- Python 3.9+
- Django 3.2
- Django REST Framework 3.12
- Simple JWT 5.0
- SQLite3
- Pillow

## Установка и запуск

git clone https://github.com/yourusername/yatube_api.git
cd yatube_apipython -m venv venv
source venv/bin/activate  # для Linux/macOS
# или
venv\Scripts\activate  # для Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate