import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
LIGHT_GRAY = (180, 180, 180)
ORANGE = (255, 165, 0)
PURPLE = (160, 32, 240)

# Font
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

# Clock
clock = pygame.time.Clock()

# Road lines for menu animation
menu_lines = [i for i in range(0, HEIGHT, 40)]
line_speed = 5

# Default car settings
car_color = BLUE
car_shape = "rectangle"  # Options: rectangle, triangle, circle

# --- Helper Functions ---
def draw_text(text, color, x, y, font_used=font):
    screen.blit(font_used.render(text, True, color), (x, y))

def button(text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect = pygame.Rect(x, y, w, h)

    if rect.collidepoint(mouse):
        pygame.draw.rect(screen, active_color, rect)
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, rect)

    draw_text(text, BLACK, x + w // 4, y + 10)

def animate_menu_lines():
    global menu_lines
    for i in range(len(menu_lines)):
        menu_lines[i] += line_speed
        if menu_lines[i] > HEIGHT:
            menu_lines[i] = -20
        pygame.draw.rect(screen, WHITE, (WIDTH//2 - 2, menu_lines[i], 4, 20))

# --- Menus ---
def main_menu():
    menu = True
    while menu:
        screen.fill(GRAY)
        animate_menu_lines()
        draw_text("CAR GAME", YELLOW, WIDTH // 2 - 100, HEIGHT // 3, big_font)

        button("PLAY", WIDTH // 2 - 75, HEIGHT // 2, 150, 50, GREEN, LIGHT_GREEN, game_loop)
        button("SETTINGS", WIDTH // 2 - 75, HEIGHT // 2 + 80, 150, 50, LIGHT_GRAY, WHITE, settings_menu)
        button("QUIT", WIDTH // 2 - 75, HEIGHT // 2 + 160, 150, 50, RED, (255, 100, 100), quit_game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        pygame.display.flip()
        clock.tick(60)

def settings_menu():
    global car_color, car_shape
    menu = True
    while menu:
        screen.fill(GRAY)
        animate_menu_lines()
        draw_text("SETTINGS", YELLOW, WIDTH // 2 - 90, HEIGHT // 5, big_font)

        # Color options
        button("BLUE", 50, 250, 100, 50, BLUE, LIGHT_GREEN, lambda: set_car_color(BLUE))
        button("RED", 250, 250, 100, 50, RED, LIGHT_GREEN, lambda: set_car_color(RED))
        button("GREEN", 50, 350, 100, 50, GREEN, LIGHT_GREEN, lambda: set_car_color(GREEN))
        button("PURPLE", 250, 350, 100, 50, PURPLE, LIGHT_GREEN, lambda: set_car_color(PURPLE))
        button("ORANGE", 150, 450, 100, 50, ORANGE, LIGHT_GREEN, lambda: set_car_color(ORANGE))

        # Car shape options
        draw_text("CAR SHAPE:", WHITE, 50, 520)
        button("RECT", 50, 550, 80, 40, LIGHT_GRAY, WHITE, lambda: set_car_shape("rectangle"))
        button("TRIANGLE", 150, 550, 100, 40, LIGHT_GRAY, WHITE, lambda: set_car_shape("triangle"))
        button("CIRCLE", 270, 550, 80, 40, LIGHT_GRAY, WHITE, lambda: set_car_shape("circle"))

        # Back to main menu
        button("BACK", WIDTH // 2 - 75, HEIGHT - 80, 150, 50, LIGHT_GRAY, WHITE, main_menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        pygame.display.flip()
        clock.tick(60)

# --- Settings Functions ---
def set_car_color(color):
    global car_color
    car_color = color

def set_car_shape(shape):
    global car_shape
    car_shape = shape

# --- Game Functions ---
def quit_game():
    pygame.quit()
    sys.exit()

def draw_player_car(x, y):
    if car_shape == "rectangle":
        pygame.draw.rect(screen, car_color, (x, y, 50, 80))
    elif car_shape == "triangle":
        pygame.draw.polygon(screen, car_color, [(x+25, y), (x, y+80), (x+50, y+80)])
    elif car_shape == "circle":
        pygame.draw.ellipse(screen, car_color, (x, y, 50, 80))

def game_loop():
    car_w, car_h = 50, 80
    car_x = WIDTH // 2 - car_w // 2
    car_y = HEIGHT - car_h - 10
    car_speed = 6

    enemy_w, enemy_h = 50, 80
    enemy_x = random.randint(0, WIDTH - enemy_w)
    enemy_y = -enemy_h
    enemy_speed = 5

    score = 0
    running = True
    game_over = False

    while running:
        clock.tick(60)
        screen.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_a] and car_x > 0:
                car_x -= car_speed
            elif keys[pygame.K_d] and car_x < WIDTH - car_w:
                car_x += car_speed

            # Move enemy
            enemy_y += enemy_speed
            if enemy_y > HEIGHT:
                enemy_y = -enemy_h
                enemy_x = random.randint(0, WIDTH - enemy_w)
                score += 1
                enemy_speed += 0.25

            # Draw cars
            draw_player_car(car_x, car_y)
            pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_w, enemy_h))

            # Collision
            player_rect = pygame.Rect(car_x, car_y, car_w, car_h)
            enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_w, enemy_h)
            if player_rect.colliderect(enemy_rect):
                game_over = True

            # Road lines + score
            for i in range(0, HEIGHT, 40):
                pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 2, i, 4, 20))
            draw_text(f"Score: {score}", WHITE, 10, 10)

        else:
            draw_text("GAME OVER", RED, WIDTH // 3 - 20, HEIGHT // 2 - 80, big_font)
            button("RESTART", WIDTH // 2 - 75, HEIGHT // 2, 150, 50, GREEN, LIGHT_GREEN, game_loop)
            button("MENU", WIDTH // 2 - 75, HEIGHT // 2 + 80, 150, 50, YELLOW, (255, 255, 150), main_menu)

        pygame.display.flip()

# --- Start game at main menu ---
main_menu()
enemy_speed = random.randint(20, 50)
