import requests
from bs4 import BeautifulSoup
from lxml import etree

def searchFormat(arg):
    puncList = ['`', '¬', '!', '"', '£', '$', '%', '^',' &', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '\'', '@', '#', '~',
            '|', ',', '<', '>', '.', '/', '?'] #list of punctuation, needs to be removed for the URL, but needs to be included in the name for the alt tag

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


def removePunc(arg):
    puncList = ['`', '¬', '!', '"', '£', '$', '%', '^',' &', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '\'', '@', '#', '~',
            '|', ',', '<', '>', '.', '/', '?'] #list of punctuation, needs to be removed for the URL, but needs to be included in the name for the alt tag

    temp = arg
    arg = ""
    for letter in temp:
        if letter not in puncList:
            arg += letter

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
    
    result = float(money) / 1.1655
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


def cardDataMTG(set, setNum):
    cardId = 'M' + set.lower() + str(setNum)
    TCG = 'MTG'

    formatSet = searchFormat(set)
    formatSetNum = searchFormat(setNum)

    #formats arguments for search engine, by replacing spaces with dashes, except for last word in arg
    URL = 'https://scryfall.com/card/' + formatSet + '/' + formatSetNum

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    page = requests.get(URL.lower(), headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    dom = etree.HTML(str(soup))

    try:
        imageElement = dom.xpath('//*[@id="main"]/div[1]/div/div[1]/div/img')[0].attrib.get('src')
        priceElement = dom.xpath('//*[@id="stores"]/ul/li[2]/a/span')[0].text

        if priceElement != None:
            price = priceElement.encode("ascii", "ignore")
            price = price.decode()
            price = EUR2GBP(price)
        else:
            price = "0.00 GBP"
    except:
        imageElement = "https://media.istockphoto.com/vectors/eye-sensitive-content-sign-nappropriate-content-censored-view-icon-vector-id1254025883?k=20&m=1254025883&s=170667a&w=0&h=LOGaQuBtSGyBlTLptw3P67pSZctopssc6cc5PQThBQE="

        price = "0.00 GBP"

    nameElement = dom.xpath('//*[@id="main"]/div[1]/div/div[3]/h1/span[1]')[0].text
    name = removePunc(nameElement)
    
    rarityElement = dom.xpath('//*[@id="main"]/div[1]/div/div[4]/div[1]/a/span[2]')[0].text
    rarity = rarityElement.split("·")
    
    returnList = [cardId, TCG, name, rarity[1], formatSet, formatSetNum, imageElement, price]
    
    return returnList


def cardDataPTCG(set, setNum):
    cardId = 'P' + set.lower() + str(setNum)
    TCG = "PTCG"

    formatSet = searchFormat(set)
    formatSetNum = searchFormat(setNum)

    #formats arguments for search engine, by replacing spaces with dashes, except for last word in arg
    URL = 'https://limitlesstcg.com/cards/' + formatSet + '/' + formatSetNum

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    page = requests.get(URL.lower(), headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    dom = etree.HTML(str(soup))

    try:
        imageElement = dom.xpath('/html/body/main/div/section[1]/div[1]/div[1]/img')[0].attrib.get('src')
        priceElement = dom.xpath('/html/body/main/div/section[2]/div[2]/a[2]/span')[0].text
        
        if priceElement != None:
            price = priceElement.encode("ascii", "ignore")
            price = price.decode()
            price = EUR2GBP(price)
        else:
            price = "0.00 GBP"
    except:
        imageElement = "https://media.istockphoto.com/vectors/eye-sensitive-content-sign-nappropriate-content-censored-view-icon-vector-id1254025883?k=20&m=1254025883&s=170667a&w=0&h=LOGaQuBtSGyBlTLptw3P67pSZctopssc6cc5PQThBQE="

        price = "0.00 GBP"

    nameElement = dom.xpath('/html/body/main/div/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/p[1]/span/a')[0].text
    name = removePunc(nameElement)
    nameEncode = name.encode("ascii", 'ignore')
    nameDecode = nameEncode.decode()
    name = nameDecode
    
    rarityElement = dom.xpath('/html/body/main/div/section[1]/div[2]/div/a/div/span[2]')[0].text
    rarity = rarityElement.split("·")
    
    returnList = [cardId, TCG, name, rarity[1], formatSet, formatSetNum, imageElement, price]
    
    return returnList
