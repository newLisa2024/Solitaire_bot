# app/config.py
import os

# Получаем настройки из переменных окружения или используем значения по умолчанию
BOT_TOKEN = os.getenv("BOT_TOKEN", "<YOUR_TELEGRAM_BOT_TOKEN>")
PAYMENT_PROVIDER_TOKEN = os.getenv("PAYMENT_PROVIDER_TOKEN", "<YOUR_PAYMENT_PROVIDER_TOKEN>")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://your_domain.com/api/payments/webhook")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://your_domain.com/webapp/index.html")
PORT = int(os.getenv("PORT", 8000))
