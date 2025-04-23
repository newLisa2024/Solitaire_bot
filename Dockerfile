# Используем официальный образ с Python
FROM python:3.10-slim

WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Открываем порт для FastAPI
EXPOSE 8000

# Команда запуска: одновременно бот и сервер
CMD ["sh", "-c", "python app/telegram/bot.py & uvicorn app.main:app --host 0.0.0.0 --port 8000"]
