list1 = []

with open ("day2/Input.txt", "r") as inputData:
    for i in inputData:
        j = i.split(" ")
        for k in range(len(j)):
            j[k] = int(j[k])
        list1.append(j)

# check list for valid according to p1 rules
# Only checks in one direction, if other direction reverse list
def valid(i):
    if i[0] > i[1]:
        i = i[::-1]

    prev = i[0]
    safe = True
    for j in i[1:]:
        if j - prev <= 3 and j - prev > 0:
            prev = j
        else: 
            safe = False
            break
    return safe


counter = 0
for i in list1:
    safe = False
    for j in range(len(i)):
        if valid([x for e,x in enumerate(i) if e != j]):
            safe = True
            break
    counter += safe

print(counter)
