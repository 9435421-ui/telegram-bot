from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

ADMIN_ID = 223465437  # твой Telegram ID

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Панель администратора."""
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("⛔ Доступ запрещён.")
        return

    text = (
        "🛠 Панель администратора:\n\n"
        "/post — создать пост\n"
        "/stats — посмотреть статистику\n"
        "/broadcast — сделать рассылку"
    )
    await update.message.reply_text(text)

def setup_admin_handlers(app):
    app.add_handler(CommandHandler("admin", admin_panel))

