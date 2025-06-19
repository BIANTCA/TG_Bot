import requests
import json
import string
import telebot
import os
import time
import traceback
import importlib
import random
import function.tools as tools

setting = tools.read_file('./setting.json')
token_api = setting['bot']['api']

def check(token_api):
 url = f'https://api.telegram.org/bot{token_api}/getMe'
 response = requests.get(url)
 data = response.json()
 
 if response.ok:
  print(f"{data['result']['username']}...\nStarting...")
  bot = telebot.TeleBot(token_api)
  
  @bot.message_handler(content_types= tools.all_content())
  def echo_all(message):
   try:
    import command
    importlib.reload(command)
    command.commands(bot, message)
   except Exception as e:
    tools.log_error(str(e))
  
  try:
   code = start_setting()
   bot.send_message(setting['owner'][0], 'start code: '+ str(code))
   bot.infinity_polling()
  except Exception as e:
   error_msg = traceback.format_exc()
   tools.log_error(error_msg)
 else:
  print(f"Gagal mendapatkan informasi bot [ {token_api} ]")

def start_setting():
 code = tools.count_files('./documents/logging/')
 setting['bot']['code'] = str(code)
 tools.dump_file(setting,'./setting.json')
 tools.logging('bot starting...')
 return code

check(token_api)