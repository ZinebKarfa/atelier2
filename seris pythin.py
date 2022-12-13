#exercice1
def createList(list1, list2):
    return list1[1::2] + list2[::2]
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
c = createList(list1,list2)
print(c)
#exercice 2
def deviserList(list):
    if len(list)%3 == 1:
        list.extend([0, 0])
    elif len(list)%3 == 2:
        list.append(0)
    else:
        list
    
    c = len(list) // 3
    result = []
    for i in range(3):
        test = []
        for j in range(c):
            test.append(list[i*c+j])
        result.append(test[::-1])
    return result

list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

print(deviserList(list))
# exercice 3 

def occurrence(list,n):
    count = 0
    for i in list:
        if i == n:
            count += 1
    return count
def compterOccurrence(list):
    mySet= set(list)
    myDict = {}
    for i in mySet:
        myDict[i] = occurrence(list,i)
    return myDict

list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

print(compterOccurrence(list))
#exercice4

def intersectionOfSets(set1,set2):
    return set1.intersection(set2)

def differenceOfSets(set1, set2):
    return set1.difference(set2)


set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

intersection = intersectionOfSets(set1,set2)
print(intersection)
set1 = differenceOfSets(set1,set2)
print(set1)

#exercice 5
def verifyElements(list,dict):
    res = []
    for x in dict.keys():
        if dict[x] in list:
            res.append(dict[x])
    return res

list = [47, 64, 69, 37, 76, 83, 95, 97]
dict = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}

print(verifyElements(list, dict))
