import pygame


class Piece:
    def __init__(self, piece):
        self.y = 0
        self.piece = piece
        if piece == 'i':
            self.color = (0, 0, 255)
            self.width = 20
            self.height = 80
            self.x = 100
        elif piece == 'o':
            self.color = (0, 255, 0)
            self.width = 40
            self.height = 40
            self.x = 100

    def draw(self, screen):
        if self.piece == 'i' or self.piece == 'o':
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def rotate(self):
        if self.piece == "i":
            self.width, self.height = self.height, self.width
            return self.width, self.height
        elif self.piece == 'o':
            pass
