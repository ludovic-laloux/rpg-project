# IMPORTS(external libraries)
import pygame
import math

# CONSTANTS(game rules)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# SETUP
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

running = True

# VARIABLES(game states)
player_x = 100
player_y = 100
player_size = 50
player_speed = 5

enemy_x = 400
enemy_y = 300
enemy_size = 50
enemy_health = 3
enemy_speed = 2

attack_range = 60

# MAIN LOOP
while running:
    clock.tick(60)

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and enemy_health > 0:
                
                # ATTACK LOGIC(event-based)
                distance = math.sqrt((player_x - enemy_x)**2 + (player_y - enemy_y)**2)

                if distance < attack_range:
                    enemy_health -= 1
                    print("Hit enemy! HP: ", enemy_health)
                else:
                    print("Too far!")

    # UPDATE / ENEMY MOVEMENT
    if enemy_health > 0:
        if player_x < enemy_x:
            enemy_x -= enemy_speed
        elif player_x > enemy_x:
            enemy_x += enemy_speed
        if player_y < enemy_y:
            enemy_y -= enemy_speed
        elif player_y > enemy_y:
            enemy_y += enemy_speed

    # ---------------- INPUT(player movement) ----------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # ---------------- BOUNDARIES ----------------
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - player_size:
        player_x = SCREEN_WIDTH - player_size

    if player_y < 0:
        player_y = 0
    if player_y > SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size

    # ---------------- DRAW ----------------
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))

    if enemy_health > 0:
        pygame.draw.rect(screen, (0, 0, 255), (enemy_x, enemy_y, enemy_size, enemy_size))

    pygame.display.flip()

# SHUTDOWN(cleanup)
pygame.quit()