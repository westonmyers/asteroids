import pygame
from circleshape import CircleShape
import random
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.radius = radius
        super().__init__(x, y, radius)
        
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)
        
        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius, 2)
    
    def draw(self, screen):
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius) , self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
        self.x = self.position.x
        self.y = self.position.y

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.x, self.y, radius).velocity = vector1 * 1.2
        Asteroid(self.x, self.y, radius).velocity = vector2 * 1.2