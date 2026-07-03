import pygame as py
import random as rd
import sys

py.init()
screen=py.display.set_mode((800,400))
clock=py.time.Clock()

rect_x, rect_y = 200,100
rect_speed = 5

targets = []

last_spawn_time = py.time.get_ticks()
spawn_delay = 0

target_rect = py.Rect(500,200,40,40)
score = 0
game_font = py.font.SysFont(None,40)

running=True
while running:
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            running=False
        
        if event.type == py.MOUSEBUTTONDOWN:
            for target in targets:
                if target.collidepoint(event.pos):
                    targets.remove(target)
                    score+=1
                    break
    screen.fill((255,255,255))

    current_time = py.time.get_ticks()

    if current_time - last_spawn_time > spawn_delay:
        random_x = rd.randint(20, 800 - 60)
        random_y = rd.randint(20, 400 - 60)
        new_target = py.Rect(random_x, random_y, 40, 40)
        targets.append(new_target)
        last_spawn_time = current_time


    for target in targets:
        py.draw.rect(screen, (0,0,255), target)
    score_surface = game_font.render(f"Score : {score}", True, (0,0,0))
    screen.blit(score_surface,(10,10))

    py.display.flip()

py.quit()
sys.exit()