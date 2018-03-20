import pygame
import math

pieces_at_bottom = []


class Piece:

    def __init__(self, piece):
        self.y = 0
        self.x = 100
        self.piece = piece
        self.at_bottom = False

        if piece == 'i':
            self.color = (0, 0, 255)
            self.width = 20
            self.height = 80

        elif piece == 'o':
            self.color = (0, 255, 0)
            self.width = 40
            self.height = 40

        elif piece == 't':
            self.color = (255, 128, 0)
            # self.points = ([100, 0], [100, 60], [120, 20], [120, 40], [120, 60], [120, 0])
            self.width = 20
            self.height = 60
            self.y1 = 20
            self.x1 = 120
            self.width1 = 20
            self.height1 = 20
            self.rotate_amount = 0

    def draw(self, screen):
        if self.piece == 'i' or self.piece == 'o':
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        elif self.piece == 't':
            # pygame.draw.polygon(screen, self.color, self.points, self.width)
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x1, self.y1, self.width1, self.height1))

    def rotate(self):
        if self.x >= 240 - self.width:
            pass

        if self.piece == "i":
            if self.x >= 240 - self.width:
                pass
            else:
                self.width, self.height = self.height, self.width
        elif self.piece == 'o':
            pass
        elif self.piece == 't':
            if self.x >= 240 - self.width or self.x >= 240 - self.width1:
                pass
            else:
                y = self.y
                x = self.x
                if self.rotate_amount == 0:
                    self.width, self.height = self.height, self.width
                    self.rotate_amount += 1
                    self.x -= 20
                    self.x1 -= 20
                elif self.rotate_amount == 1:
                    self.width, self.height = self.height, self.width
                    self.x += 20
                    self.x1 -= 20
                    self.rotate_amount += 1
                elif self.rotate_amount == 2:
                    self.width, self.height = self.height, self.width
                    self.x -= 20
                    self.y1 -= 20
                    self.y += 20
                    self.x1 += 20
                    self.rotate_amount += 1
                elif self.rotate_amount == 3:
                    self.width, self.height = self.height, self.width
                    self.y1 += 20
                    self.y -= 20
                    self.x += 20
                    self.x1 += 20
                    self.rotate_amount = 0

    def move_left(self):
        if self.piece == 'i' or self.piece == 'o':
            if self.x <= 20:
                pass
            else:
                self.x -= 20

        if self.piece == 't':
            if self.x <= 20:
                pass
            else:
                self.x -= 20
                self.x1 -= 20

    def move_right(self):
        if self.piece == 'i' or self.piece == 'o':
            if self.x >= 220 - self.width:
                pass
            else:
                self.x += 20
        if self.piece == 't':
            if self.x1 >= 220 - self.width1 or self.x >= 220 - self.width:
                pass
            else:
                self.x += 20
                self.x1 += 20

    def move_down(self):
        try:
            if self.y + self.height >= 420 or self.y1 + self.width1 >= 420:
                self.at_bottom = True
            else:
                if self.piece == 'i' or self.piece == 'o':
                    self.y += 20
                elif self.piece == 't':
                    self.y += 20
                    self.y1 += 20
        except AttributeError:
            if self.y + self.height >= 420:
                self.at_bottom = True
            else:
                if self.piece == 'i' or self.piece == 'o':
                    self.y += 20
