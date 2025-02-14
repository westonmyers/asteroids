import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    fps = 60

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = updatable, drawable
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game Over!")
                exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.split()
                    shot.kill()
                    break
        screen.fill(color=(0, 0, 0))
        drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(fps) / 1000

if __name__ == "__main__":
    main()