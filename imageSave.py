import requests

def saveImage(url, id):
    img_data = requests.get(url).content
    path = 'static/tcg-master-base_' + id + ".jpeg"
    with open(path, 'wb') as handler:
        handler.write(img_data)
