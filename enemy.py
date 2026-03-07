import pygame

class Enemy:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.speed = 2

        self.width = 40
        self.height = 60

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, player_x):

        if player_x > self.x:
            self.x += self.speed
        else:
            self.x -= self.speed

        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def draw(self, win):

        pygame.draw.rect(win, (200, 50, 50), self.hitbox)
