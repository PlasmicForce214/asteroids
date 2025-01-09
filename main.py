# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # Delta Time
    dt = 0
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroid_group)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field= AsteroidField()

    # Start Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # player.update(dt)
        for obj in updatable:
            obj.update(dt)

        for obj in asteroid_group:
            if obj.collision(player):
                sys.exit()
            for bullet in shots:
                if bullet.collision(obj):
                    bullet.kill()
                    obj.split()

        screen.fill("black")
        
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
    
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
