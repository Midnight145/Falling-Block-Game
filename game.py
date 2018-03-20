from piece_functions.piece import Piece
import pygame
import time
import random

piece_list = ['i', 'o', 't', 's', 'z']
pieces_at_bottom = []
pygame.init()
screen = pygame.display.set_mode((240, 440))
game_over = False
current_piece = Piece('s')

game_clock = time.time()


def draw_at_bottom():
    for i in pieces_at_bottom:
        i.draw(screen)

while not game_over:
        # each second of game
        if time.time() - game_clock >= 1:
            game_clock = time.time()
            current_piece.move_down()
            if current_piece.at_bottom:
                pieces_at_bottom.append(current_piece)
                current_piece = Piece(random.choice(piece_list))

        # start of event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                        current_piece.rotate()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    current_piece.move_left()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    current_piece.move_right()

        screen.fill((0, 0, 0))
        draw_at_bottom()
        current_piece.draw(screen)

        pygame.display.flip()
