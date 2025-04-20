import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 4
PADDLE_SPEED = 6
BRICK_ROWS, BRICK_COLS = 5, 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bricks Breaker")

# Paddle
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 30, 120, 10)

# Ball
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2, 15, 15)
ball_dx, ball_dy = BALL_SPEED, -BALL_SPEED

# Bricks
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT, BRICK_WIDTH - 5, BRICK_HEIGHT - 5)
        bricks.append(brick)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-PADDLE_SPEED, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(PADDLE_SPEED, 0)

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # Brick collision
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy = -ball_dy
            break

    # Lose condition
    if ball.bottom >= HEIGHT:
        running = False

    # Draw elements
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

