import json
import threading
import string
import random
import time
import sys
import traceback
import asyncio
import os
import importlib
import function.command as cmd
import function.tools as tools

def commands(bot, message):
 ct_text = (message.content_type == "text")
 ct_photo = (message.content_type == "photo")
 ct_video = (message.content_type == "video")
 
 chat_id = message.chat.id
 message_id = message.message_id
 
 if ct_text:
  command, params = tools.params_detector(message.text)
  if command:
   cmd.command(bot, message)
   bot.delete_message(chat_id,message_id)
 
 if ct_video:
  tools.logging('ct_video: '+ str(message.chat.id))
  result = tools.append(f'./documents/video.json', message.video)
  bot.delete_message(chat_id, message.message_id)
  if result['status'] == 0:
   return bot.send_message(chat_id, result['reason'])
  message_sent = bot.send_video(chat_id, message.video.file_id)
  time.sleep(3)
  bot.delete_message(chat_id, message_sent.message_id)
 
 if ct_photo:
  tools.logging('ct_photo: '+ str(message.chat.id))
  result = tools.append(f'./documents/thumbnail.json', message.photo[0], photo = True)
  bot.delete_message(chat_id, message.message_id)
  if result['status'] == 0:
   return bot.send_message(chat_id, result['reason'])
  message_sent = bot.send_photo(chat_id, message.photo[0].file_id)
  time.sleep(3)
  bot.delete_message(chat_id, message_sent.message_id)