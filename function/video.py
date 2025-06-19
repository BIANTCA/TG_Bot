import json
import threading
import requests
import traceback
import telebot
import function.tools as tools
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

setting = tools.read_file('./setting.json')
token_api = setting['bot']['api']
bot = telebot.TeleBot(token_api)
bot_detail = bot.get_me()
bot_username = bot_detail.username
channel_id = setting["channel"]["id"][1:]

def auto_post():
 try:
  post_c()
 except Exception as e:
  tools.log_error(e)
 nextPostTime = tools.random_int(2,10)
 tools.logging('post_c :'+ str(nextPostTime))
 threading.Timer(nextPostTime, lambda: auto_post()).start()
 
def post_c():
 video = tools.read_file("./documents/video.json")
 tittle = tools.read_file("./documents/tittle.json")
 thumbnail = tools.read_file("./documents/thumbnail.json")
 tittle_int = tools.random_int(0, len(tittle) - 1)
 video_int = tools.random_int(0, len(video) - 1)
 thumbnail_int = tools.random_int(0, len(thumbnail) - 1)
 try:
  bot.send_photo("@"+channel_id, thumbnail[thumbnail_int]["file_id"], caption = f'https://t.me/{bot_username}?start={video[video_int]['file_unique_id']}')
 except Exception as e:
  tools.log_error(str(e))

def get_video(message):
 tools.logging('get_video: '+ str(message.chat.id))
 videoList = tools.read_file('./documents/videoList.json')
 chat_id = message.chat.id
 command, params = tools.params_detector(message.text)
 gc_status = bot.get_chat_member('@'+channel_id, chat_id)
 if gc_status.status not in ["creator", "administrator", "member"]:
  return not_joined(message, channel_id)
 videoList = tools.read_file('./documents/videoList.json')
 if params in videoList:
  tools.send_video(chat_id, videoList[params]['file_id'])
 else:
  bot.send_message(chat_id, "link tidak valid")

def not_joined(message, channel_username):
 tools.logging('not_joined: '+ str(message.chat.id))
 command, params = tools.params_detector(message.text)
 chat_id = message.chat.id
 caption = f"Anda belum berlangganan di channel kami, harap untuk melakukan langganan di channel kami secara gratis\n\n>>> @{channel_username}\n\njika anda sudah berlangganan, anda bisa mengulang menekan link di channel kami\nklik lagi >>> [dapatkan video](https://t.me/{bot_username}?start={params})\n>>> ({str(tools.random_int(10000,99999))})"
 
 markup = InlineKeyboardMarkup()
 markup.row_width = 1
 markup.add(InlineKeyboardButton(channel_username, url=f"https://t.me/{channel_username}"))
 
 bot.send_message(chat_id, caption, reply_markup=markup, parse_mode= 'markdown',disable_web_page_preview=True)