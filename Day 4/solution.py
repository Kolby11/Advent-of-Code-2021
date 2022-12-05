lines = open("Day 4/input.txt", "r").readlines()

drawnNumbers = []
boards = []


def ProcessInput():
    board = []
    for i, line in enumerate(lines):
        number = ""
        # first line setup for drawn numbers
        if i == 0:
            for char in line:
                if char == "," or char == " " or char == "\n":
                    drawnNumbers.append(number)
                    number = ""
                    continue
                number += char
        # empty rows
        elif line == "\n":
            if board == []:
                continue
            else:
                boards.append(Board(board))
                board = []
        else:
            row = []
            number = ""
            for c, char in enumerate(line):
                if (c + 1) % 3 == 0:
                    row.append(int(number))
                    number = ""
                else:
                    number += char
            # last line
            if i == len(lines) - 1:
                row.append(int(number))
            board.append(row)
    boards.append(Board(board))


class Board:
    def __init__(self, board):
        self.board = board

    def MarkNumber(self, number):
        for rowIndex in range(len(self.board)):
            for collumnIndex in range(len(self.board[0])):
                if self.board[rowIndex][collumnIndex] == number:
                    self.board[rowIndex][collumnIndex] = "x"
                if (self.CheckHorizontal(rowIndex)) or self.CheckVertical(collumnIndex):
                    return True
        return None

    def GetUnmarkedNumbers(self):
        numbers = []
        for row in self.board:
            for collumn in row:
                if collumn == "x":
                    continue
                numbers.append(int(collumn))
        return numbers

    def CheckHorizontal(self, rowIndex):
        row = []
        for i in range(len(self.board[0])):
            row.append(self.board[rowIndex][i])
        if row.count("x") == len(self.board[0]):
            return True
        return False

    def CheckVertical(self, collumnIndex):
        collumn = []
        for i in range(len(self.board)):
            collumn.append(self.board[i][collumnIndex])
        if collumn.count("x") == len(self.board):
            return True
        return False


ProcessInput()


def Part1():
    for number in drawnNumbers:
        for i, board in enumerate(boards):
            if board.MarkNumber(int(number)) == True:
                return sum(board.GetUnmarkedNumbers()) * int(number)


def Part2():
    tempBoards = boards
    for number in drawnNumbers:
        for i, board in enumerate(tempBoards):
            if board.MarkNumber(int(number)) == True:
                if len(tempBoards) == 1:
                    return sum(board.GetUnmarkedNumbers()) * int(number)
                tempBoards.remove(board)


print(Part1())
# 65325
print(Part2())
# 4624
