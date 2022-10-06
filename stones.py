import pygame
from constants import SQUARE_SIZE

class Stone:
    PADDING = 1

    def __init__(self, row, col, color):
        self.row = row - 1 # - 1 because the ending rows/colums are 1 and not playable
        self.col = col - 1 # - 1 because the ending rows/colums are 1 and not playable
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * (self.col) + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * (self.row) + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x + 4, self.y + 4), radius)