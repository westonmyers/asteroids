from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        self.radius = radius
        super().__init__(x, y, radius)
        
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)
        
        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius, 2)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position
        self.x = self.position.x
        self.y = self.position.y