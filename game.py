from piece_functions.piece import Piece
import pygame
import time
import random

piece_list = ['i', 'o', 't', 's', 'z']
pieces_at_bottom = []
pygame.init()
screen = pygame.display.set_mode((240, 440))
game_over = False
# current_piece = Piece(random.choice(piece_list))

current_piece = Piece('i')

game_clock = time.time()

debug = False

move_time = 1
level = 1


def draw_at_bottom():
    for i in pieces_at_bottom:
        i.draw(screen)

while not game_over:
        # each second of game
        # Controls pieces moving down
        if not debug:
            if time.time() - game_clock >= move_time:
                game_clock = time.time()
                current_piece.move_down()
                if current_piece.at_bottom:
                    pieces_at_bottom.append(current_piece)
                    current_piece = Piece(random.choice(piece_list))

        # start of event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                debug = not debug
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                current_piece.rotate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                current_piece.move_left()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                current_piece.move_right()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                move_time = .07
            if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                move_time = 1

        screen.fill((0, 0, 0))
        draw_at_bottom()

        current_piece.draw(screen)
        pygame.display.flip()
