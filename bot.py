import telebot
import requests

TOKEN = "8392904298:AAGUugSTFOapKljHEJ753CQh2eV6hji17J4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "💀 WORM-AI: النظام متصل عبر GitHub Actions. أنا بانتظار أوامرك.")

@bot.message_handler(func=lambda message: True)
def work(message):
    bot.reply_to(message, "⚙️ يتم الآن معالجة الطلب عبر محرك WormGPT المدمج...")

bot.infinity_polling()
