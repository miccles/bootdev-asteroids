import pygame
from circleshape import CircleShape



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

