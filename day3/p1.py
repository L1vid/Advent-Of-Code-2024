import re


list1 = []
with open ("day3/Input.txt", "r") as inputData:
    list1 = ("").join(inputData)

list2 = re.findall("mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", list1)
list3 = [re.findall("[0-9]+", i) for i in list2]

counter = 0
for i in list3:
    counter += int(i[0]) * int(i[1])

print(counter)