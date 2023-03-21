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
    def randomizeElement(self):
        pass
    def right(self):
        pass
    def left(self):
        pass
    def up(self):
        pass
    def down(self):
        pass
    def getTable(self):
        pass
    def copyTable(self):
        pass
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
