import re


list1 = []
with open ("day3/Input.txt", "r") as inputData:
    list1 = ("").join(inputData)

re1 = "mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)"
re2 = "do\(\)"
re3 = "don't\(\)"

list2 = re.findall("mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)|do\(\)|don't\(\)", list1)

list3 = []
for i in list2:
    if i[0] == "m":
        list3.append(re.findall("[0-9]+", i))
    elif i[2] == "(":
        list3.append(True)
    else:
        list3.append(False)

doFlag = True
counter = 0
for i in list3:
    if i == False:
        doFlag = False
    elif i == True:
        doFlag = True
    else:
        if doFlag:
            counter += int(i[0]) * int(i[1])
        
        
print(counter)