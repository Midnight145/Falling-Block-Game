import pygame


class Piece:
    def __init__(self, piece, width, height):
        self.x = 120
        self.y = 0
        self.piece = piece
        self.width = width
        self.height = height
        if piece == 'i':
            self.color = (0, 21, 255)

    def draw(self, piece, screen, color, x, y, width, height):
        if piece == 'i':
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))

    def rotate(self, piece):
        if piece == "i":
            self.width, self.height = self.height, self.width
            return self.width, self.height
