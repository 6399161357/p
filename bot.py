from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from google import genai

BOT_TOKEN = "8512213807:AAG4J5vUyMHHFO1-QhqhtVnXRKKoWTIhka0"
GEMINI_API_KEY = "AIzaSyDmVFDhndDRmBgXOnzpvuVH52_jJA_eKIc"

client = genai.Client(api_key=GEMINI_API_KEY)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_text
    )

    await update.message.reply_text(response.text)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot Started...")
app.run_polling()
