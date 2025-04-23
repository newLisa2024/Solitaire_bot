# app/main.py
from fastapi import FastAPI
from app.api import auth, game, payments
from app.config import PORT

app = FastAPI()

# Регистрируем маршруты
app.include_router(auth.router, prefix="/api/auth")
app.include_router(game.router, prefix="/api/game")
app.include_router(payments.router, prefix="/api/payments")

@app.get("/")
async def root():
    return {"message": "Telegram Solitaire API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=True)
