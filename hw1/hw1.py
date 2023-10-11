#cpsc3400
#txia@seattleu.edu
#hw1
import sys

def processFile(filename = "matches"):
    inFile = open(filename)
    scores = {}
    next(inFile) #skip 1st line

    
    for line in inFile:
        country,opponent,goals = line.strip().split(",")
        goals = int(goals)
        
        if country in scores:
            goals_scored, goals_lost, matches = scores[country]
            scores[country] = (goals_scored + goals, goals_lost, matches+1)
        else:
            scores[country] = (goals,0,1)

        if opponent in scores:
            goals_scored, goals_lost, matches = scores[opponent]
            scores[opponent] = (goals_scored, goals_lost + goals, matches)
        else:
            scores[opponent] = (0,goals,0)

    inFile.close()
    return scores


def getNetScores(scores, country):
    if country in scores:
        return scores[country][0] - scores[country][1]  #goals_scored - goals_lost
    else: 
        return 0
    
def createSortedDict(scores):
    sortedByKey = {k:v for k,v in sorted(scores.items())}
    sortedByMatches = {k:v for k,v in sorted(sortedByKey.items(), key = lambda v: v[1][2], reverse = True)}
    sortedByVal = {k:v for k,v in sorted(sortedByMatches.items(), key = lambda v: v[1][0], reverse = True)}
                   
    return sortedByVal

def createSummaryList(scores):
    country_list = []
    summary = []
    sumList = []
    for key,value in scores.items():
        if value[2]>0:
            country_list.append(key)
            summary.append(float((2*value[0] - value[1]) / value[2]))

    sumList = list(zip(country_list,summary))
    return sumList

def printDictionary(dictionary):
    keys = list(dictionary.keys())
    sorted_keys = sorted(keys)
    for key in sorted_keys:
        print(key," = ",dictionary[key][0]," : ",dictionary[key][1], " in ", dictionary[key][2], " match(es)" )

        
def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        scores = processFile(filename)
        print(scores)
        printDictionary(scores)
        print("Net score for England is "+ str(getNetScores(scores, "England")))
        print("Net score for United States is "+ str(getNetScores(scores, "United States")))
        print(createSortedDict(scores))
        print(createSummaryList(scores))
main()
