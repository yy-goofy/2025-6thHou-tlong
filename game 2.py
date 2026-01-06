import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bloxs Blast")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 24)

# Grid settings
GRID_SIZE = 10
CELL = 45
GRID_OFFSET_X = 50
GRID_OFFSET_Y = 50

# Colors
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GREEN = (80, 220, 120)
RED = (255, 60, 60)
YELLOW = (240, 220, 80)
PURPLE = (170, 50, 200)
CYAN = (80, 240, 240)
COLORS = [BLUE, GREEN, RED, YELLOW, PURPLE, CYAN]

# ----- GAME STATE -----

grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Shape library
SHAPES = [
    [(0, 0)],  # 1 block
    [(0, 0), (1, 0)],  # 2 block line
    [(0, 0), (0, 1)],  # vertical 2
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # square
    [(0, 0), (1, 0), (2, 0)],  # line 3
    [(0, 0), (0, 1), (0, 2)],  # vertical 3
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # line 4
    [(0, 0), (0, 1), (1, 1)],  # L small
    [(0, 0), (1, 0), (1, 1)],  # reverse L
]


def generate_shape():
    blocks = SHAPES[random.randrange(len(SHAPES))]
    color = random.choice(COLORS)
    return {"blocks": blocks, "color": color, "x": 350, "y": 550, "grab": False}


pieces = [generate_shape() for _ in range(3)]


# ----- FUNCTIONS -----

def draw_grid():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            rect = pygame.Rect(
                GRID_OFFSET_X + c * CELL,
                GRID_OFFSET_Y + r * CELL,
                CELL, CELL
            )
            pygame.draw.rect(screen, GRAY, rect, 1)
            if grid[r][c] != 0:
                pygame.draw.rect(screen, grid[r][c], rect.inflate(-4, -4))


def draw_piece(piece):
    for (bx, by) in piece["blocks"]:
        px = piece["x"] + bx * CELL
        py = piece["y"] + by * CELL
        pygame.draw.rect(screen, piece["color"],
                         (px, py, CELL, CELL))


def can_place(piece, grid_x, grid_y):
    for (bx, by) in piece["blocks"]:
        r = grid_y + by
        c = grid_x + bx
        if r < 0 or r >= GRID_SIZE or c < 0 or c >= GRID_SIZE:
            return False
        if grid[r][c] != 0:
            return False
    return True


def place_piece(piece, grid_x, grid_y):
    for (bx, by) in piece["blocks"]:
        r = grid_y + by
        c = grid_x + bx
        grid[r][c] = piece["color"]


def clear_lines():
    cleared = 0

    # Full rows
    for r in range(GRID_SIZE):
        if all(grid[r][c] != 0 for c in range(GRID_SIZE)):
            for c in range(GRID_SIZE):
                grid[r][c] = 0
            cleared += 1

    # Full columns
    for c in range(GRID_SIZE):
        if all(grid[r][c] != 0 for r in range(GRID_SIZE)):
            for r in range(GRID_SIZE):
                grid[r][c] = 0
            cleared += 1

    return cleared


def any_moves_left():
    for piece in pieces:
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if can_place(piece, c, r):
                    return True
    return False


# ----- MAIN LOOP -----

score = 0
dragging_piece = None
offset_x = 0
offset_y = 0

running = True
while running:
    screen.fill(BLACK)
    draw_grid()

    # Draw pieces
    for piece in pieces:
        draw_piece(piece)

    # Score
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (400, 20))

    # Game Over
    if not any_moves_left():
        over_text = FONT.render("GAME OVER — No more moves!", True, RED)
        screen.blit(over_text, (120, 650))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Grab piece
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            for piece in pieces:
                for (bx, by) in piece["blocks"]:
                    px = piece["x"] + bx * CELL
                    py = piece["y"] + by * CELL
                    if pygame.Rect(px, py, CELL, CELL).collidepoint(mx, my):
                        dragging_piece = piece
                        offset_x = mx - piece["x"]
                        offset_y = my - piece["y"]
                        break

        # Drag piece
        if event.type == pygame.MOUSEMOTION and dragging_piece:
            mx, my = event.pos
            dragging_piece["x"] = mx - offset_x
            dragging_piece["y"] = my - offset_y

        # Drop piece
        if event.type == pygame.MOUSEBUTTONUP and dragging_piece:
            mx, my = event.pos

            # convert drop pos to grid
            grid_x = (mx - GRID_OFFSET_X) // CELL
            grid_y = (my - GRID_OFFSET_Y) // CELL

            if can_place(dragging_piece, grid_x, grid_y):
                place_piece(dragging_piece, grid_x, grid_y)
                score += 10
                pieces[pieces.index(dragging_piece)] = generate_shape()
                score += clear_lines() * 100

            dragging_piece = None

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
