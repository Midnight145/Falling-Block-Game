from piece_functions.piece import Piece
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((260, 440))
game_over = False


game_clock = time.time()
current_piece = Piece('i', 20, 80)

while not game_over:
        # each second of game
        if time.time() - game_clock >= 1:
            game_clock = time.time()
            current_piece.y += 20

        # start of event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if current_piece.x >= 180:
                        pass
                    else:
                        current_piece.rotate('i')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if current_piece.x <= 20:
                        pass
                    else:
                        current_piece.x -= 20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    if current_piece.x >= 240 - 80:
                        pass
                    else:
                        current_piece.x += 20

        screen.fill((0, 0, 0))
        current_piece.draw('i', screen, current_piece.color, current_piece.x, current_piece.y, current_piece.width, current_piece.height)

        pygame.display.flip()
