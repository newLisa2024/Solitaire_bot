# app/api/game.py
from fastapi import APIRouter, Depends
from app.db.store import get_user, get_or_create_game, end_game
from app.core.game_logic import SolitaireGame
from app.models.game import GameState, Card
from typing import Dict

router = APIRouter()

def get_current_user(user_id: int = None):
    """
    Заглушка для получения текущего пользователя по user_id.
    На практике user_id можно передавать в заголовке или через OAuth токен.
    """
    if user_id is None:
        return None
    return get_user(user_id)

@router.get("/state")
async def get_state(user_id: int):
    """
    Возвращает текущее состояние игры для пользователя.
    """
    user = get_current_user(user_id)
    if not user:
        return {"error": "Пользователь не найден"}
    game = get_or_create_game(user.id)
    state_dict = game.to_dict()
    state = GameState(**state_dict, stars_balance=user.stars_balance)
    return state

@router.post("/move")
async def make_move(user_id: int, move: Dict):
    """
    Выполняет ход. Пример входных данных: {'from': 'tableau1', 'to': 'foundationHearts'}.
    Реальная логика хода упрощена.
    """
    user = get_current_user(user_id)
    if not user:
        return {"error": "Пользователь не найден"}
    game = get_or_create_game(user.id)
    # Здесь нужно реализовать настоящую механику ходов.
    from_pile = move.get("from")
    to_pile = move.get("to")
    # Допустим, мы всегда разрешаем ход:
    # game.move_card(from_pile, to_pile, ...)
    return {"status": "move accepted", "from": from_pile, "to": to_pile}

@router.post("/hint")
async def get_hint(user_id: int, hint_type: str):
    """
    Даёт подсказку пользователю. Снимает звезду за подсказку.
    hint_type может быть одним из: 'target', 'refresh', 'draw', 'shuffle', 'redeal'
    """
    user = get_current_user(user_id)
    if not user:
        return {"error": "Пользователь не найден"}
    cost = 1  # стоимость подсказки в звёздах
    if user.stars_balance < cost:
        return {"error": "Недостаточно звёзд"}
    user.stars_balance -= cost
    # Простая заглушка подсказки:
    message = f"Подсказка ({hint_type}): попробуйте ход."
    return {"hint": message, "stars_balance": user.stars_balance}

@router.post("/end")
async def end_current_game(user_id: int):
    """
    Завершает текущую игру пользователя.
    """
    user = get_current_user(user_id)
    if not user:
        return {"error": "Пользователь не найден"}
    end_game(user.id)
    return {"status": "game ended"}
