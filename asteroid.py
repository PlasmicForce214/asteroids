import random
import pygame
import circleshape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # sub-classes must override
        self.position+=dt*self.velocity

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            vect1 = self.velocity.rotate(rand_angle)
            vect2 = self.velocity.rotate(-1*rand_angle)
            new_radius = self.radius-ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity=vect1
            asteroid2.velocity=vect2