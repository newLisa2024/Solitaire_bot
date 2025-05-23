# Пасьянс Косынка (Telegram Mini App)

Шаблон проекта для игры «Пасьянс Косынка» с FastAPI + Telebot.

## Структура проекта

- **app/** – исходники приложения (сервер и бот).
- **tests/** – (пустой) каталог для тестов.
- **Dockerfile**, **docker-compose.yml** – для контейнеризации.
- **requirements.txt** – зависимости.

## Как запустить

1. Скопируйте проект и заполните `config.py` или переменные окружения:
   - `BOT_TOKEN` – токен Telegram бота.
   - `PAYMENT_PROVIDER_TOKEN` – токен провайдера платежей.
   - `WEBHOOK_URL` – URL для вебхуков Telegram Payments.
   - `WEBAPP_URL` – адрес веб-приложения для игры.
2. Установите зависимости:
pip install -r requirements.txt
markdown
Копировать
Редактировать
3. Запустите бота и сервер (например, с помощью Docker или вручную):
docker-compose up --build
markdown
Копировать
Редактировать
4. Откройте чат с ботом и отправьте `/start`, чтобы начать игру.

## О функционале

- **Регистрация:** через Telegram Login Widget (handled by `/api/auth/login`).
- **Игра:** механика «Пасьянс Косынка» реализуется в `core/game_logic.py`. Данные о состоянии передаются через API.
- **Подсказки:** платные, снимают 1 звезду за подсказку (маршрут `/api/game/hint`).
- **Платежи:** интегрированы через Telegram Payments API (`/api/payments/webhook`).
- **Веб-приложение:** простой фронтенд на HTML/JS с использованием `Telegram.WebApp.sendData` для взаимодействия.

> **Примечание:** Это шаблон проекта с упрощённой логикой. Для реального использования необходима д