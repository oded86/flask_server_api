#from pyrebase import pyrebase
import pyrebase
# api config to firebase google.
config = {
    "apiKey": "AIzaSyDcfyRcyxyH4YYihWEV63tjEkBqC384564",
    "authDomain": "uploadpyfire.firebaseapp.com",
    "projectId": "uploadpyfire",
    "databaseURL": "https://uploadpyfire.firebaseio.com",
    "storageBucket": "uploadpyfire.appspot.com",
    "messagingSenderId": "541732097679",
    "appId": "1:541732097679:web:44566f5c1ebb0ff1816afa",
    "measurementId": "G-M3RWNWE4XW"
}


def getUrl(adressF):
    adress = adressF
    print("statring getURL func..................")
    # save image in path in firebase
    path_on_cloud = 'images/fire.jpg'
    # name of image that save in the server
    path_local = "fire.jpg"
    # connect to firebase
    firebase = pyrebase.initialize_app(config)
    # connect to storage into to storage
    storge = firebase.storage()
    # put the image into storge in firebase storge
    storge.child(path_on_cloud).put(path_local)
    # get url from firebase to send to rconigze_fire
    img = storge.child(path_on_cloud).get_url(None)
    # print(adress)
    # call to reconigze_fire function
    result = [img, adress]
    return result
