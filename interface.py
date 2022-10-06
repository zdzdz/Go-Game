import pygame
from board import Board
from constants import DARK_GREY, LIGHT_GREY, WHITE, RED, BLACK

board = Board()

class Interface:
    def __init__(self):
        # Interface font
        self.int_font = pygame.font.SysFont('Consolas', 28)
        self.int_font2 = pygame.font.SysFont('Consolas', 18)
        self.int_font3 = pygame.font.SysFont('Consolas', 28, bold=True)
        # Pass button
        self.pass_width = 70
        self.pass_height = 40
        self.pass_pos_x = 796
        self.pass_pos_y = 600
        self.pass_col_d = (DARK_GREY)
        self.pass_col_l = (LIGHT_GREY)
        self.pass_txt_col = (WHITE)
        self.pass_text = self.int_font.render(
            'pass', True, self.pass_txt_col)
        # Players tab
        self.player_box_col = (LIGHT_GREY)
        self.player_txt_col = (WHITE)
        self.player_width = 200
        self.player_height = 65

        self.b_player_pos_x = 796
        self.b_player_pos_y = 23
        self.b_player_txt = self.int_font.render(
            'Black', True, self.player_txt_col)
        self.w_player_pod_x = 796
        self.w_player_pos_y = 100
        self.w_player_txt = self.int_font.render(
            'White', True, self.player_txt_col)
        # Invalid move
        self.inv_move_width = 201
        self.inv_move_height = 35
        self.inv_move_pos_x = 282
        self.inv_move_pos_y = 367
        self.inv_move_col = (RED)
        self.inv_move_txt = self.int_font3.render(
            'Invalid Move!', True, self.inv_move_col)

    def draw_pass(self, win, pos):
        if (self.pass_pos_x <= pos[0] <= self.pass_pos_x + self.pass_width and
                self.pass_pos_y <= pos[1] <= self.pass_pos_y + self.pass_height):
            pygame.draw.rect(win, self.pass_col_l,
                             (self.pass_pos_x, self.pass_pos_y, self.pass_width, self.pass_height))
            win.blit(self.pass_text, (self.pass_pos_x + 5, self.pass_pos_y + 5))
        else:
            pygame.draw.rect(win, self.pass_col_d,
                             (self.pass_pos_x, self.pass_pos_y, self.pass_width, self.pass_height))
            win.blit(self.pass_text, (self.pass_pos_x + 5, self.pass_pos_y + 5))

    def draw_players_text(self, win, b_count, w_count):
        capture_count_b = self.int_font2.render(
            'Captured Stones: ' + str(b_count), True, self.player_txt_col)
        capture_count_w = self.int_font2.render(
            'Captured Stones: ' + str(w_count), True, self.player_txt_col)
        win.blit(self.b_player_txt,
                 (self.b_player_pos_x + 5, self.b_player_pos_y + 5))
        win.blit(capture_count_b,
                 (self.b_player_pos_x + 5, self.b_player_pos_y + 40))
        win.blit(self.w_player_txt,
                 (self.w_player_pod_x + 5, self.w_player_pos_y + 5))
        win.blit(capture_count_w,
                 (self.w_player_pod_x + 5, self.w_player_pos_y + 40))

    def draw_players_turn(self, win, turn):
        if turn == False:
            pygame.draw.rect(win, self.player_box_col, (self.b_player_pos_x,
                             self.b_player_pos_y, self.player_width, self.player_height))
        else:
            pygame.draw.rect(win, self.player_box_col, (self.w_player_pod_x,
                             self.w_player_pos_y, self.player_width, self.player_height))

    def draw_inv_move(self, win):
        pygame.draw.rect(win, self.player_box_col, (self.inv_move_pos_x,
                                                    self.inv_move_pos_y, self.inv_move_width, self.inv_move_height))
        win.blit(self.inv_move_txt,
                 (self.inv_move_pos_x + 5, self.inv_move_pos_y + 5))
