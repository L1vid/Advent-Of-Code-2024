import re
import random

list1 = []
list2 = []
flag = True
with open ("day5/Input.txt", "r") as inputData:
    for i in inputData:
        if i == "\n":
            flag = False
            continue
        if flag:
            list1.append([int(x) for x in re.findall("[0-9][0-9]", i)])
        else: 
            list2.append([int(x) for x in (i.split(",")) if x != "\n"])


pageDict = {i:[] for i in range(10, 100)}

for i in list1:
    pageDict[i[0]].append(i[1])

invalid = []

def valid(i, pageDict):
    # print(i)
    flag = True
    for e,j in enumerate(i):
        for k in i[e:]:
            if j in pageDict[k]:
                flag = False

    if len(i) != len(set(i)):
        flag = False
    return flag

for i in list2:
    flag = valid(i, pageDict)
    if not flag:
        invalid.append(i)


import functools
 

def comp(a,b, pageDict):
    if b in pageDict[a]:
        return -1
    if a in pageDict[b]:
        return 1
    return 0

for i in invalid: 
    i.sort(key=functools.cmp_to_key(lambda a,b: comp(a,b,pageDict)))


counter = 0
for i in invalid:
    counter += i[len(i)//2]

print(counter)