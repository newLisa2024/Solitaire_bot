# app/api/payments.py
from fastapi import APIRouter
from app.db.store import get_user

router = APIRouter()

@router.post("/webhook")
async def payments_webhook(update: dict):
    """
    Обрабатывает Telegram Payments Webhook.
    Ожидается либо pre_checkout_query, либо сообщение с successful_payment.
    """
    # Если запрос - предварительная проверка оплаты
    if "pre_checkout_query" in update:
        query = update["pre_checkout_query"]
        # Всегда отвечаем положительно
        return {"ok": True}
    # Если пришло сообщение о успешной оплате
    if "message" in update and "successful_payment" in update["message"]:
        msg = update["message"]
        user = msg["from"]
        user_id = user["id"]
        amount = msg["successful_payment"]["total_amount"]  # в копейках
        # Конвертируем рубли (например) в количество звёзд
        stars = amount // 100  # 1 рубль = 1 звезда
        user_obj = get_user(user_id)
        if user_obj:
            user_obj.stars_balance += stars
        return {"status": "stars added"}
    return {"ok": True}
