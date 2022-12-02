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


def GetMostOccurentNumber(nums):
    occurence = [0, 0]
    for number in nums:
        if number == "0":
            occurence[0] += 1
        if number == "1":
            occurence[1] += 1
    if occurence[0] > occurence[1]:
        return "0"
    elif occurence[1] > occurence[0]:
        return "1"
    else:
        return "1"


def GetLeastOccurentNumber(nums):
    occurence = [0, 0]
    for number in nums:
        if number == "0":
            occurence[0] += 1
        if number == "1":
            occurence[1] += 1
    if occurence[0] > occurence[1]:
        return "1"
    elif occurence[1] > occurence[0]:
        return "0"
    else:
        return "0"


def GetPowerConsumption():
    gamma = ""
    epsilon = ""
    collumn = []
    for i, digit in enumerate(numbers[0]):
        for number in numbers:
            collumn.append(number[i])
        gamma += GetMostOccurentNumber(collumn)
        epsilon += GetLeastOccurentNumber(collumn)
        collumn = []

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def GetLifeSupportRating(nums):
    collumn = []
    for i in range(len(nums[0])):
        for j in range(2):
            for number in nums:
                if j == 0:
                    collumn.append(nums[i])
                if j == 1:
                    if number[i] != occurence:
                        nums.remove(number)
            occurence = GetMostOccurentNumber(collumn)
            print(occurence)
            collumn = []
    return nums


def GetC02Rating(nums):
    collumn = []
    for i in range(len(nums[0])):
        for j in range(2):
            for number in nums:
                if j == 0:
                    collumn.append(number[i])
                if j == 1:
                    if number[i] != occurence:
                        nums.remove(number)
            occurence = GetLeastOccurentNumber(collumn)
            print(occurence)
            collumn = []
    return nums


numbers = ProcessInput()
# print(GetPowerConsumption())
# 1025636
print(GetLifeSupportRating(numbers))
numbers = ProcessInput()
print("------------------------")
print(GetC02Rating(numbers))
