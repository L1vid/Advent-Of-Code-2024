import re
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

valid = []

for i in list2:
    x = i
    flag = True
    for e,j in enumerate(x):
        for k in x[e:]:
            if j in pageDict[k]:
                print(i,x,e,j,k, j in pageDict[k], pageDict[k])
                flag = False
    if flag:
        valid.append(i)



print(len(valid))

counter = 0
for i in valid:
    counter += i[len(i)//2]

print(counter)