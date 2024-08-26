import pygame
from src.entities.paddle import Paddle
from src.settings import BORDER_OFFSET, SCREEN_HEIGHT

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
