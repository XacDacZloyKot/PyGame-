import pygame
import settings

class Hero(pygame.sprite.Sprite):
    def __init__(self, nickname, speed, surf):
        pygame.sprite.Sprite.__init__(self)
        self.nickname = nickname
        self.speed = speed
        self.surf = surf
        self.image = surf[1]
        self.rect = self.image.get_rect(center=(settings.WINDOW_W//2, settings.WINDOW_H//2))
    
    def move(self, side_move_horizontal, side_move_vertical):
        if self.rect.left > 0:
            if side_move_horizontal == -1:
                self.image = self.surf[0]
                self.rect.x += self.speed * side_move_horizontal
        if self.rect.right < settings.WINDOW_W: 
            if side_move_horizontal == 1:
                self.image = self.surf[2]
                self.rect.x += self.speed * side_move_horizontal
        if self.rect.bottom < settings.WINDOW_H:
            if side_move_vertical == 1:
                self.image = self.surf[1]
                self.rect.y += self.speed * side_move_vertical
        if self.rect.top > 0:
            if side_move_vertical == -1:
                self.image = self.surf[1]
                self.rect.y += self.speed * side_move_vertical