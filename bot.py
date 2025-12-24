import os
import requests
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("📱 Share Phone Number", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=True
    )

    await update.message.reply_text(
        "👋 Welcome to Income Pathshala\n\n"
        "💰 Join ₹200 | Earn ₹150 per referral\n\n"
        "👉 Continue karne ke liye phone number share karein",
        reply_markup=reply_markup
    )

async def save_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    user = update.message.from_user

    phone = contact.phone_number
    name = user.first_name
    username = user.username

    await update.message.reply_text(
        "✅ Thanks! Your details are saved.\n\n"
        f"Name: {name}\n"
        f"Phone: {phone}"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.CONTACT, save_contact))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
