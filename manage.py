import pygame
import settings 
from scenes import game, get_statistick_player, about, set_nickname

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

screen = pygame.display.set_mode((settings.WINDOW_W, settings.WINDOW_H))
screen.fill(settings.WHITE)
pygame.display.set_caption("Игра на pygame")

if __name__=='__main__':
    player_name = set_nickname(screen)
    about(screen)
    winner = game(player_name, screen)
    get_statistick_player(screen, winner)
    