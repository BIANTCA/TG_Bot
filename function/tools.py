import random
import os
import requests
import threading
import time
import json
import telebot
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def read_file(path):
 if not os.path.exists(path):
  return None
 with open(path) as json_file:
  return json.load(json_file)

setting = read_file('./setting.json')
token_api = setting['bot']['api']

def dump_file(file, path):
 if not os.path.exists(path):
  return None
 with open(path, 'w') as json_file:
  json.dump(file, json_file, indent=1)
  return "succes"

def random_string(length):
 characters = string.ascii_lowercase + string.digits
 result = ''
 for _ in range(length):
  random_index = random.randint(0, len(characters) - 1)
  result += characters[random_index]
 return result

def random_int(min_value, max_value):
 return random.randint(min_value, max_value)
 
def params_detector(messageText):
 if '/' in messageText:
  command, *params = messageText.split('/')[1].split(maxsplit=1)
  command = command.strip()
  params = messageText.split(command + " ")[1] if params else None
  return command, params
 return None, None

def all_content():
 all_menu = ["text","audio","document","animation","game","photo","sticker","video","video_note","voice","location","contact","venue","dice","new_chat_members","left_chat_member","new_chat_title","new_chat_photo","delete_chat_photo","group_chat_created","supergroup_chat_created","channel_chat_created","migrate_to_chat_id","migrate_from_chat_id","pinned_message","invoice","successful_payment","connected_website","poll","passport_data","proximity_alert_triggered","video_chat_scheduled","video_chat_started","video_chat_ended","video_chat_participants_invited","web_app_data","message_auto_delete_timer_changed","forum_topic_created","forum_topic_closed","forum_topic_reopened","forum_topic_edited","general_forum_topic_hidden","general_forum_topic_unhidden","write_access_allowed","user_shared","chat_shared","story"]
 return all_menu

def log_error(error_message):
 print(error_message)
 file_path = 'error.log'
 waktu = time.strftime("%Y-%m-%d %H:%M:%S")
 with open(file_path, 'a') as f:
  f.write(f"[{waktu}] {str(error_message)}\n")

def logging(message):
 setting = read_file('setting.json')
 file_path = f'./documents/logging/{setting['bot']['code']}.log'
 waktu = time.strftime("%Y-%m-%d %H:%M:%S")
 with open(file_path, 'a') as f:
  f.write(f"[{waktu}] {str(message)}\n")

lock = threading.Lock()
def append(path, nfile, photo = None):
 file = read_file(path)
 mfile = read_file('./documents/videoList.json')

 if not photo:
  thumbnail_data = {
   'file_id': nfile.thumbnail.file_id,
   'file_unique_id': nfile.thumbnail.file_unique_id,
   'width': nfile.thumbnail.width,
   'height': nfile.thumbnail.height,
   'file_size': nfile.thumbnail.file_size
  }

 file_data = {
  'file_id': nfile.file_id,
  'file_unique_id': nfile.file_unique_id,
  'file_size': nfile.file_size
 }

 with lock:
  if nfile.file_id in str(file):
   return {'status': 0, 'reason': 'file sudah tersedia'}
  if not photo:
   file_data['duration'] = nfile.duration
   mfile[nfile.file_unique_id] = file_data
   dump_file(mfile, './documents/videoList.json')
  file.append(file_data)
  with open(path, 'w') as json_file:
   json.dump(file, json_file, indent=1)
  return {'status': 1, 'file':file}

def send_message(chat_id, message, parse_mode= None, markup= None):
 url = f"https://api.telegram.org/bot{token_api}/sendMessage"
 payload = {
  'chat_id': chat_id,
  'text': message + " ("+ str(random_int(10000,99999)) +")",
  'parse_mode': parse_mode,
  'reply_markup': markup
 }
 return send_requests(url, payload)

def send_video(chat_id, video_file_id, caption=None, parse_mode=None, markup= None):
 url = f"https://api.telegram.org/bot{token_api}/sendVideo"
 payload = {
  'chat_id': chat_id,
  'video': video_file_id,
  'caption': f"{caption} ("+ str(random_int(10000,99999)) +")" if caption else f"("+ str(random_int(10000,99999)) +")",
  'parse_mode': parse_mode,
  'reply_markup': markup
 }
 return send_requests(url, payload)

def send_photo(chat_id, image_file_id, caption=None, parse_mode=None, markup= None):
 url = f"https://api.telegram.org/bot{token_api}/sendPhoto"
 payload = {
  'chat_id': chat_id,
  'photo': image_file_id,
  'caption': f"{caption} ("+ str(random_int(10000,99999)) +")" if caption else f"("+ str(random_int(10000,99999)) +")",
  'parse_mode': parse_mode,
  'reply_markup': markup
 }
 return send_requests(url, payload)

def send_requests(url, payload= None):
 response = requests.post(url, data=payload)
 if response.status_code == 200:
  return response.json()
 else:
  try:
   error_map = response.json()
   map_formarted = map_formarter(error_map)
   log_error(f"#Error: {map_formarted}\n\nurl: {url}\npayload:\n{map_formarter(payload)}\n")
  except Exception as e:
   log_error(e)
   return f"Error: {e}"

def map_formarter(selected_map):
 formatted_string = "\n".join([f"{key.lower()}: {str(value).lower()}" for key, value in selected_map.items()])
 return formatted_string

def count_files(folder_path):
 try:
  files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
  return len(files)
 except FileNotFoundError:
  return 0