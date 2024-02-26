import pygame
import settings


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed: int, score: int, surf, x, group, health: int = 1):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.score = score
        self.health = health
        self.surf = surf
        self.image = surf[0]
        self.rect = self.image.get_rect(center=(x, 0))
        self.count_state = len(surf)
        self.index_state = 0
        self.curr_state = 0
        self.add(group)
    
    def update(self):
        if self.rect.bottom < settings.WINDOW_H:
            self.rect.bottom += self.speed
            self.image = self.surf[self.curr_state]
            if self.index_state == 8:
                self.curr_state += 1
                self.index_state = 0
            self.index_state += 1
            if self.curr_state == self.count_state:
                self.curr_state = 0
        else:
            self.kill()
        
    
    
