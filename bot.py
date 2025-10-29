import os
from dotenv import load_dotenv
from telegram import __version__ as TGVER
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from admin_panel import setup_admin_handlers  # ← импорт в начале!

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or "ВАШ_ТОКЕН"

# --- Обработчики команд пользователя ---
async def start(update, context):
    """Приветствие для новых пользователей и приглашение подписаться на канал."""
    text = (
        "Приветствую! 👋\n\n"
        "Я бот канала @ii_vsedlyateby — публикую материалы про ИИ и продвижение.\n\n"
        "• /help — краткая справка\n"
        "• /admin — панель администратора (только для админа)\n\n"
        "Если хочешь получать автообновления — напиши /start в личке."
    )
    await update.message.reply_text(text)

async def help_command(update, context):
    """Краткая справка по возможностям бота."""
    text = (
        "📘 Помощь:\n\n"
        "/start — приветствие и инструкция\n"
        "/help — эта справка\n"
        "/admin — панель администратора (только для админа)\n\n"
        "Бот публикует посты и может генерировать контент по заданной теме."
    )
    await update.message.reply_text(text)

async def echo_default(update, context):
    """Простой автоответ на любые текстовые сообщения."""
    await update.message.reply_text("Спасибо за сообщение! Мы свяжемся с вами вскоре.")

# --- Создание приложения ---
def build_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # публичные команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # простой ответ на текст
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_default))

    # подключаем админ-панель (в admin_panel.py)
    setup_admin_handlers(app)

    return app

if __name__ == "__main__":
    application = build_app()
    print("🤖 Бот запущен и работает...")
    application.run_polling()
