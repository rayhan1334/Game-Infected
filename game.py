import pygame
from player import Player
from enemy import Enemy
from projectile import Projectile
from scoreboard import update_score

class Game:

    def __init__(self, username):

        pygame.init()

        self.width = 800
        self.height = 500
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Infected")

        self.username = username

        self.player = Player(400, 300)
        self.enemies = []
        self.bullets = []

        self.score = 0
        self.clock = pygame.time.Clock()

    def spawn_enemy(self):

        enemy = Enemy(0, 300)
        self.enemies.append(enemy)

    def run(self):

        running = True
        spawn_timer = 0

        while running:

            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Projectile(self.player.x, self.player.y, self.player.facing)
                        self.bullets.append(bullet)

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            spawn_timer += 1
            if spawn_timer > 120:
                self.spawn_enemy()
                spawn_timer = 0

            for bullet in self.bullets:
                bullet.move()

            for enemy in self.enemies:
                enemy.move(self.player.x)

            self.check_collisions()

            self.draw()

        update_score(self.username, self.score)
        pygame.quit()

    def check_collisions(self):

        for enemy in self.enemies:
            for bullet in self.bullets:

                if enemy.hitbox.colliderect(bullet.rect):
                    self.score += 10
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    break

    def draw(self):

        self.win.fill((30, 30, 30))

        self.player.draw(self.win)

        for enemy in self.enemies:
            enemy.draw(self.win)

        for bullet in self.bullets:
            bullet.draw(self.win)

        pygame.display.update()
