import pygame
import circleshape
from constants import SHOT_RADIUS

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        # sub-classes must override
        self.position+=dt*self.velocity