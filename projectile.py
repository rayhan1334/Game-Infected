import pygame

class Projectile:

    def __init__(self, x, y, facing):

        self.speed = 8 * facing
        self.radius = 5

        self.rect = pygame.Rect(x, y, 10, 10)

    def move(self):

        self.rect.x += self.speed

    def draw(self, win):

        pygame.draw.rect(win, (255, 255, 0), self.rect)
