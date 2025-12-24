import os
import requests
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
TOKEN = os.getenv("BOT_TOKEN")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ref = context.args[0] if context.args else ""
    context.user_data["ref"] = ref
    keyboard = [[KeyboardButton("📱 Share Phone Number", request_contact=True)]]
    await update.message.reply_text(
        "👋 Welcome to Income Pathshala\n\n"
        "💰 Join ₹200 | Earn ₹150 per referral\n\n"
        "➡ Continue karne ke liye phone number share karein",
        reply_markup=ReplyKeyboardMarkup(
            keyboard, resize_keyboard=True, one_time_keyboard=True
        ),
    )
async def save_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    user = update.message.from_user
    data = {
        "name": user.first_name,
        "username": user.username,
        "phone": contact.phone_number,
        "telegram_id": user.id,
        "ref": context.user_data.get("ref", ""),
    }
    # Abhi sirf confirmation
    await update.message.reply_text(
        "✅ Details received!\nAdmin approval ke baad earning start hogi."
    )
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.CONTACT, save_contact))

    app.run_polling()

if __name__ == "__main__":
    main()
