lines = open("Day 1/input.txt", "r").readlines()


def GetAmountOfIncreased():
    former = 0
    counter = 0
    for line in lines:
        if former == 0:
            former = int(line)
            continue
        if former < int(line):
            counter += 1
        former = int(line)
    return counter


def GetAmountOfIncreasedPerThree():
    counter = 0
    for i, line in enumerate(lines):
        if len(lines) >= i + 4:
            first = [int(line), int(lines[i + 1]), int(lines[i + 2])]
            second = [int(lines[i + 1]), int(lines[i + 2]), int(lines[i + 3])]
            if sum(first) < sum(second):
                counter += 1
        else:
            return counter


print(GetAmountOfIncreased())
# 1557
print(GetAmountOfIncreasedPerThree())
# 1608
