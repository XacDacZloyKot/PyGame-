from components import Database, blit_text
import pygame
import settings


def get_statistick_player(display: pygame.Surface, is_winner: bool = False):
    fonts = settings.FONT_LARGE
    text_title = 'Ты выиграл!!!\nЛучшие игроки' if is_winner else 'Ты проиграл :(\nЛучшие игроки'
    winner_title = fonts.render('Победители\t\t\t\t\t\t' + 'Очки', 1, settings.WHITE)
    pos_text_winner_title =  winner_title.get_rect(center=(settings.WINDOW_W//2, settings.WINDOW_H//2 - 200))
    winner = list()
    winner_pos = list()
    
    with Database() as db:
        sql = "SELECT * FROM player ORDER BY score DESC LIMIT 5"
        db.execute(sql)
        top_players = db.fetch_all()
        
    count_player = 0
    for item in top_players:
        winner.append(fonts.render(str(item[0]) + '          ' + str(item[2]), 1, settings.WHITE))
        winner_pos.append(winner[-1].get_rect(center=(settings.WINDOW_W//2, settings.WINDOW_H//2 - 90 + 90 * count_player)))
        count_player += 1
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
        display.blit(settings.BACKGROUND, (0, 0))
        display.blit(winner_title, pos_text_winner_title)
        blit_text(display, text_title, (450, 0), fonts)
        for index in range(len(winner)):
            display.blit(winner[index], winner_pos[index])
        settings.clock.tick(settings.FPS)
        pygame.display.update()