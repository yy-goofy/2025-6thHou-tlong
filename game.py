import pygame

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

# Load assets (replace with your actual image paths)
car_img = pygame.image.load('car.png')
road_img = pygame.image.load('road.png')

# Player car class (simplified)
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height * 0.8)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # Keep car within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

# Game loop
running = True
clock = pygame.time.Clock()
player_car = PlayerCar()
all_sprites = pygame.sprite.Group(player_car)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_car.update(keys)

    # Drawing
    screen.blit(road_img, (0, 0)) # Draw background
    all_sprites.draw(screen) # Draw all sprites

    pygame.display.flip()
    clock.tick(60) # 60 FPS

pygame.quit()