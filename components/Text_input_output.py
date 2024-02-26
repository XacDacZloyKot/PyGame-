import pygame
import settings


def blit_text(surface, text, pos, font, color=pygame.Color('White')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.w = w
        self.rect = pygame.Rect(x, y, w, h)
        self.color = settings.COLOR_INACTIVE
        self.text = text
        self.FONT = pygame.font.Font(settings.PATH_FONT, round(h//1.5))
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
        
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = settings.COLOR_ACTIVE if self.active else settings.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.FONT.render(self.text, True, self.color)


    def update(self):
        width = max(self.w, self.txt_surface.get_width()+10)
        self.rect.w = width
        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))