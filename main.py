import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Asteroid.containers = (asteroid_group, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
  
        # Iterate over all asteroids in the game
        for asteroid in asteroid_group:
        # Check if `asteroid` collides with the player
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")
        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()