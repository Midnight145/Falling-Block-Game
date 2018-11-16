from piece_functions.piece import *
import pygame
import time

left = (-20, 0)
right = (20, 0)
down = (0, 20)

game_clock = time.time()
moving_clock = time.time()

boundaries = [pygame.Rect(0, 0, 20, 440), pygame.Rect(220, 0, 20, 440), pygame.Rect(20, 420, 240, 20)]

piece_list = ['i', 'o', 't', 's', 'z', 'j', 'l']

pieces_at_bottom = []
pygame.init()
screen = pygame.display.set_mode((240, 440))
game_over = False
current_piece = choose_piece(piece_list)

debug = False

move_time = 1
level = 1
moving_right = False
moving_left = False
moving_down = False

while not game_over:
        # each second of game
        # Controls pieces moving down
        if not debug:
            if time.time() - game_clock >= move_time:
                if not moving_down:
                    game_clock = time.time()

                current_piece.move(boundaries, down)

        if current_piece.lock:
            pieces_at_bottom.append(current_piece)
            current_piece = choose_piece(piece_list)

        # start of event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # used for debugging
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                debug = not debug
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                current_piece.rotate(boundaries)
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
                current_piece.move(boundaries, left)
        if moving_right:
            if time.time() - moving_clock >= .15:
                moving_clock = time.time()
                current_piece.move(boundaries, right)
        if moving_down:
            if time.time() - moving_clock >= .07:
                moving_clock = time.time()
                current_piece.move(boundaries, down)

        screen.fill((0, 0, 0))
        draw_at_bottom(screen, pieces_at_bottom)
        for i in range(len(boundaries)):
            pygame.draw.rect(screen, (255, 255, 255), boundaries[i], 0)
        current_piece.draw(screen)
        pygame.display.flip()

