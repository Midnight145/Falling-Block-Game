import pygame


class Piece:
    def __init__(self, piece):

        # Variables that never change between piece to piece.

        self.y = 0
        self.x = 100
        self.piece = piece
        self.at_bottom = False

        # Actual code to define each piece

        if piece == 'i':
            self.color = (45, 254, 254)
            self.width = 20
            self.height = 80
            # Used later in a check
            self.rotated = False

        elif piece == 'o':
            self.color = (255, 253, 56)
            self.width = 40
            self.height = 40

        elif piece == 't':
            # I'm drawing t, j, l, s, and z as 2 rectangles which is why y1, x1, width1, and height1 exist
            self.color = (169, 38, 251)
            self.width = 20
            self.height = 60
            self.y1 = 20
            self.x1 = 120
            self.width1 = 20
            self.height1 = 20
            # Exists for blocks with > 2 orientations
            self.rotate_amount = 0

        elif piece == 's':
            self.color = (41, 253, 47)
            self.width = 20
            self.height = 40
            self.x1 = 120
            self.y1 = 20
            self.width1 = 20
            self.height1 = 40
            self.rotated = False

        elif piece == 'z':
            self.color = (252, 13, 28)
            self.width = 20
            self.height = 40
            self.x = 120
            self.x1 = 100
            self.y1 = 20
            self.width1 = 20
            self.height1 = 40
            self.rotated = False

        elif piece == 'j':
            self.color = (11, 36, 251)
            self.width = 20
            self.height = 60
            self.x1 = 120
            self.y1 = 0
            self.width1 = 20
            self.height1 = 20
            self.rotate_amount = 0

        elif piece == 'l':
            self.color = (253, 164, 41)
            self.width = 20
            self.height = 60
            self.x1 = 100
            self.x = 120
            self.y1 = 0
            self.width1 = 20
            self.height1 = 20
            self.rotate_amount = 0

    # Draws the piece to the screen
    def draw(self, screen):
        if self.piece == 'i' or self.piece == 'o':
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x1, self.y1, self.width1, self.height1))

    # Rotates the piece, this code is a mess.
    def rotate(self):
        if self.piece == 'i':
            # Boundary check
            if self.x + self.height > 240:
                return False
            elif not self.rotated:
                if self.x - self.width < 20:
                    return False
            if self.rotated or not self.rotated:
                self.width, self.height = self.height, self.width
                if self.rotated and not self.at_bottom:
                    self.x += 20
                    self.rotated = False
                elif self.rotated and self.at_bottom:
                    self.x -= 20
                    self.y -= 20
                    self.rotated = True
        # Doesn't need rotated, so I didn't bother.
        elif self.piece == 'o':
            pass

        elif self.piece == 't':
            # Boundary check
            if self.x >= 240 - self.width or self.x >= 240 - self.width1:
                return False
            else:
                self.width, self.height = self.height, self.width
                if self.rotate_amount % 4 == 0:
                    self.x -= 20
                    self.x1 -= 20
                if self.rotated_amount % 4 == 1 and self.at_bottom:
                    self.x += 20
                    self.x1 -= 20
                    self.y -= 20
                elif self.rotate_amount % 4 == 1 and not self.at_bottom:
                    self.x += 20
                    self.x1 -= 20
                elif self.rotate_amount % 4 == 2:
                    self.x -= 20
                    self.y1 -= 20
                    self.y += 20
                    self.x1 += 20
                if self.rotated_amount % 4 == 3 and not self.at_bottom:
                    self.y1 += 20
                    self.y -= 20
                    self.x += 20
                    self.x1 += 20
                elif self.rotate_amount % 4 == 3 and self.at_bottom:
                    # self.y1 += 20
                    self.y -= 20
                    self.x += 20
                    self.x1 += 20

                self.rotate_amount += 1

        elif self.piece == 'z':
            # Boundary check
            if self.x >= 240 - self.height or self.x1 >= 240 - self.height1:
                return False
            else:
                self.width, self.height = self.height, self.width
                self.width1, self.height1 = self.height1, self.width1
                if self.rotated and self.at_bottom:
                    self.x1 -= 20
                    self.x += 20
                    self.y -= 20
                    self.rotated = False
                if self.rotated and not self.at_bottom:
                    self.x1 -= 20
                    self.x += 20
                    self.rotated = False
                else:
                    self.x1 += 20
                    self.x -= 20
                    self.rotated = True

        elif self.piece == 's':
            # Boundary Check
            if self.x >= 240 - self.height or self.x1 >= 240 - self.height1:
                return False
            else:
                self.width, self.height = self.height, self.width
                self.width1, self.height1 = self.height1, self.width1
                if self.rotated and self.at_bottom:
                    self.x1 += 20
                    self.x -= 20
                    self.y -= 20
                    self.rotated = False
                elif self.rotated and not self.at_bottom:
                    self.x1 += 20
                    self.x -= 20
                    self.rotated = False
                else:
                    self.x1 -= 20
                    self.x += 20
                    self.rotated = True

        elif self.piece == 'j':
            # Boundary check
            if self.x > 240 - self.height or self.x1 > 240 - self.height1:
                pass
            elif self.rotate_amount % 4 == 0 or self.rotate_amount % 4 == 2:
                if self.x - self.width < 20 or self.x1 - self.width1 < 20:
                    return False
            if self.rotate_amount > -1:
                self.width, self.height = self.height, self.width
                self.width1, self.height1 = self.height1, self.width1
                if self.rotate_amount % 4 == 0:
                    self.y1 += 20
                    self.x -= 20
                elif self.rotate_amount % 4 == 1 and not self.at_bottom:
                    self.y1 += 20
                    self.x1 -= 20
                    self.x += 40
                elif self.rotate_amount % 4 == 1 and self.at_bottom:
                    self.x1 -= 20
                    self.x += 40
                elif self.rotate_amount % 4 == 2:
                    self.y1 -= 40
                    self.y += 20
                    self.x1 -= 20
                    self.x -= 40
                elif self.rotate_amount % 4 == 3 and not self.at_bottom:
                    self.x += 20
                    self.x1 += 40
                    self.y -= 20
                elif self.rotate_amount % 4 == 3 and self.at_bottom:
                    self.x += 20
                    self.x1 += 40
                    self.y -= 40

                self.rotate_amount += 1

        elif self.piece == 'l':
            # Boundary check
            if self.x > 240 - self.height or self.x1 > 240 - self.height1:
                pass
            elif self.rotate_amount % 4 == 0 or self.rotate_amount % 4 == 2:
                if self.x - self.width < 20 or self.x1 - self.width1 < 20:
                    return False
            if self.rotate_amount > -1:
                self.width, self.height = self.height, self.width
                self.width1, self.height1 = self.height1, self.width1
                if self.rotate_amount % 4 == 0:
                    self.x1 += 20
                    self.x -= 40
                    self.y += 20
                elif self.rotate_amount % 4 == 1:
                    self.y1 += 40
                    self.y -= 20
                    self.x += 20
                elif self.rotate_amount % 4 == 2:
                    self.y1 -= 20
                    self.x1 -= 40
                    self.x -= 20
                elif self.rotate_amount % 4 == 3:
                    self.x += 40
                    self.x1 += 20
                    self.y1 -= 20
                    # self.y -= 40

                self.rotate_amount += 1

    def move_left(self):
        if self.piece == 'i' or self.piece == 'o':
            if self.x <= 20:
                pass
            else:
                self.x -= 20

        else:
            if self.x <= 20 or self.x1 <= 20:
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
        else:
            if self.x1 >= 220 - self.width1 or self.x >= 220 - self.width:
                pass
            else:
                self.x += 20
                self.x1 += 20

    def move_down(self):
        if self.piece == 'i' or self.piece == 'o':
            if self.y + self.height >= 420:
                self.at_bottom = True
            else:
                    self.y += 20

        else:
            if self.y + self.height >= 420 or self.y1 + self.height1 >= 420:
                self.at_bottom = True
            else:
                    self.y += 20
                    self.y1 += 20

# TODO:
# Test bottom boundaries
# Combine bottom boundary checks into 1 if statement
