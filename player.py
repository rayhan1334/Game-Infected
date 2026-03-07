import pygame

class Player:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.speed = 5
        self.width = 40
        self.height = 60
        self.facing = 1

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
            self.facing = -1

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
            self.facing = 1

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, win):

        pygame.draw.rect(win, (0, 200, 255), self.rect)
