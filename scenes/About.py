import pygame
import settings
from components import InputBox, blit_text


def about(display: pygame.Surface) -> str:
    fonts = settings.FONT_NORMAL
    text = f"Вы попали в игру по охоте на пришельцев.\nВаша задача добыть с них ценные ресурсы и выжить.\nПопробуй победить {settings.TOTAL_KILL} монстров\n"\
        "Для движения используй стрелочки\nДля стрельбы используй пробел\nНажми enter для продолжения"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 
        display.blit(settings.BACKGROUND, (0, 0))
        blit_text(display, text, (settings.WINDOW_W//2-300, settings.WINDOW_H//2-100), fonts)
        settings.clock.tick(settings.FPS)
        pygame.display.update()
        