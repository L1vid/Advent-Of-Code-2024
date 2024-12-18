list1 = []
list2 = []

with open ("day1/Input.txt", "r") as inputData:
    for i in inputData:
        j = i.split(" ")
        list1.append(int(j[0]))
        list2.append(int(j[3]))

list1 = sorted(list1)
list2 = sorted(list2)

counter = 0
for i in range(len(list1)):
    counter += abs(list1[i] - list2[i])

print(counter)