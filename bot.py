import os
import requests
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
SHEET_API_URL = os.getenv("SHEET_API_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ref = context.args[0] if context.args else ""
    context.user_data["ref"] = ref

    keyboard = [[KeyboardButton("📱 Share Phone Number", request_contact=True)]]

    await update.message.reply_text(
        "👋 Welcome to Income Pathshala\n\n"
        "💰 Join ₹200 | Earn ₹150 per referral\n\n"
        "👇 Continue karne ke liye phone number share karein",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    )

async def save_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    contact = update.message.contact

    data = {
        "telegram_id": user.id,
        "name": user.first_name,
        "username": user.username or "",
        "phone": contact.phone_number,
        "referred_by": context.user_data.get("ref", "")
    }

    requests.post(SHEET_API_URL, json=data)

    await update.message.reply_text(
        "✅ Details saved successfully!\n\n"
        "💳 Ab ₹200 payment karein\n"
        "📸 Payment ke baad screenshot bhejein"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.CONTACT, save_contact))

print("Bot running...")
app.run_polling()
