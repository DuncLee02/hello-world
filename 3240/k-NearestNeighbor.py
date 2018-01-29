#Duncan Lee (ddl9be)
#Advanced Software Development
#Homework 1

import collections
import math
import sys

def getK():
    try:
        k = int(input("k: "))
        return k
    except ValueError:
        print("enter an int for K")
        return getK()

def getM():
    try:
        numValuesToReadFromFile = int(input("M: "))
        return numValuesToReadFromFile
    except ValueError:
        print("enter an int for M")
        return getM()

def getFile():
    try:
        dataFileName = input("filename: ")
        f = open(dataFileName, "r")
        return f
    except FileNotFoundError:
        print("file not found! try again")
        return getFile()



k = getK()  #get k from user
numValuesToReadFromFile = getM()  #get m from user
f = getFile()  #get filename and open


class Point:
    def __init__(self, cat, x, y):
        self.category = cat
        self.x = x
        self.y = y
        self.dist = -1

def distance(point1, point2):
    changeXSquared = math.pow(point1.x - point2.x, 2)
    changeYSquared = math.pow(point1.y - point2.y, 2)
    return math.pow(changeXSquared + changeYSquared, 1/2)



classifiedPoints = []
count = 0
for line in f:  #parses data from file
    count += 1
    if count > numValuesToReadFromFile:
        break
    #print(line.strip())
    array = line.split()
    cat = array[0]
    x = float(array[1])
    y = float(array[2])
    newPoint = Point(cat, x, y)
    classifiedPoints.append(newPoint)


def findKClosest(unclassifiedPoint, classifiedPoints):
    for x in range(0, len(classifiedPoints)):  #gets distance from given point to each point in map
        thisPoint = classifiedPoints[x]
        thisPoint.dist = distance(unclassifiedPoint, thisPoint)
    classifiedPoints = sorted(classifiedPoints, key=lambda Point: Point.dist)  #sorts points based on distance
    kClosest = classifiedPoints[0: k]
    return kClosest  #returns k closest points


nextPoint = True
kClosest = []
while nextPoint == True: # gets next point from user
    point = input("enter point: ")
    pointArray = point.split(" ")
    x = float(pointArray[0])
    y = float(pointArray[1])

    if (x == 1.0 and y == 1.0): # stops if point is 1, 1
        nextPoint = False
    else:
        newPoint = Point("", x, y)  #initialize new point
        kClosest = findKClosest(newPoint, classifiedPoints)  #find k closest points
        for p in kClosest:  #prints out points
            print(p.category + " " + str(p.x) + " " + str(p.y) + " " + str(p.dist))

        countDict = {}  #creates dict
        for item in kClosest:
            if not item.category in countDict:  #if key not in dict, creates with count 1
                countDict[item.category] = 1
            else:  #if key exists, increments count
                countDict[item.category] += 1

        countDictKeys = list(countDict)  #finds max value in dict
        maxKey = countDictKeys[0]
        for key in countDictKeys:
            if countDict[key] > countDict[maxKey]:
                maxKey = key

        print("Data Item (" + str(newPoint.x) + "," + str(newPoint.y) + ") assigned to: " + str(maxKey) )


        if (len(countDictKeys) == 1):  #finds distance to each category if only 1 category
            totalDistance = 0
            for points in kClosest:
                totalDistance += points.dist
            print("Average distance to " + countDictKeys[0] + " items: " + str( totalDistance/ len(kClosest)) )

        else:  #if multiple categories, finds average distance to both
            totalDistanceCat1 = 0
            totalCountCat1 = countDict[countDictKeys[0]]
            totalDistanceCat2 = 0
            totalCountCat2 = countDict[countDictKeys[1]]

            for points in kClosest:
                if points.category == countDictKeys[0]:
                    totalDistanceCat1 += points.dist
                else:
                    totalDistanceCat2 += points.dist

            print("Average distance to " + countDictKeys[0] + " items: " + str(totalDistanceCat1/totalCountCat1))
            print("Average distance to " + countDictKeys[1] + " items: " + str(totalDistanceCat2/totalCountCat2))





        