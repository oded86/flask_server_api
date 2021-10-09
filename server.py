from flask import Flask, request, jsonify
import json
from downloadPic import download
from upload_File_Firebase import getUrl
from reconigze import reconigze_flooded, reconigze_fire, reconigze_dogcat, reconigze_dogcatIn
import smtplib, ssl
from email.mime.text import MIMEText


from datetime import datetime

now = datetime.now() # current date and time


app = Flask(__name__)

# open server with flask api


@app.route("/fire", methods=['POST'])
def home():
 # get data from post parmeter
    data = request.stream.read()
    # change for json format
    objectData = json.loads(data)
    # get a adress data
    adress = objectData["adress"]
    # get a url image data
    urlImage = objectData["url"]
    # download the image to the server
    result_Download = download(urlImage, adress)
    # get url for do reconigze for fire
    result_getUrl = getUrl(result_Download)
    # return if it is fire
    return reconigze_fire(result_getUrl[0], result_getUrl[1])


@app.route("/flood", methods=['POST'])
def home2():
    # get data from post parmeter
    data = request.stream.read()
    # change for json format
    objectData = json.loads(data)
    # get a adress data
    adress = objectData["adress"]
    # get a url image data
    urlImage = objectData["url"]
    # download the image to the server
    result_Download = download(urlImage, adress)
    # get url for do reconigze for flooded
    result_getUrl = getUrl(result_Download)
    # return if it is flooded
    return reconigze_flooded(result_getUrl[0], result_getUrl[1])


@app.route("/dogcat", methods=['POST'])
def home3():
    print('Api:dogcat-'+str(now))
    # get data from post parmeter
    data = request.stream.read()
    # change for json format
    objectData = json.loads(data)
    # get a adress-lat data
    lat = objectData["lat"]
    # get a adress-long data
    long = objectData["long"]
    # put the values in adress object
    adress=[lat,long]
    # get a url image data
    urlImage = objectData["url"]
    # download the image to the server
    result_Download = download(urlImage, adress)
    # get url for do reconigze for flooded
    result_getUrl = getUrl(result_Download)
    # return if it is flooded
    return reconigze_dogcat(result_getUrl[0], result_getUrl[1])


@app.route("/dogcatIn", methods=['POST'])
def home4():
    print('Api:dogcatIn-'+str(now))
    # get data from post parmeter
    data = request.stream.read()
    # change for json format
    objectData = json.loads(data)
    # get a adress-lat data
    lat = objectData["lat"]
    # get a adress-long data
    long = objectData["long"]
    # put the values in adress object
    adress=[lat,long]
    # get a url image data
    urlImage = objectData["url"]
    # download the image to the server
    # result_Download = download(urlImage, adress)
    # get url for do reconigze for flooded
    # result_getUrl = getUrl(result_Download)
    # return if it is flooded
    return reconigze_dogcatIn(urlImage, adress)


@app.route("/trying", methods=['GET'])
def home5():
    return "trying :)"

@app.route("/sendMail", methods=['POST'])
def sendMAil():
    print('Api:sendMail-'+str(now))
    data = request.stream.read()
    objectData = json.loads(data)
    mess = objectData["mess"]
    sub = objectData["sub"]
    mail = objectData["mail"]
    name = objectData["name"]

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "incontrol.sys.service@gmail.com"
    receiver_email = ["alex.romm@incontrol-sys.com","royi.menashe@incontrol-sys.com"] # Enter receiver address
    password = "Aa123456!"
    msg = MIMEText('hi you hava i new message from the site'+
    '\n \n the sub:'+sub+
    '\n the name:'+name+
    '\n the message:'+ mess +'\n'
     '\n mail for callback :'+mail)
    msg['Subject'] = sub
    msg['From'] = "incontrol.sys.service@gmail.com"
    msg['To'] = mail

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        return "succses"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
