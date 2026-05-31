import pygame
import math

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# SETUP
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

# UTILITY
def distance(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
# ---------------- PLAYER CLASS ----------------
class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 200
        self.size = 50
        self.attack_range = 60
        self.health = 10

    def move(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed * dt
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * dt
        if keys[pygame.K_UP]:
            self.y -= self.speed * dt
        if keys[pygame.K_DOWN]:
            self.y += self.speed * dt

        # boundaries
        self.x = max(0, min(SCREEN_WIDTH - self.size, self.x))
        self.y = max(0, min(SCREEN_HEIGHT - self.size, self.y))

    def attack(self, enemy):
        dist = distance(self, enemy)

        if dist < self.attack_range:
            enemy.health = max(0, enemy.health - 1)
            print("Hit enemy! HP:", enemy.health)

        else:
            print("Too far!")

    def draw(self,screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))


# ---------------- ENEMY CLASS ----------------
class Enemy:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.size = 50
        self.health = 3
        self.speed = 100
        self.attack_range = 40

    def follow(self, player, dt):
        if self.health > 0:
            if player.x < self.x:
                self.x -= self.speed * dt
            if player.x > self.x:
                self.x += self.speed * dt
            if player.y < self.y:
                self.y -= self.speed * dt
            if player.y > self.y:
                self.y += self.speed * dt

    def attack(self, player, dt): # Enemy damages player
        if self.health <= 0:
            return

        dist = distance(self, player)

        if dist < self.attack_range:
            player.health -= 3 * dt

    def draw(self, screen):
        if self.health > 0:
            pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.size, self.size))


# ---------------- SETUP ----------------
player = Player()
enemy = Enemy()

running = True

# ---------------- MAIN LOOP ----------------
while running:
    dt = clock.tick(60) / 1000

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and enemy.health > 0:
                player.attack(enemy)

    # UPDATE
    player.move(dt)
    enemy.follow(player, dt)
    enemy.attack(player, dt)

    # GAME OVER CHECK
    if player.health <= 0:
        print("Game Over")
        running = False

    # DRAW
    screen.fill((0, 0, 0))

    player.draw(screen)
    enemy.draw(screen)

    pygame.display.flip()

pygame.quit()
