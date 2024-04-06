import pygame
import math
import os
from enemy.enemy_types import *
from functions import *

HEART_PATH = os.path.join("assets", "images", "heart.png")
SHIP_PATH = os.path.join("assets", "images", "ship.png")
SMALL_ENEMY_PATH = os.path.join("assets", "images", "small_enemy.png")
BIG_ENEMY_PATH = os.path.join("assets", "images", "big_enemy_bug.png")
UFO_ENEMY_PATH = os.path.join("assets", "images", "small2_enemy.png")
WAVY_ENEMY_PATH = os.path.join("assets", "images", "middle_enemy_bug.png")
PLANET_PATH = os.path.join("assets", "images", "planet_2.png")
BULLET_PATH = os.path.join("assets", "images", "bullet_2.png")
REPAIR_BOX_PATH = os.path.join("assets", "images", "repair_box.png")
SHIELD_BOX_PATH = os.path.join("assets", "images", "shield_box.png")
FIRE_RED_BOX_PATH = os.path.join("assets", "images", "fire_red_box.png")
SHIELD_BUFF_PATH = os.path.join("assets", "images", "shield_buff.png")


def render_game(game):
    center = game.size // 2

    planet_image = pygame.image.load(PLANET_PATH)
    ship_image = pygame.image.load(SHIP_PATH)
    heart_image = pygame.image.load(HEART_PATH)
    bullet_image = pygame.image.load(BULLET_PATH)
    shield_buff_image = pygame.image.load(SHIELD_BUFF_PATH)

    planet_image = scale_image(planet_image, 50, 50)
    ship_image = scale_image(ship_image, 50, 50)
    heart_image = scale_image(heart_image, 50, 50)
    bullet_image = scale_image(bullet_image, 8, 37)

    planet_rect = planet_image.get_rect(center=(center, center))
    game.window.blit(planet_image, planet_rect)

    ship_x = int(game.player.x)
    ship_y = int(game.player.y)
    angle = math.atan2(ship_x - center, ship_y - center)
    rotated_ship_image = rotate_image(ship_image, angle)
    ship_rect = rotated_ship_image.get_rect(center=(ship_x, ship_y))
    game.window.blit(rotated_ship_image, ship_rect)

    for bullet in game.bullets:
        bullet.move(center)
        if abs(bullet.y - center) < 25 and abs(bullet.x - center) < 25:
            game.bullets.remove(bullet)
        else:
            angle = math.atan2(bullet.x - center, bullet.y - center)
            rotated_bullet_image = rotate_image(bullet_image, angle)
            scaled_bullet_image = pygame.transform.scale(rotated_bullet_image, (int(bullet.radius), int(bullet.radius)))
            bullet_rect = scaled_bullet_image.get_rect(center=(int(bullet.x), int(bullet.y)))
            game.window.blit(scaled_bullet_image, bullet_rect)

    for enemy in game.enemies:
        enemy_image = pygame.image.load(get_enemy_skin(enemy))
        enemy_image = scale_image(enemy_image, enemy.size, enemy.size)

        if isinstance(enemy, SpeedyBug) or isinstance(enemy, SpeedyBug2) or isinstance(enemy, WavyBug):
            rotated_enemy_image = rotate_enemy(enemy_image, enemy.previous_x, enemy.previous_y, enemy.x, enemy.y)
            enemy.previous_x = enemy.x
            enemy.previous_y = enemy.y
        else:
            rotated_enemy_image = enemy_image

        enemy_rect = rotated_enemy_image.get_rect(center=(int(enemy.x), int(enemy.y)))
        game.window.blit(rotated_enemy_image, enemy_rect)

    for bonus in game.bonuses:
        if bonus.bonus_type == "repair":
            bonus_image = pygame.image.load(REPAIR_BOX_PATH)
        elif bonus.bonus_type == "moon_shard":
            bonus_image = pygame.image.load(FIRE_RED_BOX_PATH)
        elif bonus.bonus_type == "shield":
            bonus_image = pygame.image.load(SHIELD_BOX_PATH)

        bonus.move(center)
        bonus.check_bonus_collision(game.player, game.bonuses)
        bonus_image = scale_image(bonus_image, bonus.size, bonus.size)
        bonus_rect = bonus_image.get_rect(center=(int(bonus.x), int(bonus.y)))
        game.window.blit(bonus_image, bonus_rect)

    heart_padding = 35
    for i in range(game.player.health):
        heart_pos_x = 10 + i * heart_padding
        heart_pos_y = game.size - 50
        heart_rect = pygame.Rect(heart_pos_x, heart_pos_y, 50, 50)
        game.window.blit(heart_image, heart_rect)
