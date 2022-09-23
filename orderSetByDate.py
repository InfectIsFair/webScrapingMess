import datetime
import numpy as np

def sortSets():
    setList = []

    setCSV = open("mtg-set.csv", "r")
    for line in setCSV.readlines():
        line = line.split("/")
        returnList = []
        for i in range(len(line)):
            if (i != 0) and (i != 4):
                returnList.append(line[i])
        
        setList.append(returnList)

    setCSV.close()

    setList = np.array(setList)

    sorted_array = setList[np.argsort(setList[:, 1])]
    
    setCSV = open("mtg-set.csv", "w")
    sortId = 1
    for file in sorted_array:
        setCSV.write(str(sortId) + "/")
        for item in file:
            setCSV.write(item)
            setCSV.write("/")
        setCSV.write("\n")
        sortId += 1

sortSets()
