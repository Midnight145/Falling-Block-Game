import pygame


class Piece:
    def __init__(self, piece):
        self.y = 0
        self.x = 100
        self.piece = piece
        self.at_bottom = False

        if piece == 'i':
            self.color = (45, 254, 254)
            self.width = 20
            self.height = 80
            self.rotated = False

        elif piece == 'o':
            self.color = (255, 253, 56)
            self.width = 40
            self.height = 40

        elif piece == 't':
            self.color = (169, 38, 251)
            self.width = 20
            self.height = 60
            self.y1 = 20
            self.x1 = 120
            self.width1 = 20
            self.height1 = 20
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

    def draw(self, screen):
        if self.piece == 'i' or self.piece == 'o':
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x1, self.y1, self.width1, self.height1))

    def rotate(self):
        if self.piece == 'i':
            if self.x >= 240 - self.height + 20 or self.x <= 20 - self.height + 20:
                pass
            else:
                self.width, self.height = self.height, self.width
                if self.rotated:
                    self.x += 20
                    self.rotated = False
                else:
                    self.x -= 20
                    self.rotated = True
        elif self.piece == 'o':
            pass
        elif self.piece == 't':
            if self.x >= 240 - self.width or self.x >= 240 - self.width1:
                pass
            else:
                self.width, self.height = self.height, self.width
                if self.rotate_amount % 4 == 0:
                    self.x -= 20
                    self.x1 -= 20
                elif self.rotate_amount % 4 == 1:
                    self.x += 20
                    self.x1 -= 20
                elif self.rotate_amount % 4 == 2:
                    self.x -= 20
                    self.y1 -= 20
                    self.y += 20
                    self.x1 += 20
                elif self.rotate_amount % 4 == 3:
                    self.y1 += 20
                    self.y -= 20
                    self.x += 20
                    self.x1 += 20

                self.rotate_amount += 1

        elif self.piece == 'z':
            if self.x >= 240 - self.height or self.x1 >= 240 - self.height1:
                pass
            else:
                self.width, self.height = self.height, self.width
                self.width1, self.height1 = self.height1, self.width1
                if self.rotated:
                    self.x1 -= 20
                    self.x += 20
                    self.rotated = False
                else:
                    self.x1 += 20
                    self.x -= 20
                    self.rotated = True

        elif self.piece == 's':
            if self.x >= 240 - self.height or self.x1 >= 240 - self.height1:
                pass
            else:
                self.width, self.height = self.height, self.width
                self.width1, self.height1 = self.height1, self.width1
                if self.rotated:
                    self.x1 += 20
                    self.x -= 20
                    self.rotated = False
                else:
                    self.x1 -= 20
                    self.x += 20
                    self.rotated = True

        elif self.piece == 'j':
            if self.x > 240 - self.height or self.x1 > 240 - self.height1:
                pass
            # elif 20 + self.height > self.x:
            #    pass
            else:
                self.width, self.height = self.height, self.width
                self.width1, self.height1 = self.height1, self.width1
                if self.rotate_amount % 4 == 0:
                    self.y1 += 20
                    self.x -= 20
                elif self.rotate_amount % 4 == 1:
                    self.y1 += 20
                    self.x1 -= 20
                    self.x += 40
                elif self.rotate_amount % 4 == 2:
                    self.y1 -= 40
                    self.y += 20
                    self.x1 -= 20
                    self.x -= 40
                elif self.rotate_amount % 4 == 3:
                    self.x += 20
                    self.x1 += 40
                    self.y -= 20

                self.rotate_amount += 1

        elif self.piece == 'l':
            if self.x > 240 - self.height or self.x1 > 240 - self.height1:
                pass
            # elif 20 + self.height > self.x:
            #    pass
            else:
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
