# app/db/store.py
from app.models.user import User
from app.core.game_logic import SolitaireGame

# Хранилище пользователей и игр в памяти (словарём)
USERS: dict[int, User] = {}
GAMES: dict[int, SolitaireGame] = {}  # ключ - user_id

def create_user(user: User):
    USERS[user.id] = user

def get_user(user_id: int) -> User:
    return USERS.get(user_id)

def get_or_create_game(user_id: int) -> SolitaireGame:
    if user_id not in GAMES:
        GAMES[user_id] = SolitaireGame()
    return GAMES[user_id]

def end_game(user_id: int):
    if user_id in GAMES:
        del GAMES[user_id]
