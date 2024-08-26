import pygame
import sys
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, LIGHT_GREY
from src.entities.ball import Ball
from src.entities.player import Player
from src.entities.opponent import Opponent

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")

        # Create game objects
        self.ball = Ball(SCREEN_WIDTH / 2 - 15, SCREEN_HEIGHT / 2 - 15, 30, 30, 7, 7)
        self.player = Player(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - 70, 10, 140)
        self.opponent = Opponent(10, SCREEN_HEIGHT / 2 - 70, 10, 140, self.ball)

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
        pygame.draw.aaline(self.screen, LIGHT_GREY, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))
        self.ball.draw(self.screen)
        self.player.draw(self.screen)
        self.opponent.draw(self.screen)
