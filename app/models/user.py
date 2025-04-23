# app/models/user.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    stars_balance: int = 5  # начальное количество звёзд
    # ... другие поля по необходимости (last_name, photo_url и т.д.)
