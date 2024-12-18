list1 = []
with open ("day6/Input.txt", "r") as inputData:
    for i in inputData:
        temp = []
        for j in i:
            if j != "\n":
                temp.append(j)
        list1.append(temp)

width = len(list1[0])
height = len(list1)
position = [0,0]
for e1,i in enumerate(list1):
    for e2,j in enumerate(i):
        if j == "^":
            position = [e1,e2]
            break
    else:
        continue
    break 


up = True
down = False
left = False
right = False

positionMap = {}

while True:
    positionMap[(position[0], position[1])] = True
    print(position)
    if up:
        if position[0] == 0:
            up = False
        elif list1[position[0] - 1][position[1]] == "#":
            up = False
            right = True
        else:
            position[0] -= 1
    elif down:
        if position[0] == height - 1:
            down = False
        elif list1[position[0] + 1][position[1]] == "#":
            down = False
            left = True
        else:
            position[0] += 1
    elif left:
        if position[1] == 0:
            left = False
        elif list1[position[0]][position[1] - 1] == "#":
            left = False
            up = True
        else:
            position[1] -= 1
    elif right:
        if position[1] == width - 1:
            right = False
        elif list1[position[0]][position[1] + 1] == "#":
            right = False
            down = True
        else:
            position[1] += 1
    else:
        print(len(positionMap))
        break
