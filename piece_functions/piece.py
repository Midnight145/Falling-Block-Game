import pygame


class Piece:

    def __init__(self, piece):

        # Variables that never change between piece to piece.

        self.piece = piece
        self.at_bottom = False
        # Used later in a check
        self.rotate_amount = 0

        # Actual code to define each piece

        if piece == 'i':
            self.color = (45, 254, 254)

            self.rect = pygame.Rect(80, 0, 80, 20)

        elif piece == 'o':
            self.color = (255, 253, 56)

            self.rect = pygame.Rect(100, 0, 40, 40)

        elif piece == 't':
            # I'm drawing t, j, l, s, and z as 2 rectangles
            self.color = (169, 38, 251)

            self.rect = pygame.Rect(80, 20, 60, 20)
            self.rect1 = pygame.Rect(100, 0, 20, 20)

        elif piece == 's':
            self.color = (41, 253, 47)

            self.rect = pygame.Rect(100, 0, 40, 20)
            self.rect1 = pygame.Rect(80, 20, 40, 20)

        elif piece == 'z':
            self.color = (252, 13, 28)

            self.rect = pygame.Rect(80, 0, 40, 20)
            self.rect1 = pygame.Rect(100, 20, 40, 20)

        elif piece == 'j':
            self.color = (11, 36, 251)

            self.rect = pygame.Rect(80, 20, 60, 20)
            self.rect1 = pygame.Rect(80, 0, 20, 20)

        elif piece == 'l':
            self.color = (253, 164, 41)

            self.rect = pygame.Rect(80, 20, 60, 20)
            self.rect1 = pygame.Rect(120, 0, 20, 20)

    # Draws the piece to the screen
    def draw(self, screen):
        if self.piece == 'i' or self.piece == 'o':
            pygame.draw.rect(screen, self.color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, self.color, self.rect1)

    # Rotates the piece, this code is a mess.
    def rotate(self):
        if self.piece == 'i':
            # Boundary check
            # if self.rect.x + self.rect.height > 240:
            #     return False
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
                return True

        # Doesn't need rotated, so I didn't bother.
        elif self.piece == 'o':
            return True

        elif self.piece == 't':
            # Boundary check
            # if self.rect.x >= 240 - self.rect.width or self.rect.x >= 240 - self.rect1.width:
            #     return False
            # else:
            if self.rotate_amount > -1:
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
                return True

        elif self.piece == 's':
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
                    self.rect1.move_ip(-20, 0
                                       )
                self.rotate_amount += 1
                return True

        elif self.piece == 'z':
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
                return True

        elif self.piece == 'j':
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
                return True

        elif self.piece == 'l':
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
                return True

    def move_left(self):
        if self.piece == 'i' or self.piece == 'o':
            if self.rect.x <= 20:
                return False
            else:
                self.rect.move_ip(-20, 0)

        else:
            if self.rect.x <= 20 or self.rect1.x <= 20:
                return False
            else:
                self.rect.move_ip(-20, 0)
                self.rect1.move_ip(-20, 0)

    def move_right(self):
        if self.piece == 'i' or self.piece == 'o':
            if self.rect.x >= 220 - self.rect.width:
                return False
            else:
                self.rect.move_ip(20, 0)
        else:
            if self.rect1.x >= 220 - self.rect1.width or self.rect.x >= 220 - self.rect.width:
                return False
            else:
                self.rect.move_ip(20, 0)
                self.rect1.move_ip(20, 0)

    def move_down(self):
        if self.piece == 'i' or self.piece == 'o':
            if self.rect.y + self.rect.height >= 420:
                self.at_bottom = True
            else:
                self.rect.move_ip(0, 20)
        elif self.piece == 't':
            if self.rect.y + self.rect.height >= 420 or self.rect1.y + self.rect1.height >= 420:
                self.at_bottom = True
            else:
                    self.rect.move_ip(0, 20)
                    self.rect1.move_ip(0, 20)
        else:
            if self.rect.y + self.rect.height >= 420 or self.rect1.y + self.rect1.height >= 420:
                self.at_bottom = True
            else:
                    self.rect.move_ip(0, 20)
                    self.rect1.move_ip(0, 20)

# TODO:
# Test bottom boundaries
# Combine bottom boundary checks into 1 if statement
