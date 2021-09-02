import requests
from upload_File_Firebase import getUrl


def download(url, adressF):
    adress = adressF

    print("statring downloadPic func.........")
    # open image on the server
    f = open('fire.jpg', 'wb')
    print('success-1')
    # download the image from url
    f.write(requests.get(url).content)
    print('success-2')
    # close the file
    f.close()
    print('success-3')
    # call to getUrl function
    # print(adress)
    return adress
