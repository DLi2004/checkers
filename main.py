import pygame
from checkers.constants import *
from checkers.board import *
from checkers.piece import Piece

FPS = 30

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers 2.0")

def mouse_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def game_over(winner):
    WIN.fill(WHITE)
    pygame.font.init()
    font = pygame.font.SysFont("verdana", 24)
    if winner == WHITE:
        text = font.render("White wins!", False, (0, 0, 0))
        WIN.blit(text, (295, 320))
    elif winner == RED:
        text = font.render("Red wins!", False, (0, 0, 0))
        WIN.blit(text, (300, 320))
    else:
        text = font.render("It's a tie.", False, (0, 0, 0))
        WIN.blit(text, (300, 320))
    

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    winner = None

    def next_turn():
        if board.turn == RED:
            board.turn = WHITE
        else:
            board.turn = RED

    while run:
        clock.tick(FPS)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = mouse_pos(pos)
                piece = board.get_piece(row, col)
                if piece != 0:
                    if board.get_turn() == piece.get_color():
                        board.selected = piece
                else:
                    if board.selected is not None:
                        if board.can_move(board.selected, row, col):
                            board.move(board.selected, row, col)
                            next_turn()
                        elif board.can_jump(board.selected, row, col):
                            board.jump(board.selected, row, col)
                            next_turn()
                        else:
                            board.selected = None
                if board.check_game_over() == RED:
                    winner = RED
                elif board.check_game_over() == WHITE:
                    winner = WHITE
                elif board.check_game_over() == TIE:
                    winner = TIE
        
        if winner is None:
            board.draw_squares(WIN)
            for row in board.board:
                for piece in row:
                    if piece != 0:
                        piece.draw(WIN)
        elif winner == RED:
            game_over(RED)
        elif winner == WHITE:
            game_over(WHITE)
        elif winner == TIE:
            game_over(TIE)
        pygame.display.update()

    pygame.quit()

main()