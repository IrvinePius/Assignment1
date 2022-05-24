def minEditDistance(string1,string2, insertCost, deleteCost, substituteCost, printDistanceMatrix):

    string1length = len(string1) + 1
    string2length = len(string2) + 1
    distMatrix = [[0 for col in range(string1length)] for row in range(string2length)]

    for col in range(string1length):
        distMatrix[0][col] = col

    for row in range(string2length):
        distMatrix[row][0] = row

    for row in range(string2length):
        for col in range(string1length):
            if row > 0 and col > 0:
                if string1[col - 1] == string2[row - 1]:
                    distMatrix[row][col] = distMatrix[row - 1][col - 1]
                else:
                    distMatrix[row][col] = min(distMatrix[row - 1][col] + deleteCost,
                                           distMatrix[row - 1][col - 1] + substituteCost,
                                           distMatrix[row][col - 1] + insertCost)

    if printDistanceMatrix == "Y" :
        string1 = "#" + string1
        arrstring1 = [string1[i] for i in range(string1length)]

        string2 = "#" + string2
        arrstring2 = [[string2[i] for col in range(1)] for i in range(string2length)]

        print(arrstring2)
        for row in range(string2length):
            print(arrstring1[row], distMatrix[row])

    print("The minimum edit distance is: ", distMatrix[string2length-1][string1length-1])

string1 = input("Please enter the first word: \n")
string2 = input("Please enter the second word \n")
insertCost = input("Please enter the cost for insertion: \n")
deleteCost = input("Please enter the cost for deletion: \n")
substituteCost = input("Please enter the for a substitution: \n")
printDistanceMatrix = input("Print out the distance matric (Y/N) \n")

try:
    minEditDistance(string1, string2, int(insertCost), int(deleteCost), int(substituteCost),printDistanceMatrix)
except ValueError:
    print("Invalid input data")

