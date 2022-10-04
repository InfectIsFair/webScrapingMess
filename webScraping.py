from calendar import TextCalendar
import requests
from bs4 import BeautifulSoup
from lxml import etree
import imageSave

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
        imageElement = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"

        price = "0.00 GBP"

    imageSave.saveImage(imageElement, cardId.lower())
    nameElement = dom.xpath('//*[@id="main"]/div[1]/div/div[3]/h1/span[1]')[0].text
    name = removePunc(nameElement)
    
    rarityElement = dom.xpath('//*[@id="main"]/div[1]/div/div[4]/div[1]/a/span[2]')[0].text
    rarity = rarityElement.split("·")
    
    returnList = [cardId, TCG, name, rarity[1], formatSet, formatSetNum, price]
    
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
        imageElement = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"

        price = "0.00 GBP"

    imageSave.saveImage(imageElement, cardId.lower())
    nameElement = dom.xpath('/html/body/main/div/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/p[1]/span/a')[0].text
    name = removePunc(nameElement)
    nameEncode = name.encode("ascii", 'ignore')
    nameDecode = nameEncode.decode()
    name = nameDecode
    
    rarityElement = dom.xpath('/html/body/main/div/section[1]/div[2]/div/a/div/span[2]')[0].text
    rarity = rarityElement.split("·")


    returnList = [cardId, TCG, name, rarity[1], formatSet, formatSetNum, price]

    return returnList


# def cardDataPTCGVariants(set, setNum, count):
#     try:
#         correctSetNum = setNum - count
#         TCG = "PTCG"

#         formatSet = searchFormat(set)
#         formatSetNum = searchFormat(str(correctSetNum))
#         try:
#             try:
#                 cardId = "P" + set.lower() + "TG" + str(correctSetNum)

#                 #formats arguments for search engine, by replacing spaces with dashes, except for last word in arg
#                 URL = 'https://limitlesstcg.com/cards/' + formatSet + '/TG' + str(formatSetNum)

#             except:
#                 cardId = "P" + set.lower() + "SV" + str(correctSetNum)

#                 #formats arguments for search engine, by replacing spaces with dashes, except for last word in arg
#                 URL = 'https://limitlesstcg.com/cards/' + formatSet + '/SV' + str(formatSetNum)
#         except:
#             cardId = "P" + set.lower() + "RC" + str(correctSetNum)

#             #formats arguments for search engine, by replacing spaces with dashes, except for last word in arg
#             URL = 'https://limitlesstcg.com/cards/' + formatSet + '/RC' + str(formatSetNum)

#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
#         }

#         page = requests.get(URL.lower(), headers=headers)

#         soup = BeautifulSoup(page.content, 'html.parser')
#         dom = etree.HTML(str(soup))

#         try:
#             imageElement = dom.xpath('/html/body/main/div/section[1]/div[1]/div[1]/img')[0].attrib.get('src')
#             priceElement = dom.xpath('/html/body/main/div/section[2]/div[2]/a[2]/span')[0].text
            
#             if priceElement != None:
#                 price = priceElement.encode("ascii", "ignore")
#                 price = price.decode()
#                 price = EUR2GBP(price)
#             else:
#                 price = "0.00 GBP"
#         except:
#             imageElement = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png"

#             price = "0.00 GBP"

#         nameElement = dom.xpath('/html/body/main/div/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/p[1]/span/a')[0].text
#         name = removePunc(nameElement)
#         nameEncode = name.encode("ascii", 'ignore')
#         nameDecode = nameEncode.decode()
#         name = nameDecode
        
#         rarityElement = dom.xpath('/html/body/main/div/section[1]/div[2]/div/a/div/span[2]')[0].text
#         rarity = rarityElement.split("·")


#         returnList = [cardId, TCG, name, rarity[1], formatSet, formatSetNum, imageElement, price]
    
#     except:
#         returnList = ["error", "error", "Card not found", "Error", "Error", "0", "data:image/png;base64,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", "X.XX GBP"]
    
#     return returnList
