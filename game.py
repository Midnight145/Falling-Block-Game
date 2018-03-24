from piece_functions.piece import *
import pygame
import time
import random

game_clock = time.time()
moving_clock = time.time()

piece_list = [IPiece(), OPiece(), TPiece(), SPiece(), ZPiece(), JPiece(), LPiece()]
pieces_at_bottom = []
pygame.init()
screen = pygame.display.set_mode((240, 440))
game_over = False
current_piece = random.choice(piece_list)
# current_piece = OPiece()

debug = False

print(current_piece)

move_time = 1
level = 1
moving_right = False
moving_left = False
moving_down = False


def draw_at_bottom():
    for i in pieces_at_bottom:
        i.draw(screen)

while not game_over:
        # each second of game
        # Controls pieces moving down
        if not debug:
            if time.time() - game_clock >= move_time:
                if not moving_down:
                    game_clock = time.time()
                    current_piece.move_down()
                if current_piece.at_bottom:
                    pieces_at_bottom.append(current_piece)
                    current_piece = random.choice(piece_list)

        # start of event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # used for debugging
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                debug = not debug
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                current_piece.rotate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                moving_down = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                moving_left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                moving_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    moving_down = False
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_RIGHT:
                    moving_right = False
        if moving_left:
            if time.time() - moving_clock >= .15:
                moving_clock = time.time()
                current_piece.move_left()
        if moving_right:
            if time.time() - moving_clock >= .15:
                moving_clock = time.time()
                current_piece.move_right()
        if moving_down:
            if time.time() - moving_clock >= .07:
                moving_clock = time.time()
                if current_piece.at_bottom:
                    pieces_at_bottom.append(current_piece)
                    current_piece = random.choice(piece_list)
                current_piece.move_down()

        screen.fill((0, 0, 0))

        draw_at_bottom()
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 20, 440), 0)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(220, 0, 20, 440), 0)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(20, 420, 240, 20), 0)
        current_piece.draw(screen)
        pygame.display.flip()
