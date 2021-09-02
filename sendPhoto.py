import requests
import datetime
import pywhatkit as kit
from telegram.ext import Updater
# bot = telegram.Bot(token='TOKEN')
updater = Updater(
        token='1702864193:AAGj_J3ipAQ3wS0P1a2GEoEnnaAXOx9f9FY', use_context=True)
updater.bot.sendMessage(chat_id='-519827084', text='check')
updater.bot.sendPhoto(chat_id='-519827084'
            ,photo='https://merrimackvalleytma.com/wp-content/uploads/megamenu_image_2-160812-143410-emergency-notification-image.jpg')