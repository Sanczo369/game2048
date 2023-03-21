import random


class Element:
    def __init__(self):
        self.val = 0

    def setVal(self, val):
        self.val = val

    def delVal(self):
        self.val = 0

    def getVal(self):
        return self.val

class Board:
    #initialization 4x4 board
    def __init__(self):
        self.board = [[], [], [], []]
        self.prevBoard = [[], [], [], []]
        for x in range(0, 4):
            for y in range(0, 4):
                self.board[y].append(Element())
                self.prevBoard[y].append(Element())

    #randomize a new element (value of 2 or 4) into the empty spaces
    def randomizeElement(self):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while self.board[x][y].getVal() != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        self.board[x][y].setVal(random.randint(1, 2)*2)

    #move
    def right(self):
        self.copyTable()
        for z in range(0, 3):
            for x in range(0, 3):
                for y in range(0, 4):
                    x = 2-x
                    if self.board[y][x+1].getVal() == 0:
                        self.board[y][x+1].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal() == self.board[y][x+1].getVal():
                        self.board[y][x + 1].setVal(self.board[y][x].getVal()*2)
                        self.board[y][x].delVal()
        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True
        return False

    def left(self):
        self.copyTable()
        for z in range(0, 3):
            for x in range(1, 4):
                for y in range(0, 4):
                    if self.board[y][x - 1].getVal() == 0:
                        self.board[y][x - 1].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal() == self.board[y][x - 1].getVal():
                        self.board[y][x - 1].setVal(self.board[y][x].getVal() * 2)
                        self.board[y][x].delVal()
        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True
        return False

    def up(self):
        self.copyTable()
        for z in range(0, 3):
            for x in range(0, 4):
                for y in range(1, 4):
                    if self.board[y-1][x].getVal() == 0:
                        self.board[y-1][x].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal() == self.board[y-1][x].getVal():
                        self.board[y-1][x].setVal(self.board[y][x].getVal() * 2)
                        self.board[y][x].delVal()
        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True
        return False

    def down(self):
        self.copyTable()
        for z in range(0, 3):
            for x in range(0, 4):
                for y in range(0, 3):
                    y = 2-y
                    if self.board[y+1][x].getVal() == 0:
                        self.board[y+1][x].setVal(self.board[y][x].getVal())
                        self.board[y][x].delVal()
                    elif self.board[y][x].getVal() == self.board[y+1][x].getVal():
                        self.board[y+1][x].setVal(self.board[y][x].getVal()*2)
                        self.board[y][x].delVal()
        for x in range(0, 4):
            for y in range(0, 4):
                if self.prevBoard[y][x].getVal() != self.board[y][x].getVal():
                    return True
        return False
    def getTable(self):
        return self.board

    def copyTable(self):
        for x in range(0, 4):
            for y in range(0, 4):
                self.prevBoard[y][x].setVal(self.board[y][x].getVal())
class Game:
    def __init__(self):
        pass
    def draw(self, table):
        pass
    def run(self, board):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
