import random
import sys
import pygame

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
        pygame.init()
        self.screen = pygame.display.set_mode([400, 400])
        pygame.display.set_caption("Game 2048")
        pygame.font.init()
        self.myfont30 = pygame.font.SysFont("ComicSans", 30)
        self.myfont45 = pygame.font.SysFont("ComicSans", 45)
    def draw(self, table):
        self.screen.fill((0, 0, 0))
        text = self.myfont45.render("Nasza Gra", False, (128, 255, 0))
        self.screen.blit(text, (0, 0))
        for x in range(0, 4):
            for y in range(0, 4):
                text = self.myfont30.render(str(table[y][x].getVal()), False, (255, 255, 0))
                self.screen.blit(text, (x*100+20, y*75+100))
        pygame.display.flip()
    def run(self, board):
        board.randomizeElement()
        while True:
            self.draw(board.getTable())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if board.up():
                            board.randomizeElement()
                    elif event.key == pygame.K_DOWN:
                        if board.down():
                            board.randomizeElement()
                    elif event.key == pygame.K_LEFT:
                        if board.left():
                            board.randomizeElement()
                    elif event.key == pygame.K_RIGHT:
                        if board.right():
                            board.randomizeElement()
                    elif event.key == pygame.K_z:
                        for x in range(0, 4):
                            for y in range(0, 4):
                                board[y][x].setVal(self.prevBoard[y][x].getVal())
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()


def main():
    pass


if __name__ == '__main__':
    main()
