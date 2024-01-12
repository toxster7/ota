"""
import webcam
webcam.run()
"""

import camera
import machine
from config import app_config
from config import utelegram_config
from webserver import webcam
import utelegram

server = webcam()
server.run(app_config)



def get_message(message):
    bot.send(message['message']['chat']['id'], message['message']['text'].upper())

def reply_ping(message):
    print(message)
    bot.send(message['message']['chat']['id'], 'pong')


bot = utelegram.ubot(utelegram_config['token'])
bot.register('/ping', reply_ping)
bot.set_default_handler(get_message)
bot.register('/makeScreenshot',reply_ping)

print('BOT LISTENING')
bot.listen()
