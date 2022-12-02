lines = open("Day 2/input.txt", "r").readlines()


def GetSubmarineCourse():
    position = [0, 0]
    for command in lines:
        command = command.split()
        match command[0]:
            case "forward":
                position[0] += int(command[1])
            case "up":
                position[1] -= int(command[1])
            case "down":
                position[1] += int(command[1])
    return position[0] * position[1]


def GetSubmarineCourse2():
    position = [0, 0, 0]
    for command in lines:
        command = command.split()
        match command[0]:
            case "forward":
                position[0] += int(command[1])
                position[1] += int(command[1]) * position[2]
            case "up":
                position[2] -= int(command[1])
            case "down":
                position[2] += int(command[1])
    return position[0] * position[1]


print(GetSubmarineCourse())
# 2272262
print(GetSubmarineCourse2())
# 2134882034
