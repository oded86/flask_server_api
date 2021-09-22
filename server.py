from flask import Flask, request, jsonify
import json
from downloadPic import download
from upload_File_Firebase import getUrl
from reconigze import reconigze_flooded, reconigze_fire, reconigze_dogcat, reconigze_dogcatIn
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
