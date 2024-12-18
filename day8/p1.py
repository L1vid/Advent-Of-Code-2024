import re

positionMap = {}
antiPositionMap = set()
with open ("day8/Input.txt", "r") as inputData:
    for e1,i in enumerate(inputData):
        for e2,j in enumerate(i):
            a = re.match("[0-9a-zA-Z]", j)
            if a != None:
                b = a.group(0)
                if b in positionMap:
                    positionMap[b].append((e1,e2))
                else:
                    positionMap[b] = [(e1,e2)]
    width = e2 + 1
    height = e1 + 1

print(width, height)

def manhatten(a, b):
    height = b[0] - a[0]
    width =  b[1] - a[1]
    return (height, width)

for key in positionMap.keys():
    for e1,a1 in enumerate(positionMap[key]):
        for e2,a2 in enumerate(positionMap[key]):
            if a1 == a2:
                continue
            x, y = manhatten(a1,a2)
            print(a1, a2, manhatten(a1, a2))
            antiPosition = (a1[0] - x, a1[1] - y)
            if antiPosition[0] >= 0 and antiPosition[0] < height:
                if antiPosition[1] >= 0 and antiPosition[1] < width:
                    antiPositionMap.add(antiPosition)
                    print("Added,", antiPosition)


print(len(antiPositionMap))