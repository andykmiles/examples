#HW6_Question_1
def listToDict(bdayList):
    bdayList = {num+1: bdayList[num] for num in range(len(bdayList))}
    return bdayList

listToDict([1,2,1,0])

#HW6_Question_2
def newDict(Miriam):
    funDict = {alphnum:letter for letter, alphnum in Miriam.items()}
    return funDict

newDict({'F': 6,'U' : 21,'N': 14})

#with duplicates it will only return the key and value once
def newDict(Miriam):
    funDict = {alphnum:letter for letter, alphnum in Miriam.items()}
    return funDict

newDict({'F': 6,'U' : 21,'N': 6, 'N' : 33, 'Y': 25})

#HW6_Question_3
