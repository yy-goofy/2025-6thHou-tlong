"""
1v1 Snake Game (Pygame)
Controls:
  Player 1: W A S D
  Player 2: Arrow keys
  R to restart
  Esc or window close to quit
"""

import pygame
import random
import sys

# --- Config ---
CELL_SIZE = 20
GRID_WIDTH = 32   # number of cells horizontally
GRID_HEIGHT = 24  # number of cells vertically
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10  # game speed (increase for faster)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
P1_COLOR = (50, 200, 50)     # green
P2_COLOR = (200, 50, 50)     # red
FOOD_COLOR = (255, 200, 0)   # yellow
GRID_COLOR = (40, 40, 40)
SCORE_COLOR = (200, 200, 200)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# --- Helper functions ---
def place_food(exclude_positions):
    """Place food at a random grid cell not in exclude_positions."""
    while True:
        x = random.randrange(0, GRID_WIDTH)
        y = random.randrange(0, GRID_HEIGHT)
        if (x, y) not in exclude_positions:
            return (x, y)

def rect_from_cell(cell):
    """Return a pygame.Rect for a given cell (x, y)."""
    x, y = cell
    return pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

# --- Game classes ---
class Snake:
    def __init__(self, body, direction, color, name="Player"):
        self.body = body[:]  # list of (x, y) tuples, head = body[0]
        self.direction = direction
        self.next_direction = direction
        self.grow_pending = 0
        self.color = color
        self.alive = True
        self.name = name

    def head(self):
        return self.body[0]

    def set_direction(self, d):
        # Prevent reversing directly
        if (d[0] == -self.direction[0] and d[1] == -self.direction[1]) and len(self.body) > 1:
            return
        self.next_direction = d

    def update(self):
        if not self.alive:
            return
        self.direction = self.next_direction
        hx, hy = self.head()
        nx, ny = hx + self.direction[0], hy + self.direction[1]
        new_head = (nx, ny)
        self.body.insert(0, new_head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self, amount=1):
        self.grow_pending += amount

    def collides_with_cell(self, cell):
        return cell in self.body

    def collides_with_self(self):
        return self.head() in self.body[1:]

    def collides_with_wall(self):
        x, y = self.head()
        return not (0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT)

    def kill(self):
        self.alive = False

# --- Game initialization ---
def new_game():
    # Player 1 starts left middle, moving right
    p1_start = [(5, GRID_HEIGHT//2), (4, GRID_HEIGHT//2), (3, GRID_HEIGHT//2)]
    p1 = Snake(p1_start, RIGHT, P1_COLOR, "Player 1")

    # Player 2 starts right middle, moving left
    p2_start = [(GRID_WIDTH - 6, GRID_HEIGHT//2), (GRID_WIDTH - 5, GRID_HEIGHT//2), (GRID_WIDTH - 4, GRID_HEIGHT//2)]
    p2 = Snake(p2_start, LEFT, P2_COLOR, "Player 2")

    exclude = set(p1.body + p2.body)
    food = place_food(exclude)

    return p1, p2, food

# --- Main ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("1v1 Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    big_font = pygame.font.SysFont(None, 48)

    p1, p2, food = new_game()
    running = True
    paused = False
    winner_text = None

    while running:
        # --- Input ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
                if event.key == pygame.K_r:
                    p1, p2, food = new_game()
                    winner_text = None
                    paused = False
                # Player 1 controls
                if event.key == pygame.K_w:
                    p1.set_direction(UP)
                elif event.key == pygame.K_s:
                    p1.set_direction(DOWN)
                elif event.key == pygame.K_a:
                    p1.set_direction(LEFT)
                elif event.key == pygame.K_d:
                    p1.set_direction(RIGHT)
                # Player 2 controls
                elif event.key == pygame.K_UP:
                    p2.set_direction(UP)
                elif event.key == pygame.K_DOWN:
                    p2.set_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    p2.set_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    p2.set_direction(RIGHT)

        if not running:
            break

        if not paused and (p1.alive or p2.alive):
            # --- Update game state ---
            p1.update()
            p2.update()

            # Check wall collisions
            if p1.collides_with_wall():
                p1.kill()
            if p2.collides_with_wall():
                p2.kill()

            # Build set of occupied cells for collision checks
            p1_body_set = set(p1.body)
            p2_body_set = set(p2.body)

            # Check self-collisions
            if p1.collides_with_self():
                p1.kill()
            if p2.collides_with_self():
                p2.kill()

            # Check head-to-body collisions (hitboxes)
            # If P1's head overlaps any cell in P2's body -> P1 dies
            if p1.head() in p2_body_set:
                p1.kill()
            # If P2's head overlaps any cell in P1's body -> P2 dies
            if p2.head() in p1_body_set:
                p2.kill()

            # Check head-to-head collision: both die
            if p1.head() == p2.head():
                p1.kill()
                p2.kill()

            # Food consumption: if a head lands on food, grow and respawn food
            # Note: If both land on the same food simultaneously, both grow and new food spawns
            consumed = False
            exclude = set(p1.body + p2.body)
            if p1.alive and p1.head() == food:
                p1.grow(2)
                consumed = True
            if p2.alive and p2.head() == food:
                p2.grow(2)
                consumed = True
            if consumed:
                food = place_food(exclude)

            # Determine if game ended
            if not p1.alive and not p2.alive:
                winner_text = "Tie!"
                paused = True
            elif not p1.alive:
                winner_text = "Player 2 wins!"
                paused = True
            elif not p2.alive:
                winner_text = "Player 1 wins!"
                paused = True

        # --- Draw ---
        screen.fill(BLACK)

        # Draw grid (subtle)
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

        # Draw food
        pygame.draw.rect(screen, FOOD_COLOR, rect_from_cell(food))

        # Draw snakes as rectangles with small inner spacing to create hitbox feel
        for idx, seg in enumerate(p1.body):
            r = rect_from_cell(seg).inflate(-2, -2)
            pygame.draw.rect(screen, p1.color, r)
            # head highlight
            if idx == 0:
                pygame.draw.rect(screen, WHITE, r, 2)
        for idx, seg in enumerate(p2.body):
            r = rect_from_cell(seg).inflate(-2, -2)
            pygame.draw.rect(screen, p2.color, r)
            if idx == 0:
                pygame.draw.rect(screen, WHITE, r, 2)

        # Draw scores (length)
        p1_score_text = font.render(f"Player 1: {len(p1.body)}", True, SCORE_COLOR)
        p2_score_text = font.render(f"Player 2: {len(p2.body)}", True, SCORE_COLOR)
        screen.blit(p1_score_text, (8, 8))
        screen.blit(p2_score_text, (SCREEN_WIDTH - p2_score_text.get_width() - 8, 8))

        # Draw controls reminder
        hint = font.render("WASD / Arrows. R to restart.", True, SCORE_COLOR)
        screen.blit(hint, ((SCREEN_WIDTH - hint.get_width())//2, 8))

        # Winner message
        if winner_text:
            wrap = big_font.render(winner_text, True, SCORE_COLOR)
            screen.blit(wrap, ((SCREEN_WIDTH - wrap.get_width())//2, (SCREEN_HEIGHT - wrap.get_height())//2))

            sub = font.render("Press R to play again", True, SCORE_COLOR)
            screen.blit(sub, ((SCREEN_WIDTH - sub.get_width())//2, (SCREEN_HEIGHT - wrap.get_height())//2 + 60))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
