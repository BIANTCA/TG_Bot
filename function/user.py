import function.tools as tools
import json

def user_checker(bot, message):
 chat_id = message.chat.id
 file = tools.read_file('./documents/user.json')
 if str(chat_id) not in file:
  bot.send_message(chat_id, welcome_message())
  file[chat_id] = vars(message.from_user)
  tools.dump_file(file, './documents/user.json')

def welcome_message():
 message = (
  "👋 Hai Kamu!\n\n"
  "Selamat datang di bot ini. Saya di sini untuk membantumu.\n\n"
  "🔹 Gunakan /help untuk melihat daftar perintah.\n"
  "🔹 Kirim /bug (pesannya) untuk komplain terhadap bug pada bot.\n\n"
  "Semoga harimu menyenangkan!"
 )
 return message