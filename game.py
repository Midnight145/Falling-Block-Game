from piece_functions.piece import Piece
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((240, 440))
game_over = False


game_clock = time.time()
current_piece = Piece('t')

while not game_over:
        # each second of game
        if time.time() - game_clock >= 1:
            game_clock = time.time()
            current_piece.move_down()

        # start of event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if current_piece.x >= 180:
                        pass
                    else:
                        current_piece.rotate()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    current_piece.move_left()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    current_piece.move_right()

        screen.fill((0, 0, 0))
        current_piece.draw(screen)

        pygame.display.flip()
