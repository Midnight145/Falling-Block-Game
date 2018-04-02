import pygame
import random

things_at_bottom = []


class Piece:
    # Variables that never change between piece to piece.

    lock = False
    # Used later in a check
    rotate_amount = 0

    def __init__(self):
        pass

    # Draws the piece to the screen
    def draw(self, screen):
        pass

    # Rotates the piece, this code is a mess.
    def rotate(self):
        pass

    def move_left(self, boundaries, piece):
        pass

    def move_right(self, boundaries, piece):
        pass

    def move_down(self, boundaries):
        pass


class IPiece(Piece):
    def __init__(self):
        self.rect = pygame.Rect(80, 0, 80, 20)
        self.color = (45, 254, 254)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def rotate(self):
        if self.rotate_amount > -1:
            self.rect.width, self.rect.height = self.rect.height, self.rect.width
            if self.rotate_amount % 4 == 0:
                self.rect.move_ip(40, -20)
            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(-40, 40)
            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(20, -40)
            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(-20, 20)

            self.rotate_amount += 1

    def move_left(self, boundaries):
        self.rect.move_ip(-20, 0)
        if self.rect.collidelist(boundaries) == -1 and self.rect.collidelist(things_at_bottom) == -1:
            return True
        else:
            self.rect.move_ip(20, 0)

    def move_right(self, boundaries):
        self.rect.move_ip(20, 0)
        if self.rect.collidelist(boundaries) == -1 and self.rect.collidelist(things_at_bottom) == -1:
            return True
        else:
            self.rect.move_ip(-20, 0)

    def move_down(self, boundaries):
        self.rect.move_ip(0, 20)
        if self.rect.collidelist(boundaries) == -1 and self.rect.collidelist(things_at_bottom) == -1:
            return True
        else:
            self.rect.move_ip(0, -20)
            things_at_bottom.append(self.rect)
            self.lock = True
            return False


class OPiece(Piece):
    def __init__(self):
        self.rect = pygame.Rect(100, 0, 40, 40)
        self.color = (255, 253, 56)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def rotate(self):
        pass

    def move_left(self, boundaries):
        self.rect.move_ip(-20, 0)
        if self.rect.collidelist(boundaries) == -1 and self.rect.collidelist(things_at_bottom) == -1:
            return False
        else:
            self.rect.move_ip(20, 0)

    def move_right(self, boundaries):
        self.rect.move_ip(20, 0)
        if self.rect.collidelist(boundaries) == -1 and self.rect.collidelist(things_at_bottom) == -1:
            return False
        else:
            self.rect.move_ip(-20, 0)

    def move_down(self, boundaries):
        self.rect.move_ip(0, 20)
        if self.rect.collidelist(boundaries) == -1 and self.rect.collidelist(things_at_bottom) == -1:
            return True
        else:
            self.rect.move_ip(0, -20)
            things_at_bottom.append(self.rect)
            self.lock = True
            return False


class TPiece(Piece):
    def __init__(self):
        self.rect = pygame.Rect(80, 20, 60, 20)
        self.rect1 = pygame.Rect(100, 0, 20, 20)
        self.color = (169, 38, 251)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, self.color, self.rect1)

    def rotate(self):
        self.rect.width, self.rect.height = self.rect.height, self.rect.width
        if self.rotate_amount % 4 == 0:
            self.rect.move_ip(20, -20)
            self.rect1.move_ip(20, 20)
        elif self.rotate_amount % 4 == 1:
            self.rect.move_ip(-20, 20)
            self.rect1.move_ip(-20, 20)
        elif self.rotate_amount % 4 == 2:
            self.rect.move_ip(20, -20)
            self.rect1.move_ip(-20, -20)
        elif self.rotate_amount % 4 == 3:
            self.rect.move_ip(-20, 20)
            self.rect1.move_ip(20, -20)

        self.rotate_amount += 1

    def move_left(self, boundaries):
        self.rect.move_ip(-20, 0)
        self.rect1.move_ip(-20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(20, 0)
            self.rect1.move_ip(20, 0)

    def move_right(self, boundaries):

        self.rect.move_ip(20, 0)
        self.rect1.move_ip(20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(-20, 0)
            self.rect1.move_ip(-20, 0)

    def move_down(self, boundaries):

        self.rect.move_ip(0, 20)
        self.rect1.move_ip(0, 20)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(0, -20)
            self.rect1.move_ip(0, -20)
            self.lock = True
            things_at_bottom.append(self.rect)
            things_at_bottom.append(self.rect1)


class SPiece(Piece):
    def __init__(self):
        self.rect = pygame.Rect(100, 0, 40, 20)
        self.rect1 = pygame.Rect(80, 20, 40, 20)
        self.color = (41, 253, 47)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, self.color, self.rect1)

    def rotate(self):
        # Boundary Check
        # if self.rect.x >= 240 - self.rect.height or self.rect1.x >= 240 - self.rect1.height:
        #     return False
        # else:
        if self.rotate_amount > -1:
            self.rect.width, self.rect.height = self.rect.height, self.rect.width
            self.rect1.width, self.rect1.height = self.rect1.height, self.rect1.width
            if self.rotate_amount % 4 == 0:
                self.rect1.move_ip(40, 0)
            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(0, 20)
                self.rect1.move_ip(-40, 20)
            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(-20, -20)
                self.rect1.move_ip(20, -20)
            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(20, 0)
                self.rect1.move_ip(-20, 0)
            self.rotate_amount += 1

    def move_left(self, boundaries):
        self.rect.move_ip(-20, 0)
        self.rect1.move_ip(-20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(20, 0)
            self.rect1.move_ip(20, 0)

    def move_right(self, boundaries):

        self.rect.move_ip(20, 0)
        self.rect1.move_ip(20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(-20, 0)
            self.rect1.move_ip(-20, 0)

    def move_down(self, boundaries):

        self.rect.move_ip(0, 20)
        self.rect1.move_ip(0, 20)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(0, -20)
            self.rect1.move_ip(0, -20)
            self.lock = True
            things_at_bottom.append(self.rect)
            things_at_bottom.append(self.rect1)


class ZPiece(Piece):
    def __init__(self):
        self.rect = pygame.Rect(80, 0, 40, 20)
        self.rect1 = pygame.Rect(100, 20, 40, 20)
        self.color = (252, 13, 28)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, self.color, self.rect1)

    def rotate(self):
        # Boundary check
        # if self.rect.x >= 240 - self.rect.height or self.rect1.x >= 240 - self.rect1.height:
        #     return False
        # else:
        if self.rotate_amount > -1:
            self.rect.width, self.rect.height = self.rect.height, self.rect.width
            self.rect1.width, self.rect1.height = self.rect1.height, self.rect1.width
            if self.rotate_amount % 4 == 0:
                self.rect.move_ip(40, 0)
            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(-40, 20)
                self.rect1.move_ip(0, 20)
            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(20, -20)
                self.rect1.move_ip(-20, -20)
            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(-20, 0)
                self.rect1.move_ip(20, 0)

            self.rotate_amount += 1

    def move_left(self, boundaries):
        self.rect.move_ip(-20, 0)
        self.rect1.move_ip(-20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(20, 0)
            self.rect1.move_ip(20, 0)

    def move_right(self, boundaries):

        self.rect.move_ip(20, 0)
        self.rect1.move_ip(20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(-20, 0)
            self.rect1.move_ip(-20, 0)

    def move_down(self, boundaries):

        self.rect.move_ip(0, 20)
        self.rect1.move_ip(0, 20)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(0, -20)
            self.rect1.move_ip(0, -20)
            self.lock = True
            things_at_bottom.append(self.rect)
            things_at_bottom.append(self.rect1)


class JPiece(Piece):
    def __init__(self):
        self.rect = pygame.Rect(80, 20, 60, 20)
        self.rect1 = pygame.Rect(80, 0, 20, 20)
        self.color = (11, 36, 251)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, self.color, self.rect1)

    def rotate(self):
        # Boundary check
        # if self.rect.x > 240 - self.rect.height or self.rect1.x > 240 - self.rect1.height:
        #     pass
        # elif self.rotate_amount % 4 == 0 or self.rotate_amount % 4 == 2:
        #     if self.rect.x - self.rect.width < 20 or self.rect1.x - self.rect1.width < 20:
        #         return False
        if self.rotate_amount > -1:
            self.rect.width, self.rect.height = self.rect.height, self.rect.width
            self.rect1.width, self.rect1.height = self.rect1.height, self.rect1.width
            if self.rotate_amount % 4 == 0:
                self.rect.move_ip(20, -20)
                self.rect1.move_ip(40, 0)
            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(-20, 20)
                self.rect1.move_ip(0, 40)
            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(20, -20)
                self.rect1.move_ip(-40, 0)
            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(-20, 20)
                self.rect1.move_ip(0, -40)

            self.rotate_amount += 1

    def move_left(self, boundaries):
        self.rect.move_ip(-20, 0)
        self.rect1.move_ip(-20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(20, 0)
            self.rect1.move_ip(20, 0)

    def move_right(self, boundaries):

        self.rect.move_ip(20, 0)
        self.rect1.move_ip(20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(-20, 0)
            self.rect1.move_ip(-20, 0)

    def move_down(self, boundaries):

        self.rect.move_ip(0, 20)
        self.rect1.move_ip(0, 20)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(0, -20)
            self.rect1.move_ip(0, -20)
            self.lock = True
            things_at_bottom.append(self.rect)
            things_at_bottom.append(self.rect1)


class LPiece(Piece):
    def __init__(self):
        self.rect = pygame.Rect(80, 20, 60, 20)
        self.rect1 = pygame.Rect(120, 0, 20, 20)
        self.color = (253, 164, 41)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, self.color, self.rect1)

    def rotate(self):
        # Boundary check
        # if self.rect.x > 240 - self.rect.height or self.rect1.x > 240 - self.rect1.height:
        #     pass
        # elif self.rotate_amount % 4 == 0 or self.rotate_amount % 4 == 2:
        #     if self.rect.x - self.rect.width < 20 or self.rect1.x - self.rect1.width < 20:
        #         return False
        if self.rotate_amount > -1:
            self.rect.width, self.rect.height = self.rect.height, self.rect.width
            self.rect1.width, self.rect1.height = self.rect1.height, self.rect1.width
            if self.rotate_amount % 4 == 0:
                self.rect.move_ip(20, -20)
                self.rect1.move_ip(0, 40)
            elif self.rotate_amount % 4 == 1:
                self.rect.move_ip(-20, 20)
                self.rect1.move_ip(-40, 0)
            elif self.rotate_amount % 4 == 2:
                self.rect.move_ip(20, -20)
                self.rect1.move_ip(0, -40)
            elif self.rotate_amount % 4 == 3:
                self.rect.move_ip(-20, 20)
                self.rect1.move_ip(40, 0)

            self.rotate_amount += 1

    def move_left(self, boundaries):
        self.rect.move_ip(-20, 0)
        self.rect1.move_ip(-20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(20, 0)
            self.rect1.move_ip(20, 0)

    def move_right(self, boundaries):

        self.rect.move_ip(20, 0)
        self.rect1.move_ip(20, 0)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(-20, 0)
            self.rect1.move_ip(-20, 0)

    def move_down(self, boundaries):

        self.rect.move_ip(0, 20)
        self.rect1.move_ip(0, 20)
        if (self.rect.collidelist(boundaries) == -1 and self.rect1.collidelist(boundaries) == -1
                and self.rect.collidelist(things_at_bottom) == -1 and self.rect1.collidelist(things_at_bottom) == -1):
            pass
        else:
            self.rect.move_ip(0, -20)
            self.rect1.move_ip(0, -20)
            self.lock = True
            things_at_bottom.append(self.rect)
            things_at_bottom.append(self.rect1)


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