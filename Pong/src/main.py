import pygame, sys

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
BORDER_OFFSET = 5
BALL_SIZE = 30
BALL_SPEED_X = 7
BALL_SPEED_Y = 7
PAD_HEIGHT = 140
PAD_WIDTH = 10

player_speed = 0
opponent_speed = 7

BG_COLOR = pygame.Color("gray1")
LIGHT_GREY = (200,200,200)

run = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Game Objects
ball = pygame.Rect(SCREEN_WIDTH/2 - BALL_SIZE/2, SCREEN_HEIGHT/2 - BALL_SIZE/2, BALL_SIZE, BALL_SIZE)
player = pygame.Rect(SCREEN_WIDTH - PAD_WIDTH * 2, SCREEN_HEIGHT/2 - PAD_HEIGHT/2, PAD_WIDTH, PAD_HEIGHT)
opponent = pygame.Rect(PAD_WIDTH, SCREEN_HEIGHT/2 - PAD_HEIGHT/2, PAD_WIDTH, PAD_HEIGHT)

ball_speed = pygame.Vector2(BALL_SPEED_X, BALL_SPEED_Y)

def ball_animation(ball, ball_speed):
    ball.x += ball_speed.x
    ball.y += ball_speed.y

    # Bounce off top and bottom edges
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed.y *= -1

    # Bounce off left and right edges
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed.x *= -1

    # Bounce off paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed.x *= -1

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = BORDER_OFFSET
    if player.bottom > SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT - BORDER_OFFSET

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = BORDER_OFFSET
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT - BORDER_OFFSET

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed +=7

    ball_animation(ball, ball_speed)
    player_animation()
    opponent_animation()

    #Visuals
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, LIGHT_GREY, player)
    pygame.draw.rect(screen, LIGHT_GREY, opponent)
    pygame.draw.ellipse(screen, LIGHT_GREY, ball)
    pygame.draw.aaline(screen, LIGHT_GREY, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    pygame.display.flip()
    clock.tick(60)
