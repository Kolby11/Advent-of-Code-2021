lines = open("Day 3/input.txt", "r").readlines()


def ProcessInput():
    numbers = []
    for line in lines:
        number = ""
        for digit in line:
            if digit == "\n":
                continue
            else:
                number += digit
        numbers.append(number)
    return numbers


def GetCommonNumber(numbers):
    # index 0=most common
    # index 1=least common
    if numbers.count("0") > numbers.count("1"):
        return ["0", "1"]
    return ["1", "0"]


def GetOxygenRating(numbers):
    while True:
        for bitPos in range(len(numbers[0])):
            if len(numbers) == 1:
                return numbers[0]
            newNumbers = []
            collumn = []
            for number in numbers:
                collumn.append(number[bitPos])
            for number in numbers:
                if number[bitPos] != GetCommonNumber(collumn)[0]:
                    newNumbers.append(number)
            numbers = newNumbers


def GetC02Rating(numbers):
    while True:
        for bitPos in range(len(numbers[0])):
            if len(numbers) == 1:
                return numbers[0]
            newNumbers = []
            collumn = []
            for number in numbers:
                collumn.append(number[bitPos])
            for number in numbers:
                if number[bitPos] != GetCommonNumber(collumn)[1]:
                    newNumbers.append(number)
            numbers = newNumbers


def Part1():
    numbers = ProcessInput()
    gamma = ""
    epsilon = ""
    collumn = []
    for i in range(len(numbers[0])):
        for number in numbers:
            collumn.append(number[i])
        gamma += GetCommonNumber(collumn)[0]
        epsilon += GetCommonNumber(collumn)[1]
        collumn = []

    return int(gamma, 2) * int(epsilon, 2)


def Part2():
    oxygen = int(GetOxygenRating(ProcessInput()), 2)
    c02 = int(GetC02Rating(ProcessInput()), 2)
    return oxygen * c02


print(Part1())
# 1025636
print(Part2())
# 793873
