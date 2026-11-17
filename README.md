# HotelLinks

Короткие ссылки для электронного справочника гостя: меню, правила проживания, маршруты прогулок и контакты ресепшена. Введите адрес документа в веб-форме или через API и получите удобный адрес для памятки гостю. При переходе открывается исходный документ. Авторизация и управление бронированиями не предусмотрены.

Автор адаптации и доработок — Рябуха Олег.

Python 3.11, Flask, SQLAlchemy, SQLite, Flask-WTF и Alembic. Модуль приложения `yacut`, таблица и API сохранены, схема БД не менялась.

## Запуск

Из каталога проекта в PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
Copy-Item .env.example .env
# Замените SECRET_KEY собственной случайной строкой.
.\.venv\Scripts\python -m flask db upgrade
.\.venv\Scripts\python -m flask run --port 8005
```

Главная страница: <http://127.0.0.1:8005/>. Linux/macOS: `python3.11 -m venv .venv` и `.venv/bin/python`. Команды выполняются из корня: там читается `.env` и создается `db.sqlite3`. Без SECRET_KEY ключ выбирается случайно на процесс.

В форме укажите URL документа и, по желанию, короткое имя `menu`, `rules`, `walk` или `contacts`. Допустимы 1–16 латинских букв и цифр. Без имени генерируются шесть случайных символов. Занятое имя нельзя использовать повторно. Сервис не проверяет доступность конечного сайта. Сервис публичный: размещайте его в доверенной сети или настройте доступ на уровне обратного прокси.

## API

`POST /api/id/`:

```json
{"url":"https://hotel.example.com/guest/restaurant/menu.pdf","custom_id":"menu"}
```

Ответ 201:

```json
{"url":"https://hotel.example.com/guest/restaurant/menu.pdf","short_link":"http://127.0.0.1:8005/menu"}
```

`GET /api/id/menu/` возвращает исходный URL; `GET /menu` перенаправляет на него со статусом 302. `custom_id` можно опустить или передать пустым. Контракт и ошибки — `openapi.yml`.

`examples/guest_links.json` содержит примеры запросов. `hotel.example.com` — демонстрационный домен: замените адреса реальными страницами своего справочника.

## Проверки

```powershell
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
.\.venv\Scripts\python -m pytest
.\.venv\Scripts\python -m flask db current
```

Результаты проверок — `REVIEW.md`. Сведения о лицензии — `NOTICE.md`.
