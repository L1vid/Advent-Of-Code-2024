list1 = []
with open ("day4/Input.txt", "r") as inputData:
    for e,i in enumerate(inputData):
        

        temp = []
        for j in i:
            if j != "\n":
                temp.append(j)
        list1.append(temp)

verWidth = len(list1[0])
verHeight = len(list1)


counter = 0
for e1,i in enumerate(list1):
    for e2,j in enumerate(i):
        if j == "A":
            if e2 >= 1 and e1 >= 1 and e2 < verWidth - 1 and e1 < verHeight - 1:
                if list1[e1 - 1][e2 - 1] == "M" and list1[e1 + 1][e2 + 1] == "S" :
                    if list1[e1 + 1][e2 - 1] == "M" and list1[e1 - 1][e2 + 1] == "S":
                        counter += 1
                    elif list1[e1 + 1][e2 - 1] == "S" and list1[e1 - 1][e2 + 1] == "M":
                        counter += 1
                elif list1[e1 - 1][e2 - 1] == "S" and list1[e1 + 1][e2 + 1] == "M":
                    if list1[e1 + 1][e2 - 1] == "M" and list1[e1 - 1][e2 + 1] == "S":
                        counter += 1
                    elif list1[e1 + 1][e2 - 1] == "S" and list1[e1 - 1][e2 + 1] == "M":
                        counter += 1
print(counter)