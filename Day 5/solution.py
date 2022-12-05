lines = open("Day 5/input.txt", "r").readlines()


def ProcessInput():
    moves = []
    for line in lines:
        pos1, pos2 = line.split("->")
        x1, y1 = tuple(map(int, pos1.split(",")))
        x2, y2 = tuple(map(int, pos2.split(",")))
        moves.append([x1, y1, x2, y2])
    return moves


def Part1(moves):
    field = []
    answer = 0
    for r in range(1000):
        row = []
        for c in range(1000):
            row.append(int(0))
        field.append(row)

    for move in moves:
        if move[0] == move[2] or move[1] == move[3]:
            for x in range(min(move[0], move[2]), max(move[0], move[2]) + 1):
                for y in range(min(move[1], move[3]), max(move[1], move[3]) + 1):
                    field[x][y] += 1
    for x in field:
        for y in x:
            if y > 1:
                answer += 1
    return answer


def Part2(moves):
    field = []
    answer = 0
    for r in range(1000):
        row = []
        for c in range(1000):
            row.append(int(0))
        field.append(row)

    for move in moves:
        if move[0] == move[2] or move[1] == move[3]:
            for x in range(min(move[0], move[2]), max(move[0], move[2]) + 1):
                for y in range(min(move[1], move[3]), max(move[1], move[3]) + 1):
                    field[x][y] += 1
        else:
            ...
    for x in field:
        for y in x:
            if y > 1:
                answer += 1
    return answer


print(Part1(ProcessInput()))
# 4655
