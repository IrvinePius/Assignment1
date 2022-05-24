import re

def calculateNgram():
    type = None
    while type == None:
        ngramType = input("Choose type of ngram (unigram | bigram)? ")
        if(ngramType == "unigram" or ngramType == "bigram"):
            type = ngramType
    if(ngramType == "unigram"):
        calculateUnigram()
    if(ngramType == "bigram"):
        calculateBigram()
        
def calculateUnigram():
    word = input("Please enter your word: ")

    test = getCorpusTwo()
    test = getCorpusOne()
    vocabularySet = set(test)

    occurrenceCount = len(re.findall(word, test))
    wordCount = len(re.findall("\\w+", test))

    print (occurrenceCount)
    print (wordCount)

    print("Occurrence rate: {}/{}".format(occurrenceCount, wordCount))
    print("P(w) = {}".format(float(occurrenceCount) / wordCount))
    print("PLaplace(wi) = {}").format(float(occurrenceCount + 1) / (wordCount + len(vocabularySet)))

def calculateBigram():
    word = input("Please enter your word: ")
    precedingWord = input("Please enter the preceding word: ")

    test = "obada obada duck test thing stuff obada"
    test = getCorpusOne()
    vocabularySet = set(test)

    occurrenceCount = len(re.findall(precedingWord + " " + word, test))
    wordCount = len(re.findall(precedingWord, test))

    print (occurrenceCount)
    print (wordCount)
    print("P(w1 | w-1) = {}".format(float(occurrenceCount) / wordCount))
    print("Occurrence rate: {}/{}".format(occurrenceCount, wordCount))
    print("P(w(n) | w(n-1)) = {}".format(float(occurrenceCount) / wordCount))
    print("PLaplace(w(n) | w(n-1)) = {}".format(float(occurrenceCount + 1) / (wordCount + len(vocabularySet))))

def getCorpusOne():
    return fileContents("The_House_Of_Hunger.txt")

def getCorpusTwo():
    return fileContents("The_Mystical_Life_Of_Jesus.txt")

def fileContents(fileName):
    f=open(fileName, "r")
    if f.mode == 'r':
        return f.read()
    
calculateNgram()
