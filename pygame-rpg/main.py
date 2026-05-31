import pygame
import math

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ENEMY_HEALTH_BAR_OFFSET = 15

# SETUP
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

# UTILITY
def distance(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def draw_health_bar(screen, x, y, current, maximum, width=100, height=10):
    ratio = max(0, min(current / maximum, 1))

    # background (red)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

    # foreground (green)
    pygame.draw.rect(screen, (0, 255, 0), (x, y, width * ratio, height))

# ---------------- PLAYER CLASS ----------------
class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 200
        self.size = 50
        self.attack_range = 60
        self.health = 10
        self.max_health = 10

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
            enemy.take_damage(1)
            
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
        self.max_health = 3
        self.health = 3
        self.speed = 100
        self.attack_range = 40
        self.attack_cooldown = 1.0   # seconds
        self.attack_timer = 0
        self.alive = True

    def follow(self, player, dt):
        if not self.alive:
            return
        
        if player.x < self.x:
            self.x -= self.speed * dt
        if player.x > self.x:
            self.x += self.speed * dt
        if player.y < self.y:
                self.y -= self.speed * dt
        if player.y > self.y:
                self.y += self.speed * dt

    def attack(self, player, dt): # Enemy damages player
        if not self.alive:
            return

        self.attack_timer -= dt

        dist = distance(self, player)

        if dist < self.attack_range and self.attack_timer <= 0:
            player.health -= 1
            print("Player hit! HP:", player.health)

            self.attack_timer = self.attack_cooldown

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.size, self.size))
        
    def take_damage(self, amount):
        if not self.alive:
            return

        self.health = max(0, self.health - amount)

        print("Hit enemy! HP:", self.health)

        if self.health <= 0:
            self.health = 0
            self.alive = False

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
            if event.key == pygame.K_SPACE:
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
    draw_health_bar(screen, 20, 20, player.health, player.max_health)

    enemy.draw(screen)
    if enemy.alive:
        draw_health_bar(
            screen,
            enemy.x,
            enemy.y - ENEMY_HEALTH_BAR_OFFSET,
            enemy.health,
            enemy.max_health
            )

    pygame.display.flip()

pygame.quit()
