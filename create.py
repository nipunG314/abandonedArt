import sys
import os

def main():
    arguments = sys.argv[1:]
    if len(arguments) != 2:
        print str(len(arguments)) + " argument(s) passed. Expecting 2."
    else:
        createFiles(arguments)

def createFiles(arguments):
    fileName = "week" + arguments[0] + "_" + arguments[1]
    if os.path.isfile(fileName + ".html"):
        print "Scaffolding already exists."
    elif os.path.isfile(fileName + ".js"):
        print "Scaffolding already exists."
    else:
        createHTML(arguments)
        createJS(fileName)

def createHTML(arguments):
    fileName = "week" + arguments[0] + "_" + arguments[1]
    refFile = open("ref.html", 'r')
    newFile = open(fileName+".html", 'w')

    refHTML = refFile.read()
    title = "AA Week " + arguments[0] + " " + antiCamel(arguments[1])
    jsFile = "week" + arguments[0] + "_" + arguments[1] + ".js"

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

if __name__ == "__main__":
    main()