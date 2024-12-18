list1 = []
list2 = []

with open ("day1/Input.txt", "r") as inputData:
    for i in inputData:
        j = i.split(" ")
        list1.append(int(j[0]))
        list2.append(int(j[3]))

list2Hist = {}
for i in list2:
    if i in list2Hist:
        list2Hist[i] += 1
    else:
        list2Hist[i] = 1

counter = 0
for i in list1:
    if i in list2Hist:
        counter += i * list2Hist[i]

print(counter)