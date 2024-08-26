import pygame
import sys

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
BORDER_OFFSET = 5
BALL_SIZE = 30
BALL_SPEED_X = 7
BALL_SPEED_Y = 7
PAD_HEIGHT = 140
PAD_WIDTH = 10
OPPONENT_SPEED = 7
BG_COLOR = pygame.Color("gray1")
LIGHT_GREY = (200, 200, 200)

# Game Classes
class Ball:
    def __init__(self, x, y, width, height, speed_x, speed_y):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = pygame.Vector2(speed_x, speed_y)

    def animate(self, player, opponent):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

        # Bounce off top and bottom edges
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed.y *= -1

        # Bounce off left and right edges
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed.x *= -1

        # Bounce off paddles
        if self.rect.colliderect(player.rect) or self.rect.colliderect(opponent.rect):
            self.speed.x *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, LIGHT_GREY, self.rect)


class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, LIGHT_GREY, self.rect)


class Player(Paddle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, speed=0)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.speed += 7
            if event.key == pygame.K_UP:
                self.speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.speed -= 7
            if event.key == pygame.K_UP:
                self.speed += 7

    def update(self):
        self.rect.y += self.speed
        if self.rect.top <= 0:
            self.rect.top = BORDER_OFFSET
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT - BORDER_OFFSET


class Opponent(Paddle):
    def __init__(self, x, y, width, height, ball):
        super().__init__(x, y, width, height, speed=OPPONENT_SPEED)
        self.ball = ball

    def update(self):
        if self.rect.top < self.ball.rect.y:
            self.rect.top += self.speed
        if self.rect.bottom > self.ball.rect.y:
            self.rect.bottom -= self.speed

        if self.rect.top <= 0:
            self.rect.top = BORDER_OFFSET
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT - BORDER_OFFSET


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")

        # Create game objects
        self.ball = Ball(SCREEN_WIDTH/2 - BALL_SIZE/2, SCREEN_HEIGHT/2 - BALL_SIZE/2, BALL_SIZE, BALL_SIZE, BALL_SPEED_X, BALL_SPEED_Y)
        self.player = Player(SCREEN_WIDTH - PAD_WIDTH * 2, SCREEN_HEIGHT/2 - PAD_HEIGHT/2, PAD_WIDTH, PAD_HEIGHT)
        self.opponent = Opponent(PAD_WIDTH, SCREEN_HEIGHT/2 - PAD_HEIGHT/2, PAD_WIDTH, PAD_HEIGHT, self.ball)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.player.handle_input(event)

            # Update game objects
            self.ball.animate(self.player, self.opponent)
            self.player.update()
            self.opponent.update()

            # Draw everything
            self.screen.fill(BG_COLOR)
            self.draw_elements()
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)

    def draw_elements(self):
        pygame.draw.aaline(self.screen, LIGHT_GREY, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))
        self.ball.draw(self.screen)
        self.player.draw(self.screen)
        self.opponent.draw(self.screen)


if __name__ == '__main__':
    game = Game()
    game.run()
