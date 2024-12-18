import re
targets = []
source = []

with open ("day7/Input.txt", "r") as inputData:
    for i in inputData:
        targets.append(int(re.match("[0-9]*", i).group(0)))
        source.append([int(x) for x in re.findall("[0-9]+", i)[1:]])


data = zip(targets, source)

def backtrack2(target, value, source):

    if value == target and len(source) == 0:
        return True
    if len(source) == 0:
        return False
    
    for i in [lambda x, y: x+y, lambda x, y: x*y, lambda x, y: x * (10 ** len(str(y))) + y]:
        result = backtrack2(target, i(value, source[0]), source[1:])
        if result:
            return True
    return False

def backtrack(target, value, source):
    if value == target and len(source) == 0:
        return True
    if len(source) == 0:
        return False
    for i in [lambda x, y: x+y, lambda x, y: x*y]:
        result = backtrack(target, i(value, source[0]), source[1:])
        if result:
            return True
    return False



invalid = []
counter = []
for t,s in data:
    if backtrack(t, s[0], s[1:]):
        counter.append(t)
    else:
        invalid.append((t,s))

for t,s in invalid:
    if backtrack2(t,s[0],s[1:]):
        counter.append(t)

print(sum(counter))