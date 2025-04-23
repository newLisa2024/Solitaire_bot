# app/api/auth.py
from fastapi import APIRouter, Request
from app.models.user import User
from app.db.store import create_user, get_user

router = APIRouter()

@router.post("/login")
async def login(data: dict):
    """
    Обрабатывает данные из Telegram Login Widget (передаются через JS).
    Пример data: {'id':12345, 'username':'user', 'first_name':'Имя', 'hash':'...', ...}
    """
    # TODO: Проверить подпись Telegram (для шаблона опустим проверку)
    user_id = data.get("id")
    username = data.get("username")
    first_name = data.get("first_name")
    if not user_id:
        return {"error": "Неверные данные аутентификации"}
    user = get_user(user_id)
    if not user:
        user = User(id=user_id, username=username, first_name=first_name)
        create_user(user)
    return {"status": "ok", "user": user.dict()}
