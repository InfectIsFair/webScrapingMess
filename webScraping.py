import requests
from bs4 import BeautifulSoup
from lxml import etree

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


def EUR2GBP(money):
    result = ""
    numList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    moneyRemoved = []
    for char in money:
        if char in numList:
            moneyRemoved.append(char)
    
    temp1 = moneyRemoved[-2]
    moneyRemoved.pop(-2)
    temp2 = moneyRemoved[-1]
    moneyRemoved.pop(-1)
    
    moneyRemoved.append('.')
    moneyRemoved.append(temp1)
    moneyRemoved.append(temp2)
    
    money= ""
    for item in moneyRemoved:
        money += item
    
    result = float(money) * 0.84
    result = round(result, 2)
    
    pennyCheck = str(result).split(".")
    try:
        while len(pennyCheck[1]) != 2:
            pennyCheck[1] += '0'
    except:
        pennyCheck.append('00')
    
    result = ""
    result += pennyCheck[0]
    result += '.'
    result += pennyCheck[1]
    
    output = str(result) + ' GBP'

    # result = result
    return output


def cardDataMTG(name, set, setNum):
    formatName = searchFormat(name)
    formatSet = searchFormat(set)
    formatSetNum = searchFormat(setNum)

    #formats arguments for search engine, by replacing spaces with dashes, except for last word in arg
    URL = 'https://scryfall.com/card/' + formatSet + '/' + formatSetNum + '/' + formatName

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    dom = etree.HTML(str(soup))

    imageElement = dom.xpath('//*[@id="main"]/div[1]/div/div[1]/div/img')[0].attrib.get('src')
    priceElement = dom.xpath('//*[@id="stores"]/ul/li[2]/a/span')[0].text
    price = priceElement.encode("ascii", "ignore")
    price = price.decode()
    price = EUR2GBP(price)
    
    returnList = [imageElement, price]
    
    return returnList


# def cardImagePTCG(name, set):
#     formatName = searchFormat(name)
#     formatSet = searchFormat(set)

#     #formats arguments for search engine, by replacing spaces with dashes, except for last word in arg
#     URL = 'https://www.tcgplayer.com/search/pokemon/' + formatSet

#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
#     }

#     page = requests.get(URL, headers=headers)

#     soup = BeautifulSoup(page.content, 'html.parser')

#     #imageElement finds image element
#     #image finds the src of the image
#     imageElement = soup.find('span', name)
#     image = imageElement['src']
    
#     return image
