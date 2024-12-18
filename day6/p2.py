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
start = [0,0]
for e1,i in enumerate(list1):
    for e2,j in enumerate(i):
        if j == "^":
            start = [e1,e2]
            break
    else:
        continue
    break 


loops = 0
for e1,i in enumerate(list1):
    for e2,j in enumerate(i):
        if j != ".":
            continue
        else:
            list1[e1][e2] = "#"

        up = True
        down = False
        left = False
        right = False

        position = start.copy()
        positionMap = {}

        while True:
            x = (position[0], position[1], ("").join([str(int(up)), str(int(down)), str(int(left)), str(int(right))]))
            if x in positionMap:
                loops += 1
                break
            else:
                positionMap[x] = 1
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
                break
        print(loops, e1, e2)
        list1[e1][e2] = "."

print(loops)