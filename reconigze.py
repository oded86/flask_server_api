
from azure.cognitiveservices.vision.computervision import ComputerVisionClient

from msrest.authentication import CognitiveServicesCredentials
import cv2
from PIL import Image
from sendMessage import sendMessage,sendMessageDogCat
from urlMap import getMAp
from yolo_recongized.yolo_dection import yolo_dection_dogcat
fire = 'https://instaface.co.il/wp-content/uploads/2020/03/%D7%9C%D7%94%D7%A4%D7%95%D7%9A-%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%9C%D7%A6%D7%99%D7%95%D7%A8-7-1.png'
key = "7b26cb22cdf14b07b35af19d57471f5f"
endpoint = "https://sagiekadomain.cognitiveservices.azure.com/"


def config(img):
    print(img)
    fire = 'https://instaface.co.il/wp-content/uploads/2020/03/%D7%9C%D7%94%D7%A4%D7%95%D7%9A-%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%9C%D7%A6%D7%99%D7%95%D7%A8-7-1.png'
    # network to api of Microsoft
    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
    # collect all refrens of image
    des = client.describe_image(img)
    print('the des:', des)
    return des


fire_text = ''
percent = ''
flooded_text=''

def reconigze_flooded(img, adressF):
    adress = adressF
    print("statring reconigze_flooded func..................")
    print(img)
    des = config(img)
    print(des)
    # reconigze the flooded image
    for caption in des.captions:
        # get image of description the image
        flooded_text = caption.text
        # percent of fire image
        percent = caption.confidence

        if 'flooded' in flooded_text:
            print('true')
            mapLocation = getMAp(adress)
            sendMessage(flooded_text+' '+str(percent),
                        ' the loaction: ' + mapLocation)
            return flooded_text+' '+str(percent)
        else:
            print('false')
            return 'Hello , this is not reconigzed a flooded this: '+flooded_text

def reconigze_fire(img, adressF):
    adress = adressF

    print("statring reconigze_fire func..................")
    print(img)

    des = config(img)
    print(des)
    # reconigze the fire image
    for caption in des.captions:
        # get image of description the image
        fire_text = caption.text
        # percent of fire image
        percent = caption.confidence

        if 'fire' in fire_text:
            print('true')
            mapLocation = getMAp(adress)
            sendMessage(fire_text+' '+str(percent),
                        ' the loaction: ' + mapLocation)
            return fire_text+' '+str(percent)
        else:
            print('false')
            return 'Hello , this is not reconigzed a fire this: '+fire_text
def reconigze_dogcat(img, adressF):
    adress = adressF
    print("statring reconigze_dogcat func..................")
    fire_text=yolo_dection_dogcat()
    print(fire_text)
    if 'not' in fire_text:
        print('false')
        return 'Hello , '+fire_text
    else:
        print('true')
        # mapLocation = getMAp(adress)
        sendMessageDogCat(fire_text+' '+str(percent),
                        adress)
        return fire_text+' '+str(percent)

