import sys

def setMemory(filename = "memory"):
    class EmptyFileError(Exception):pass
    class ImproperDateError(Exception):pass
    inFile = open(filename)
    try:
        if inFile is None: raise EmptyFileError
    except FileNotFoundError:
        print('File does not exit')

    heapList = []
    varDict = {}
    with open(filename) as f:
        first = f.readline()
        first = int(first)#n=10
        global keys
        keys = range(0, first)#0-9
        heapList = [ [] for k in keys]#create a list of n list inside                                 

        for line in f:
            x = line.strip().split(",")
            if len(x) > 1:
                for i in range(1,len(x)):
                    #non-heap                                                                         
                    if x[i].isalpha():
                        varDict[x[i]] = int(x[0])
                    #heap                                                                             
                    else:
                        if int(x[i]) in keys:
                            heapList[int(x[i])].append(int(x[0]))
    for k in keys:
        heapList[k].sort()
    varDict = {k:v for k,v in sorted(varDict.items())}
    memoTuple = (varDict,heapList)
    return memoTuple


def dfs(heapList, varDict,isMarked):
    for key,val in varDict.items():
        isMarked[val] = 1
        for i in heapList[val]:
            dfs(heapList, varDict, i)
    return isMarked

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        (varDict,heapList) = setMemory(filename)
        print(varDict)
        print(heapList)
        whole = [0]*(len(heapList))

        marked=[]
        swept=[]

        for i in varDict:
            curr = varDict[i]
            if curr not in marked:
                marked.append(curr)                
                whole[curr] = 1

                def dfs(curr):
                    for j in heapList[curr]:# j is element                                            
                        # nothing in there                                                            
                        if j == []:
                            break
                        else:
                            if(j in marked): continue
                            else:
                                marked.append(j)
                                whole[j] = 1
                                curr = j
                                dfs(curr)
                dfs(curr)
        count=0
        while count in range(len(heapList)):
            if whole[count] == 0 :
                swept.append(count)
            count=count+1

        def printout(something):
            for i in something:
                print(i,end=' ' )
            print()

        print('marked: ',end='')
        printout(marked)
        print('swept: ',end='')
        printout(swept)

main()