import pygame
from .constants import *

class Piece:
    PADDING = 10
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == WHITE:
            self.direction = 1
        else:
            self.direction = -1
        
        self.x = 60
        self.y = 60
        self.update_pos()

    def update_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2 + OFFSET
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2

    def make_king(self):
        self.king = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.update_pos()

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def __repr__(self):
        return str(self.color)

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_pos(self):
        return (self.x, self.y)

    def get_color(self):
        return self.color

    def get_direction(self):
        return self.direction

    def get_king(self):
        return self.king