import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.image.load('face.png')
        self.scaled_image = pygame.transform.scale(self.image, (2 * radius, 2 * radius))

    def draw(self, screen):
        #pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        screen.blit(self.scaled_image, (self.position.x - self.radius, self.position.y - self.radius))

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None, None
        else:
            angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(angle)
            vel2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = vel1
            ast2.velocity = vel2
            return ast1, ast2
