import re
targets = []
source = []

with open ("day7/Input.txt", "r") as inputData:
    for i in inputData:
        targets.append(int(re.match("[0-9]*", i).group(0)))
        # print(re.findall("[0-9]+", i))
        source.append([int(x) for x in re.findall("[0-9]+", i)[1:]])


data = zip(targets, source)



def backtrack(target, value, source, flag):
    # print(target, value, flag, source, source[flag-1])


    if value == target and flag == len(source):
        print("NICE")
        return True
    if flag == len(source):
        return False
    


    for i in [lambda x, y: x+y, lambda x, y: x*y]:
        result = backtrack(target, i(value, source[flag]), source, flag + 1)
        if result:
            return True
    return False


counter = []
for t,s in data:
    # print(t, s, backtrack(t, 0, s, 0))
    if backtrack(t, 0, s, 0):
        counter.append(t)

print(sum(counter))