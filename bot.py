import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("📱 Share Phone Number", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "👋 Welcome to Income Pathshala\n\n"
        "📌 Continue karne ke liye apna phone number share karein",
        reply_markup=reply_markup
    )

async def save_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    await update.message.reply_text(
        f"✅ Thanks!\n\n"
        f"Name: {contact.first_name}\n"
        f"Phone: {contact.phone_number}"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.CONTACT, save_contact))

    app.run_polling()

if __name__ == "__main__":
    main()
