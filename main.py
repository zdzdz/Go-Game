import pygame
import os
from constants import SQUARE_SIZE, WIDTH, HEIGHT, FPS
from board import Board
from interface import Interface

pygame.init()
pygame.display.set_caption('Go by Gavril Marinov (a python GURU)')
logo = pygame.image.load(os.path.join('images', 'go_icon.png'))
pygame.display.set_icon(logo)
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Transform mouse position into rows and columns of the board list
def get_row_col_mouse(pos):
    x, y = pos
    row = (y // SQUARE_SIZE)
    col = (x // SQUARE_SIZE)
    # Returns the row and column of the board list
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    interface = Interface()
    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                print(pos)
                # If mouse click is on the Go board
                if 12 <= pos[0] <= 755 and 12 <= pos[1] <= 755:
                    row, col = get_row_col_mouse(pos)
                    if board.white_to_move == False:
                        placed_stone = board.black_stone
                        opponent_stone = board.white_stone
                    else:
                        placed_stone = board.white_stone
                        opponent_stone = board.black_stone
                    board.place_stone(row + 1, col + 1,
                                      placed_stone, opponent_stone)
                # If pass button is clicked
                elif (interface.pass_pos_x <= pos[0] <= interface.pass_pos_x + 140 and
                      interface.pass_pos_y <= pos[1] <= interface.pass_pos_y + 40):
                    board.pass_move()

        board.draw_board(win)
        interface.draw_players_turn(win, board.white_to_move)
        interface.draw_players_text(win, board.captued_white_stones, board.captued_black_stones)
        interface.draw_pass(win, pos)
        if board.start_time and pygame.time.get_ticks() - board.start_time < 600:
            interface.draw_inv_move(win)
        pygame.display.update()

main()