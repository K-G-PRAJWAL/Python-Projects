# Simple Pong game

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15
BALL_SPEED_X, BALL_SPEED_Y = 7, 7
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Advanced Pong')

# Game objects
paddle1 = pygame.Rect(10, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH - 10, (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect((SCREEN_WIDTH - BALL_SIZE) // 2, (SCREEN_HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)

# Initial ball speed and direction
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
paddle_speed = 7

# Scoring
score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)

# Clock for controlling FPS
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < SCREEN_HEIGHT:
        paddle1.y += paddle_speed

    # Simple AI for paddle2
    if paddle2.centery < ball.centery and paddle2.bottom < SCREEN_HEIGHT:
        paddle2.y += paddle_speed
    if paddle2.centery > ball.centery and paddle2.top > 0:
        paddle2.y -= paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision with top and bottom
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    # Collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Scoring
    if ball.left <= 0:
        score2 += 1
        ball = pygame.Rect((SCREEN_WIDTH - BALL_SIZE) // 2, (SCREEN_HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)
        ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
        ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
    if ball.right >= SCREEN_WIDTH:
        score1 += 1
        ball = pygame.Rect((SCREEN_WIDTH - BALL_SIZE) // 2, (SCREEN_HEIGHT - BALL_SIZE) // 2, BALL_SIZE, BALL_SIZE)
        ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
        ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Display scores
    score_text1 = font.render(str(score1), True, WHITE)
    screen.blit(score_text1, (320, 10))
    score_text2 = font.render(str(score2), True, WHITE)
    screen.blit(score_text2, (420, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
