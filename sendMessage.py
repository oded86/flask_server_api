import requests
import datetime
# import pywhatkit as kit
from telegram.ext import Updater
# bot = telegram.Bot(token='TOKEN')


def sendMessage(message, adress):
    print("statring sendMessage func..................")
    pic = open('./fire.jpg', 'rb')
    # send message to telgram
    updater = Updater(
        token='1702864193:AAGj_J3ipAQ3wS0P1a2GEoEnnaAXOx9f9FY', use_context=True)
    updater.bot.sendPhoto(
        chat_id='-519827084', photo='https://merrimackvalleytma.com/wp-content/uploads/megamenu_image_2-160812-143410-emergency-notification-image.jpg')
    updater.bot.sendMessage(chat_id='-519827084',
                            text='the deatils: '+message+' in the loccation:')
    # updater.bot.sendMessage(chat_id='-519827084', text=adress)
    updater.bot.sendLocation(chat_id='-519827084',
                             latitude=32.0123111,
                             longitude=34.7947405)
    updater.bot.send_photo(chat_id='-519827084', photo=pic)

    # how to tag any image using deep learning python
    # *****send_to_whatsapp****
    # now = datetime.datetime.now()
    # hour = now.hour
    # minute = now.minute
    # kit.sendwhatmsg("+972542025665",
    #                 message, hour, minute+1)


def sendMessageDogCat(message, adress):
    pic = open('./example.png', 'rb')
    print("statring sendMessage func..................")
    print(float(adress[0]))
    print(float(adress[1]))
    # send message to telgram
    updater = Updater(
        token='1702864193:AAGj_J3ipAQ3wS0P1a2GEoEnnaAXOx9f9FY', use_context=True)
    updater.bot.sendPhoto(
        chat_id='-519827084', photo='https://merrimackvalleytma.com/wp-content/uploads/megamenu_image_2-160812-143410-emergency-notification-image.jpg')
    updater.bot.sendMessage(chat_id='-519827084',
                            text='The details: the system has recognized a dog in the following location:')
    # updater.bot.sendMessage(chat_id='-519827084', text=adress)
    updater.bot.sendLocation(chat_id='-519827084',
                             latitude=float(adress[0]),
                             longitude=float(adress[1]))

    updater.bot.send_photo(chat_id='-519827084', photo=pic)
