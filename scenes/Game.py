import pygame
import settings
from components import Hero, Bullets, Enemy, Database, blit_text
from random import randint


score = 0
kill = 0
is_winner = None


def load_statistics_to_database(name, kill, score):
    try:
        with Database() as db:
            db.execute("INSERT INTO player (name, kill, score) VALUES (?, ?, ?)", (name, kill, score))
    except Exception as e:
        print(f"Error loading statistics to database: {e}")


def spawn_enemy(group: pygame.sprite.Group, list_enemy) -> Enemy:
    index = randint(0, 2)
    x = randint(16, settings.WINDOW_W - 16)
    speed = randint(1, 4)
    if index == 0:
        score = randint(100, 120)
    if index == 1:
        score = randint(150, 170)
    if index == 2:
        score = randint(200, 210)
    return Enemy(speed=speed, score=score, surf=list_enemy[index], x=x, group=group)


def shoot(speed, group, *args):
    if len(group)<=settings.BULLET_COUNT:
        return Bullets(speed, group, args[0])


def surface_init() -> list:
    surf_player = [
        pygame.image.load('resources/img/Player ship/0.png').convert_alpha(),
        pygame.image.load('resources/img/Player ship/2.png').convert_alpha(),
        pygame.image.load('resources/img/Player ship/1.png').convert_alpha(),
        ]
    surf_player = [pygame.transform.
            scale(img, (img.get_width() * settings.SCALE_HERO, 
                        img.get_height() * settings.SCALE_HERO)) 
            for img in surf_player]
    
    surf_alan = [pygame.image.load(f'resources/img/Enemies/Alan/{i}.png')
                .convert_alpha() for i in range(6)]
    surf_alan = [pygame.transform.
                 scale(img, (img.get_width() * settings.SCALE_ENEMY, 
                             img.get_height() * settings.SCALE_ENEMY))
                 for img in surf_alan]
    surf_Bon = [pygame.image.load(f'resources/img/Enemies/Bon_Bon/{i}.png')
            .convert_alpha() for i in range(4)]
    surf_Bon = [pygame.transform.
                 scale(img, (img.get_width() * settings.SCALE_ENEMY, 
                             img.get_height() * settings.SCALE_ENEMY))
                 for img in surf_Bon]
    surf_Lips = [pygame.image.load(f'resources/img/Enemies/Lips/{i}.png')
                .convert_alpha() for i in range(5)]
    surf_Lips = [pygame.transform.
                scale(img, (img.get_width() * settings.SCALE_ENEMY, 
                            img.get_height() * settings.SCALE_ENEMY))
                for img in surf_Lips]
    surf_enemy = [surf_alan, surf_Bon, surf_Lips]
    return [surf_player, surf_enemy]


def collider_hit_player(group_enemy: pygame.sprite.Group, player: Hero):
    global is_winner
    for item in group_enemy:
        if player.rect.collidepoint(item.rect.center):
            is_winner = False


def colider_hit_enemy(group_enemy: pygame.sprite.Group, group_bullets: pygame.sprite.Group):
    global score, kill, is_winner
    for enemy in group_enemy:
        if enemy.rect.collidelistall(list(group_bullets)):
            dead_enemy = enemy
            break
    for bullet in group_bullets:
        if bullet.rect.collidelistall(list(group_enemy)):
            bullet.kill()
            score += dead_enemy.score
            kill += 1
            if kill == settings.TOTAL_KILL:
                is_winner = True
            dead_enemy.kill()
            break


def game(nickname: str, display: pygame.Surface):
    global score, kill, is_winner
    surf_player, surf_enemy = surface_init()
    player = Hero(nickname=nickname, speed=7, surf=surf_player)
    score_text = settings.FONT_NORMAL.render("Очки: 0", 1, settings.YELLOW)
    count_kill_text = settings.FONT_NORMAL.render(f"Враги: 0/{settings.TOTAL_KILL}", 1, settings.YELLOW)
    pos_score_text = score_text.get_rect(x=0, y=0)
    pos_count_kill_text = count_kill_text.get_rect(x=0, y=20)
    enemy_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    pygame.time.set_timer(pygame.USEREVENT, 2000)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.USEREVENT:
                spawn_enemy(enemy_group, surf_enemy)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot(settings.BULLET_SPEED, bullet_group, player.rect.center)
        press_btn = pygame.key.get_pressed()
        if press_btn[pygame.K_LEFT]:
            player.move(-1, 0)
        if press_btn[pygame.K_RIGHT]:
            player.move(1, 0)
        if press_btn[pygame.K_UP]:
            player.move(0, -1)
        if press_btn[pygame.K_DOWN]:
            player.move(0, 1)
        
        score_text = settings.FONT_NORMAL.render(f"Очки: {score}", 1, settings.YELLOW)
        count_kill_text = settings.FONT_NORMAL.render(f"Враги: {kill}/{settings.TOTAL_KILL}", 1, settings.YELLOW)
        
        collider_hit_player(enemy_group, player)
        colider_hit_enemy(enemy_group, bullet_group)
        
        if is_winner == False:
            return False
        
        if is_winner == True:
            load_statistics_to_database(nickname, kill, score)
            return True
            
        enemy_group.update()
        bullet_group.update()
        
        display.blit(settings.BACKGROUND, (0, 0))
        
        enemy_group.draw(display)
        bullet_group.draw(display)
        
        display.blit(player.image, player.rect)
        display.blit(score_text, pos_score_text)
        display.blit(count_kill_text, pos_count_kill_text)
        
        pygame.display.update()
        settings.clock.tick(settings.FPS)
        