from typing import Any
import pygame

class Bullets(pygame.sprite.Sprite):
    def __init__(self, speed, group, center):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.image = pygame.image.load('resources/img/Projectiles/bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center=(center[0], center[1]-10))
        self.add(group)
        
    def update(self) :
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.kill()