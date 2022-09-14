from ast import If
import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600))


animate = True


def play_animation():
    global index, play_sur
    if animate == True:
        index += 0.2
        if index >= len(play_walk):
            index = 0
        play_sur = play_walk[int(index)]


def enemy_animation():
    global enemy_index, enemy
    if animate == True:
        enemy_index += 0.2
        if enemy_index >= len(enemy_walk):
            enemy_index = 0
        enemy = enemy_walk[int(enemy_index)]


def fly_animation():
    global fly_index, fly
    if animate == True:
        fly_index += 0.2
        if fly_index >= len(fly_walk):
            fly_index = 0
        fly = fly_walk[int(fly_index)]


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(fly, obstacle_rect)
            else:
                screen.blit(enemy, obstacle_rect)
        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rec in obstacles:
            if player.colliderect(obstacle_rec):
                return False

    return True


# Gravity
gravity = 0

# SCORE:


def score():
    s_core = int((pygame.time.get_ticks()-start_time)/1000)
    text = pygame.font.SysFont('Calibri', 25, True, False)
    text_sur = text.render(f'{s_core}', False, 'blue')
    screen.blit(text_sur, (350, 100))
    return s_core


# Timer
obstacle_timer = pygame.USEREVENT + 0
pygame.time.set_timer(obstacle_timer, 1500)


start_time = 0
# player-animation
# Surfaces:
pic = pygame.image.load('clouds_bg_2.png').convert_alpha()
pic = pygame.transform.rotozoom(pic, 0, 1.4)

pic_2 = pygame.image.load('the floor.png').convert_alpha()
pic_2 = pygame.transform.rotozoom(pic_2, 0, 1.4)


pic_6 = pygame.image.load('4_better2.png').convert_alpha()
pic_6 = pygame.transform.rotozoom(pic_6, 0, 1.4)

pic_7 = pygame.image.load('5_better2.png').convert_alpha()
pic_7 = pygame.transform.rotozoom(pic_7, 0, 1.4)

pic_8 = pygame.image.load('2nd_better2.png').convert_alpha()
pic_8 = pygame.transform.rotozoom(pic_8, 0, 1.4)


enemy_1 = pygame.image.load('snail1.png').convert_alpha()
enemy_2 = pygame.image.load('snail2.png').convert_alpha()
enemy_walk = [enemy_1, enemy_2]
enemy_index = 0
enemy = enemy_walk[enemy_index]
snail_rect = enemy.get_rect(bottomleft=(800, 470))


enemy_3 = pygame.image.load('Fly1.png').convert_alpha()
enemy_4 = pygame.image.load('Fly2.png').convert_alpha()
fly_walk = [enemy_3, enemy_4]
fly_index = 0
fly = fly_walk[fly_index]
fly_rect = fly.get_rect(bottomleft=(800, 300))

obstacle_rect_list = []

# enemy_x=700
# fly_x=700

# Rectangles


# def enemy_moition():
#global enemy_x
# enemy_x==400 :
#  enemy_x=800
#   scre#en.blit(enemy,(enemy_x,480))
#
play_walk = [pic_6, pic_7, pic_8]
index = 0
play_sur = play_walk[index]
# Time:
clock = pygame.time.Clock()

game_Active = True
game_on = True
player_rect = play_sur.get_rect(topleft=(200, 430))


# Active_game_loop
while game_Active:
    # Quiting Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_Active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.y >= 430:
                gravity = -20

        if event.type == pygame.KEYDOWN and game_on == False:

            player_rect = play_sur.get_rect(topleft=(200, 430))
            game_on = True
            start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_on == True:

            if randint(0, 2):
                obstacle_rect_list.append(fly.get_rect(
                    bottomleft=(randint(800, 1100), 300)))

            else:
                obstacle_rect_list.append(enemy.get_rect(
                    bottomleft=(randint(800, 1100), 530)))

    if game_on:

        screen.blit(pic_2, (0, 100))
        screen.blit(pic, (0, 0))

        gravity += 1
        player_rect.y += gravity
        if player_rect.y >= 430:
            player_rect.y = 430
        screen.blit(play_sur, player_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        play_animation()
        enemy_animation()
        fly_animation()
        score()
        end_game = score()
        game_on = collisions(player_rect, obstacle_rect_list)
    # game_stop

    else:

        screen.fill((70, 142, 220))
        play_animation()
        enemy_animation()
        fly_animation()
        obstacle_rect_list.clear()
        gravity = 0
        player_rect = play_sur.get_rect(midbottom=(400, 300))
        display_player = pygame.transform.scale(play_sur, (200, 400))
        screen.blit(play_sur, player_rect)
        text_2 = pygame.font.SysFont('Calibri', 25, True, False)
        text_2_sur = text_2.render(
            f'you managed to run for: {end_game} second.', False, 'black')
        # display_score=pygame.transform.scale2x(text_2_sur)
        screen.blit(text_2_sur, (200, 100))
        text_3 = pygame.font.SysFont('Calibri', 25, True, False)
        text_3_sur = text_3.render(
            'Press any key to continue.', False, 'black')
        # display_score=pygame.transform.scale2x(text_2_sur)
        screen.blit(text_3_sur, (250, 400))

    pygame.display.update()
    clock.tick(60)


pygame.quit()
