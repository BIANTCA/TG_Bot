import json
import threading
import string
import random
import time
import sys
import traceback
import os
import importlib
import function.user as user
import function.video as fvideo
import function.tools as tools

def command(bot, message):
 setting = tools.read_file('./setting.json')
 command, params = tools.params_detector(message.text)
 is_owner = (message.chat.id in setting["owner"])
 message_id = message.message_id
 from_id = message.from_user.id
 chat_id = message.chat.id
 
 if command == "start":
  tools.logging('cmd_start: '+ str(message.chat.id))
  user.user_checker(bot, message)
  if params:
   fvideo.get_video(message)
 if command == "stopbot" and is_owner:
  tools.logging('cmd_stopbot: '+ str(message.chat.id))
  bot.send_message(chat_id, "stoping...")
  bot.stop_polling()
  os._exit(0)
 if command == "send_message" and is_owner:
  tools.logging('send_message: '+ str(message.chat.id))
  params2 = params.split(" ")
  tools.send_message(params2[0], params.split(params2[0] + " ")[1])
 if command == "post" and is_owner:
  tools.logging('cmd_post: '+ str(message.chat.id))
  fvideo.auto_post()