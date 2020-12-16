import pygame

WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
OFFSET = 0
SQUARE_SIZE = (WIDTH - 2*OFFSET)//COLS

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
TEAL = (0, 255, 255)

TIE = "tie"

CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (45, 25))