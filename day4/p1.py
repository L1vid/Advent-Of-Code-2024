import re

list1 = []
with open ("day4/Input.txt", "r") as inputData:
    for i in inputData:
        temp = []
        for j in i:
            if j != "\n":
                temp.append(j)
        list1.append(temp)


def checkFlat(l):
    l = ("").join(l)
    a = re.findall("XMAS", l)
    b = re.findall("SAMX", l)
    print(a, b)
    return len(a) + len(b)

def remV(l):
    return l[1:]
def remH(l):
    return [i[1:] for i in l]

def diag(l):
    slice = []
    for i in range(min(len(l), len(l[0]))):
        # print(i, len(l), len(l[0]))
        slice.append(l[i][i])
    return slice
# 1, 
count = 0
for i in list1:
    count += checkFlat(i)
print(count, "FLAT")
for i in list(map(list, zip(*list1))):
    count += checkFlat(i)
print(count, "FLAT OTHER WAY")


copy = list1.copy()
count += checkFlat(diag(copy))
# print(diag(copy))
for i in range(len(copy) -1):
    # print(diag(copy))
    copy = remV(copy)
    count += checkFlat(diag(copy))
print(count, "DIAG1")
copy = list1.copy()
for i in range(len(copy[0]) - 1):
    copy = remH(copy)
    count += checkFlat(diag(copy))
print(count, "DIAG2")


list1 = [i[::-1] for i in list1]

copy = list1.copy()
count += checkFlat(diag(copy))
for i in range(len(copy) -1):
    copy = remV(copy)
    count += checkFlat(diag(copy))
print(count, "DIAG1 REV")
copy = list1.copy()
for i in range(len(copy[0]) - 1):
    copy = remH(copy)
    count += checkFlat(diag(copy))
print(count, "DIAG2 REV")