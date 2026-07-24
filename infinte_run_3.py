import pygame as py
import sys
import random as rd
import time
py.init()
screen=py.display.set_mode((600,310))
clock=py.time.Clock()

dino_image = None
cactus_image = None
try:
    dino_image = py.image.load(".\dinosaur.png")
    dino_image = py.transform.scale(dino_image, (100,90))
    cactus_image = py.image.load(".\cactus.png")
    cactus_image = py.transform.scale(cactus_image, (105,110))
except:
    print("이미지 파일을 찾을 수 없습니다! 기본 사각형으로 대체하여 게임을 시작합니다.")

player_rect = py.Rect(100, 220, 50, 50)
obs_rect = py.Rect(800, 215, 40, 50)
obs_speed = 7

is_jumping = False
jump_velocity = 15
gravity = 1
y_velocity = 0
game_over = False

score = 0
last_score_update_time = py.time.get_ticks()
font = py.font.SysFont("arial", 25)

while True:
    current_time = py.time.get_ticks()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE and not is_jumping and not game_over:
                is_jumping = True
                y_velocity = -jump_velocity

            
            if game_over and event.key == py.K_r:
                game_over = False
                player_rect.y = 220
                is_jumping = False
                y_velocity = 0
                obs_rect.x = 800
                obs_rect.x = rd.randint(400,1200)
                score = 0
                last_score_update_time = py.time.get_ticks()


    if not game_over:
        if current_time - last_score_update_time >= 1000:
            score += 1
            last_score_update_time = current_time
        if is_jumping:
            player_rect.y += y_velocity
            y_velocity += gravity

            if player_rect.y >= 220:
                player_rect.y = 220
                is_jumping = False
                y_velocity = 0

    obs_rect.x -= obs_speed

    if obs_rect.x < -40:
        obs_rect.x = rd.randint(400,1200)

    if player_rect.colliderect(obs_rect):
        game_over = True

    screen.fill((255,255,255))
    if dino_image:
        screen.blit(dino_image, player_rect)
    else:
        py.draw.rect(screen, (0,0,255), player_rect)
    if cactus_image:
        screen.blit(cactus_image,obs_rect)
    else: py.draw.rect(screen, (255,0,0), obs_rect)

    score_text = font.render(f"Score : {score}", True, (50, 50, 50))
    screen.blit(score_text, (20, 20))

    if game_over:
        overlay = py.Surface((800,400))
        overlay.fill((255, 0, 0))
        overlay.set_alpha(50)
        screen.blit(overlay, (0,0))

        re_font = py.font.SysFont("malgungothic", 30)
        text = re_font.render("game over, press 'R' to respawn.", True, (0,0,0))
        screen.blit(text, (100,130))

    py.display.flip()
    clock.tick(60)
