import pygame
import settings
from components import InputBox

def set_nickname(display: pygame.Surface) -> str:
    nickname = InputBox(settings.WINDOW_W//2-200, settings.WINDOW_H//2-32, 400, 64)
    fonts = settings.FONT_LARGE
    text_surface = fonts.render('Введите свой ник:', 1, settings.PURPLE)
    pos_text = text_surface.get_rect(center=(settings.WINDOW_W//2, settings.WINDOW_H//2 - 100))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return nickname.text
            nickname.handle_event(event=event)
        nickname.update()
        display.blit(settings.BACKGROUND, (0, 0))
        display.blit(text_surface, pos_text)
        nickname.draw(display)
        settings.clock.tick(settings.FPS)
        pygame.display.update()
        