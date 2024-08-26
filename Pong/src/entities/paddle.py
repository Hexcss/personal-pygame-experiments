import pygame
from ..settings import LIGHT_GREY

class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, LIGHT_GREY, self.rect)
