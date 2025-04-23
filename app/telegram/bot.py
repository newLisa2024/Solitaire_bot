# app/telegram/bot.py
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from app.config import BOT_TOKEN, WEBAPP_URL
from app.db.store import get_user, create_user

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    """
    Приветственное сообщение. Отправляем пользователю кнопку для запуска веб-приложения.
    """
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    # Создаём пользователя, если ещё нет
    if get_user(user_id) is None:
        from app.models.user import User
        create_user(User(id=user_id, username=username, first_name=first_name))
    # Кнопка с веб-приложением
    web_app = WebAppInfo(url=WEBAPP_URL)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Играть в Пасьянс 🎲", web_app=web_app))
    bot.send_message(chat_id=user_id, text="Добро пожаловать! Нажмите кнопку ниже, чтобы запустить игру.",
                     reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Это шаблон бота для пасьянса Косынка. Используйте /start, чтобы начать игру.")

# Здесь можно добавить команды для проверки баланса, пополнения и т.д.
# Например:
@bot.message_handler(commands=['balance'])
def balance(message):
    user = get_user(message.from_user.id)
    if not user:
        bot.reply_to(message, "Пользователь не зарегистрирован.")
    else:
        bot.reply_to(message, f"У вас {user.stars_balance} звёзд(ы).")

# Запуск Long Polling
if __name__ == "__main__":
    print("Bot polling...")
    bot.infinity_polling()
