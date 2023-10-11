import sys
from functools import cmp_to_key

def processFile(filename = "dates"):

    inFile = open(filename) 
    dateList = []    
    MONTH = {"JAN":31,"FEB":28,"MAR":31,"APR":30,"MAY":31,"JUN":30,"JUL":31,"AUG":31,"SEP":30,"OCT":31,"NOV":30,"DEC":31}
    
    try:
        if inFile is None:
            raise OSError
    except FileNotFoundError:
        print("File does not exist.")
        raise
    except OSError as EmptyFileError:
        print("The file is empty.")
        
    for line in inFile:
        month,day,year = line.strip().split(",")
        day = int(day)
        year = int(year)
        dateTuple = (month,day,year)
        try:
            dateList.append(dateTuple)
            if (month not in MONTH) or (day not in range(1, MONTH[month]+1)) or (year not in range(1950, 2024)) :
                raise ValueError
        except ValueError as ImproperDateError:
            print("This exception is raised if any of the dates are invalid.")
            raise
        
    inFile.close()
    return dateList

def dateConvertGen(dateList, dateFormat):
    AmGen = []
    IntGen = []
    AsnGen = []
    MONTH = {"JAN":"01","FEB":"02","MAR":"03","APR":"04","MAY":"05","JUN":"06","JUL":"07","AUG":"08","SEP":"09","OCT":"10","NOV":"11","DEC":"12"}

    try:
        for (month,day,year) in dateList:
            if dateFormat is "Asian":
                AsnGen.append(str(year)+"-"+ MONTH[month] +"-"+str(day).zfill(2))
            if dateFormat is "International":
                IntGen.append(str(day).zfill(2)+"-"+MONTH[month]+"-"+str(year))
            else:
                AmGen.append(MONTH[month]+"-"+str(day).zfill(2)+"-"+str(year))
    except:
        print("Something else went wrong")
    else:
        if dateFormat is "International":
            return IntGen
        if dateFormat is "Asian":
            return AsnGen
        else:
            return AmGen


def compare(date1, date2):
    numList = []
    comList = [date1,date2]
    comList = dateConvertGen(comList,"Asian")
    for x in comList:
        num = x.replace("-",'')
        numList.append(int(num))
    
    date1 = int(numList[0])
    date2 = int(numList[1])

    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0
  

def calcDifference(date1, date2):
    try:
        if compare(date1, date2) is 1:
            print("This exception is raised if date2 is earlier than date1.")
            raise ValueError
    except ValueError as InvalidPairError:
        raise
    
    MONTH = {"JAN":31,"FEB":28,"MAR":31,"APR":30,"MAY":31,"JUN":30,"JUL":31,"AUG":31,"SEP":30,"OCT":31,"NOV":30,"DEC":31}
    temp = list(MONTH)
    numList = []
    finalList = ['Y','M','D']#order in Y,M,D!
    calcList = [date1,date2]
    calcList = dateConvertGen(calcList,"American")
    
    for x in calcList:
        month, day, year = x.strip().split("-")
        month = int(month)
        day = int(day.zfill(2))
        year = int(year)
        numTuple = month, day, year
        numList.append(numTuple)
#    print(numList[0],numList[1])
    
    if numList[1][1] >= numList[0][1]:
        #New day > old day
        #subtract from day
        finalList[2] = numList[1][1]-numList[0][1]
        if numList[1][0] >= numList[0][0]:
            #new month > old month
            finalList[1] = numList[1][0]-numList[0][0]
            finalList[0] = numList[1][2]-numList[0][2]
        else:#month borrow from adjacent year
            #new month < old month
            finalList[1] = numList[1][0]+12-numList[0][0]
            finalList[0] = numList[1][2]-1-numList[0][2]
    else:#new day < old day
        #day: borrow from adjacent month
        res = None
        temp = iter(MONTH)
        for key in temp:
            if key == MONTH[date2[0]]:
                res = next(temp, None)
        finalList[2] = (MONTH[res] + numList[1][1]) - numList[0][1] 

        if numList[1][0] >= numList[0][0]:
            #new month > old month
            finalList[1] = numList[1][0]-numList[0][0]
            finalList[0] = numList[1][2]-numList[0][2]
        else:#month: borrow from adjacent year 
            #new month < old month                                          
            finalList[1] = numList[1][0]+12-numList[0][0]
            finalList[0] = numList[1][2]-1-numList[0][2]

    finalList = tuple(finalList)
    return finalList



    
def main():
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        dateList = processFile(filename)
        print([''.join(month + " " + str(day) + ", " + str(year)) for (month, day, year) in dateList],"\n")
        AmGen = dateConvertGen(dateList, "American")
        print(AmGen[0], "\n")
        IntGen = dateConvertGen(dateList, "International")
        try:
            print(*IntGen, sep = "\n")
            if StopIteration:
                print("No more dates\n")
        except:
            print("General Mistake: Something else went wrong\n")
            
        print("Most recent year:", max([year for (month, day, year) in dateList]),"\n")

        print(sorted(dateList,key = cmp_to_key(compare)),"\n")
        target = dateList[-1]
        print([calcDifference((month, day, year),(target)) for (month, day, year) in dateList],"\n")
        print([compare(('JAN',1,2000),(month, day, year)) for (month, day, year) in dateList],"\n")
        
main()