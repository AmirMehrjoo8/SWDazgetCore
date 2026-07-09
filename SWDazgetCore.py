from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import asyncio
import os


TOKEN = "8523281660:AAHDY-fN-Xyjft0eGKwX2-adF1I9-cYTugY"                    # توکن ربات
CHANNEL_ID = -1002642052817                   # آیدی کانال (با -100 شروع بشه)



async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        message = update.message
        if message is None:
            return

        await message.forward(chat_id=CHANNEL_ID)
        print(f"پیام از {message.chat.id} فوروارد شد.")

    except Exception as e:
        print(f"خطا: {e}")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.ALL, forward_message))

    print("ربات شروع شد...")
    app.run_polling()

if __name__ == "__main__":
    main()