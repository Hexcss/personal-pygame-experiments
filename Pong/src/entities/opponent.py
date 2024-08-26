from src.entities.paddle import Paddle
from src.settings import BORDER_OFFSET, SCREEN_HEIGHT, OPPONENT_SPEED

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
