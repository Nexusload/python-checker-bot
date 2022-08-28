#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Dhaka'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 15600540, #get it from https://my.telegram.org/auth
    api_hash="0531d49b459b73c81c7fed842ac97ba6", #get it from https://my.telegram.org/auth
    bot_token="5726914986:AAGXIeu4S0t9Jrm1rTdVGsOw-vrYitBL6Og", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
