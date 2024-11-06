# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import * 


def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    keys = pygame.key.get_pressed()
    font = pygame.font.Font(None, 74)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    game_over = False
    while True:
        if not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            screen.fill((0, 0, 0))
            for thing in drawable:
                thing.draw(screen)
            for thing in updatable:
                thing.update(dt)

            # Collision Detection
            for asteroid in asteroids:
                if player.check_collisions(asteroid):
                    game_over = True
            
            if game_over:
                # Render game over message
                game_over_surface = font.render('Game Over!', True, (255, 255, 255))
                exit_surface = font.render('Press E to exit', True, (255, 255, 255))
                game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
                exit_rect = exit_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
                screen.blit(game_over_surface, game_over_rect)
                screen.blit(exit_surface, exit_rect)

        else:
            # Handle game over events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        return
                elif event.type == pygame.QUIT:
                    return

        pygame.display.flip()  # Ensure the display updates regardless of the state
        dt = clock.tick(60) / 1000  # Refresh rate


if __name__ == "__main__":
    main()


