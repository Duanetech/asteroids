from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rangle = random.uniform(20,50)
        new_vec1 =self.velocity.rotate(rangle)
        new_vec2 = self.velocity.rotate(-rangle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x,self.position.y,new_rad)
        asteroid2 = Asteroid(self.position.x,self.position.y,new_rad)
        asteroid1.velocity = new_vec1 * 1.2
        asteroid2.velocity = new_vec2
        

