# app/models/game.py
from typing import List, Dict, Any
from pydantic import BaseModel

class Card(BaseModel):
    suit: str
    rank: int
    face_up: bool

class GameState(BaseModel):
    # Текущее состояние игры для клиента
    tableau: List[List[Card]]   # Списки карт в семи столбах
    stock: List[Card]           # Запас (колода)
    waste: List[Card]           # Сброс
    foundations: Dict[str, List[int]]  # Фундамент по мастям (списки достоинств карт)
    stars_balance: int          # Текущий баланс звёзд пользователя
