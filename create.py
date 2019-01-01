import sys
import os
import datetime

def main():
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print str(len(arguments)) + " argument(s) passed. Expecting 1."
    else:
        createFiles(arguments[0])

def createFiles(name):
    week = findWeek()
    fileName = "week" + week + "_" + name
    if os.path.isfile(fileName + ".html"):
        print "Scaffolding already exists."
    elif os.path.isfile(fileName + ".js"):
        print "Scaffolding already exists."
    else:
        createHTML(week, name)
        createJS(fileName)

def createHTML(week, name):
    fileName = "week" + week + "_" + name
    refFile = open("ref.html", 'r')
    newFile = open(fileName+".html", 'w')

    refHTML = refFile.read()
    title = "AA Week " + week + " " + antiCamel(name)
    jsFile = "week" + week + "_" + name + ".js"

    newFile.write(refHTML.replace("Insert_Title", title).replace("Insert_JS", jsFile))
    refFile.close()
    newFile.close()

def createJS(fileName):
    refFile = open("ref.js", 'r')
    newFile = open(fileName+".js", 'w')

    refJS = refFile.read()
    newFile.write(refJS)
    refFile.close()
    newFile.close()

def antiCamel(title):
    wordList = []
    oldIndex = 0
    for i in range(len(title)):
        if(title[i].isupper()):
            wordList.append((title[oldIndex:i]).capitalize())
            oldIndex = i
    wordList.append((title[oldIndex:(i+1)]).capitalize())
    newTitle = " ".join(wordList)
    return newTitle

def findWeek():
    zeroIDate = datetime.date.today().strftime("%W")
    unitIDate = str(int(zeroIDate) + 1)
    if len(unitIDate) == 1:
        unitIDate = "0" + unitIDate
    return unitIDate

if __name__ == "__main__":
    main()