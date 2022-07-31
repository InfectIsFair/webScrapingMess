import requests
from bs4 import BeautifulSoup

def searchFormat(arg):
    puncList = ['`', '¬', '!', '"', '£', '$', '%', '^',' &', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '\'', '@', '#', '~',
            '\\', '|', ',', '<', '>', '.', '/', '?'] #list of punctuation, needs to be removed for the URL, but needs to be included in the name for the alt tag

    temp = arg.split(" ")
    numWords = len(temp)
    counter = 1
    arg = ""
    for word in temp:
        temp = ''
        for letter in word:
            if letter not in puncList:
                temp += letter
        word = temp 
        arg += word
        if counter != numWords:
            arg += "-"
        counter += 1

    return arg


def cardImageMTG(name, set):
    formatName = searchFormat(name)
    formatSet = searchFormat(set)

    #formats arguments for search engine, by replacing spaces with dashes, except for last word in arg
    URL = 'https://www.cardmarket.com/en/Magic/Products/Singles/' + formatSet + '/' + formatName

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #imageElement finds image element
    #image finds the src of the image
    imageElement = soup.find('img', alt=name)
    image = imageElement['src']
    
    return image


def cardImagePTCG(name, set):
    formatName = searchFormat(name)
    formatSet = searchFormat(set)

    #formats arguments for search engine, by replacing spaces with dashes, except for last word in arg
    URL = 'https://www.tcgplayer.com/search/pokemon/' + formatSet

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #imageElement finds image element
    #image finds the src of the image
    imageElement = soup.find('span', name)
    image = imageElement['src']
    
    return image
