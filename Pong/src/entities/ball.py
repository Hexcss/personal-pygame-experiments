import pygame
from src.settings import LIGHT_GREY, SCREEN_HEIGHT, SCREEN_WIDTH

class Ball:
    def __init__(self, x, y, width, height, speed_x, speed_y):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = pygame.Vector2(speed_x, speed_y)

    def animate(self, player, opponent):
        self.rect.x += int(self.speed.x)
        self.rect.y += int(self.speed.y)

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
