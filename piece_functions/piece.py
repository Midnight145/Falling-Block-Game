import pygame
import random

things_at_bottom = []


class Piece:
    def __init__(self):
        # Variables that never change between piece to piece.

        self.lock = False
        # Used later in a check
        self.rotate_amount = 0
        self.color = (0, 0, 0)
        self.rect = None
        self.rect1 = None
        self.rect2 = None
        self.rect3 = None
        # Used for efficient code writing, so I can loop over the rects.
        self.rects = [self.rect, self.rect1, self.rect2, self.rect3]

    # Draws the piece to the screen

    def draw(self, screen):
        for i in self.rects:
            pygame.draw.rect(screen, self.color, i)

    # Rotates the piece, this code is a mess.
    def rotate(self, boundaries):
        pass

    def move(self, boundaries, coords):
        for i in self.rects:
            i.move_ip(coords[0], coords[1])

        if not self.collideCheck(boundaries):
            for i in self.rects:
                # Moves pieces back if it couldn't move it in that direction.
                i.move_ip(-coords[0], -coords[1])
                # If pieces are moving down, lock them.
                if coords == (0, 20):
                    things_at_bottom.append(i)
                    self.lock = True

        # I don't know why this works. But, it does. It checks to make sure the piece can move in that direction.

    def collideCheck(self, boundaries):
        if all(-1 == x.collidelist(boundaries) for x in self.rects) \
                and all(-1 == x.collidelist(things_at_bottom) for x in self.rects):
            return True
        else:
            return False

    def wall_kick(self, boundaries):
        pass


class IPiece(Piece):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(80, 0, 20, 20)
        self.rect1 = pygame.Rect(100, 0, 20, 20)
        self.rect2 = pygame.Rect(120, 0, 20, 20)
        self.rect3 = pygame.Rect(140, 0, 20, 20)
        self.color = (45, 254, 254)
        self.rects = [self.rect, self.rect1, self.rect2, self.rect3]

    def rotate(self, boundaries):

        if self.rotate_amount > -1:
            print(self.rotate_amount)
            if self.rotate_amount % 4 == 0:
                self.rect.move_ip(40, -20)
                self.rect1.move_ip(20, 0)
                self.rect2.move_ip(0, 20)
                self.rect3.move_ip(-20, 40)
                if not self.collideCheck(boundaries):

                    self.rect.move_ip(-40, 20)
                    self.rect1.move_ip(-20, 0)
                    self.rect2.move_ip(0, -20)
                    self.rect3.move_ip(20, -40)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(20, 40)
                self.rect1.move_ip(0, 20)
                self.rect2.move_ip(-20, 0)
                self.rect3.move_ip(-40, -20)
                if not self.collideCheck(boundaries):
                    self.wall_kick(boundaries)
                    # self.rect.move_ip(-20, -40)
                    # self.rect1.move_ip(0, -20)
                    # self.rect2.move_ip(20, 0)
                    # self.rect3.move_ip(40, 20)
                    # self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(-40, 20)
                self.rect1.move_ip(-20, 0)
                self.rect2.move_ip(0, -20)
                self.rect3.move_ip(20, -40)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(40, -20)
                    self.rect1.move_ip(20, 0)
                    self.rect2.move_ip(0, 20)
                    self.rect3.move_ip(-20, 40)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(-20, -40)
                self.rect1.move_ip(0, -20)
                self.rect2.move_ip(20, 0)
                self.rect3.move_ip(40, 20)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(20, 40)
                    self.rect1.move_ip(0, 20)
                    self.rect2.move_ip(-20, 0)
                    self.rect3.move_ip(-40, -20)
                    self.rotate_amount -= 1

            self.rotate_amount += 1

    def wall_kick(self, boundaries):
        if not self.collideCheck(boundaries) and self.rotate_amount % 4 == 1:
            for i in self.rects:
                i.move_ip(-20, 0)
            if self.collideCheck(boundaries):
                return 0
            else:
                for i in self.rects:
                    i.move_ip(20, 0)
            for i in self.rects:
                i.move_ip(20, 0)
            if self.collideCheck(boundaries):
                return 0
            else:
                for i in self.rects:
                    i.move_ip(-20, 0)
            for i in self.rects:
                i.move_ip(-40, 20)
            if self.collideCheck(boundaries):
                return 0
            else:
                for i in self.rects:
                    i.move_ip(40, -20)
            for i in self.rects:
                i.move_ip(20, -40)
            if self.collideCheck(boundaries):
                return 0
            else:
                for i in self.rects:
                    i.move_ip(-20, 40)


class OPiece(Piece):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(100, 0, 20, 20)
        self.rect1 = pygame.Rect(120, 0, 20, 20)
        self.rect2 = pygame.Rect(100, 20, 20, 20)
        self.rect3 = pygame.Rect(120, 20, 20, 20)
        self.rects = [self.rect, self.rect1, self.rect2, self.rect3]
        self.color = (255, 253, 56)


class TPiece(Piece):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(80, 20, 20, 20)
        self.rect1 = pygame.Rect(100, 20, 20, 20)
        self.rect2 = pygame.Rect(120, 20, 20, 20)
        self.rect3 = pygame.Rect(100, 0, 20, 20)
        self.rects = [self.rect, self.rect1, self.rect2, self.rect3]
        self.color = (169, 38, 251)

    def rotate(self, boundaries):

        if self.rotate_amount % 4 == 0:

            self.rect.move_ip(20, -20)
            self.rect2.move_ip(-20, 20)
            self.rect3.move_ip(20, 20)
            if not self.collideCheck(boundaries):
                self.rect.move_ip(-20, 20)
                self.rect2.move_ip(20, -20)
                self.rect3.move_ip(-20, -20)
                self.rotate_amount -= 1

        elif self.rotate_amount % 4 == 1:
            self.rect.move_ip(20, 20)
            self.rect2.move_ip(-20, -20)
            self.rect3.move_ip(-20, 20)
            if not self.collideCheck(boundaries):
                self.rect.move_ip(-20, -20)
                self.rect2.move_ip(20, 20)
                self.rect3.move_ip(20, -20)
                self.rotate_amount -= 1

        elif self.rotate_amount % 4 == 2:
            self.rect.move_ip(-20, 20)
            self.rect2.move_ip(20, -20)
            self.rect3.move_ip(-20, -20)
            if not self.collideCheck(boundaries):
                self.rect.move_ip(20, -20)
                self.rect2.move_ip(-20, 20)
                self.rect3.move_ip(20, 20)
                self.rotate_amount -= 1

        elif self.rotate_amount % 4 == 3:
            self.rect.move_ip(-20, -20)
            self.rect2.move_ip(20, 20)
            self.rect3.move_ip(20, -20)
            if not self.collideCheck(boundaries):
                self.rect.move_ip(20, 20)
                self.rect2.move_ip(-20, -20)
                self.rect3.move_ip(-20, 20)
                self.rotate_amount -= 1

        self.rotate_amount += 1


class SPiece(Piece):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(100, 0, 20, 20)
        self.rect1 = pygame.Rect(120, 0, 20, 20)
        self.rect2 = pygame.Rect(80, 20, 20, 20)
        self.rect3 = pygame.Rect(100, 20, 20, 20)
        self.rects = [self.rect, self.rect1, self.rect2, self.rect3]
        self.color = (41, 253, 47)

    def rotate(self, boundaries):

        if self.rotate_amount > -1:

            if self.rotate_amount % 4 == 0:
                self.rect.move_ip(20, 20)
                self.rect1.move_ip(0, 40)
                self.rect2.move_ip(20, -20)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(-20, -20)
                    self.rect1.move_ip(0, -40)
                    self.rect2.move_ip(-20, 20)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(-20, 20)
                self.rect1.move_ip(-40, 0)
                self.rect2.move_ip(20, 20)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(20, -20)
                    self.rect1.move_ip(40, 0)
                    self.rect2.move_ip(-20, -20)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(-20, -20)
                self.rect1.move_ip(0, -40)
                self.rect2.move_ip(-20, 20)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(20, 20)
                    self.rect1.move_ip(0, 40)
                    self.rect2.move_ip(20, -20)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(20, -20)
                self.rect1.move_ip(40, 0)
                self.rect2.move_ip(-20, -20)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(-20, 20)
                    self.rect1.move_ip(-40, 0)
                    self.rect2.move_ip(20, 20)
                    self.rotate_amount -= 1
            self.rotate_amount += 1


class ZPiece(Piece):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(80, 0, 20, 20)
        self.rect1 = pygame.Rect(100, 0, 20, 20)
        self.rect2 = pygame.Rect(100, 20, 20, 20)
        self.rect3 = pygame.Rect(120, 20, 20, 20)
        self.rects = [self.rect, self.rect1, self.rect2, self.rect3]
        self.color = (252, 13, 28)

    def rotate(self, boundaries):

        if self.rotate_amount > -1:

            if self.rotate_amount % 4 == 0:
                self.rect.move_ip(40, 0)
                self.rect1.move_ip(20, 20)
                self.rect3.move_ip(-20, 20)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(-40, 0)
                    self.rect1.move_ip(-20, -20)
                    self.rect3.move_ip(20, -20)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(0, 40)
                self.rect1.move_ip(-20, 20)
                self.rect3.move_ip(-20, -20)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(0, -40)
                    self.rect1.move_ip(20, -20)
                    self.rect3.move_ip(20, 20)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(-40, 0)
                self.rect1.move_ip(-20, -20)
                self.rect3.move_ip(20, -20)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(40, 0)
                    self.rect1.move_ip(20, 20)
                    self.rect3.move_ip(-20, 20)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(0, -40)
                self.rect1.move_ip(20, -20)
                self.rect3.move_ip(20, 20)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(0, 40)
                    self.rect1.move_ip(-20, 20)
                    self.rect3.move_ip(-20, -20)
                    self.rotate_amount -= 1

            self.rotate_amount += 1


class JPiece(Piece):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(80, 20, 20, 20)
        self.rect1 = pygame.Rect(100, 20, 20, 20)
        self.rect2 = pygame.Rect(120, 20, 20, 20)
        self.rect3 = pygame.Rect(80, 0, 20, 20)
        self.rects = [self.rect, self.rect1, self.rect2, self.rect3]
        self.color = (11, 36, 251)

    def rotate(self, boundaries):

        if self.rotate_amount > -1:

            if self.rotate_amount % 4 == 0:
                self.rect.move_ip(20, -20)
                self.rect2.move_ip(-20, 20)
                self.rect3.move_ip(40, 0)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(-20, 20)
                    self.rect2.move_ip(20, -20)
                    self.rect3.move_ip(-40, 0)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(20, 20)
                self.rect2.move_ip(-20, -20)
                self.rect3.move_ip(0, 40)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(-20, -20)
                    self.rect2.move_ip(20, 20)
                    self.rect3.move_ip(0, -40)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(-20, 20)
                self.rect2.move_ip(20, -20)
                self.rect3.move_ip(-40, 0)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(20, -20)
                    self.rect2.move_ip(-20, 20)
                    self.rect3.move_ip(40, 0)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(-20, -20)
                self.rect2.move_ip(20, 20)
                self.rect3.move_ip(0, -40)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(20, 20)
                    self.rect2.move_ip(-20, -20)
                    self.rect3.move_ip(0, 40)
                    self.rotate_amount -= 1

            self.rotate_amount += 1


class LPiece(Piece):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(80, 20, 20, 20)
        self.rect1 = pygame.Rect(100, 20, 20, 20)
        self.rect2 = pygame.Rect(120, 20, 20, 20)
        self.rect3 = pygame.Rect(120, 0, 20, 20)
        self.rects = [self.rect, self.rect1, self.rect2, self.rect3]
        self.color = (253, 164, 41)

    def rotate(self, boundaries):

        if self.rotate_amount > -1:

            if self.rotate_amount % 4 == 0:
                self.rect.move_ip(20, -20)
                self.rect2.move_ip(-20, 20)
                self.rect3.move_ip(0, 40)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(-20, 20)
                    self.rect2.move_ip(20, -20)
                    self.rect3.move_ip(0, -40)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(20, 20)
                self.rect2.move_ip(-20, -20)
                self.rect3.move_ip(-40, 0)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(-20, -20)
                    self.rect2.move_ip(20, 20)
                    self.rect3.move_ip(40, 0)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(-20, 20)
                self.rect2.move_ip(20, -20)
                self.rect3.move_ip(0, -40)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(20, -20)
                    self.rect2.move_ip(-20, 20)
                    self.rect3.move_ip(0, 40)
                    self.rotate_amount -= 1

            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(-20, -20)
                self.rect2.move_ip(20, 20)
                self.rect3.move_ip(40, 0)
                if not self.collideCheck(boundaries):
                    self.rect.move_ip(20, 20)
                    self.rect2.move_ip(-20, -20)
                    self.rect3.move_ip(-40, 0)
                    self.rotate_amount -= 1

            self.rotate_amount += 1


def choose_piece(pieces):
    piece = random.choice(pieces)
    if piece == 'i':
        return IPiece()
    if piece == 'o':
        return OPiece()
    if piece == 't':
        return TPiece()
    if piece == 's':
        return SPiece()
    if piece == 'z':
        return ZPiece()
    if piece == 'j':
        return JPiece()
    if piece == 'l':
        return LPiece()


def draw_at_bottom(screen, pieces):
    for i in pieces:
        i.draw(screen)


def force_down(piecelist):
    for i in piecelist:
        i.move_ip(0, 20)
