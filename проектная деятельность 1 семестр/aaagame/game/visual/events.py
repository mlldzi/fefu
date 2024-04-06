import pygame
import os
import sys
import threading
from render import render_game
from player import Player
from enemy.enemies_handler import EnemyHandler
from enemy.enemies_spawning import EnemySpawning


def start_enemy_spawning_thread(game):
    enemy_spawning_thread = threading.Thread(target=game.handle_enemy_spawning)
    enemy_spawning_thread.start()


def handle_main_events(game):
    button_restart_img = pygame.transform.scale(
        pygame.image.load(os.path.join("assets", "images", "restart_button.png")), (177, 100))
    button_restart_rect = pygame.Rect(game.size // 2 - 100, game.size // 2 + 200, 177, 100)
    button_start_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "start_BUTTON.png")),
                                              (217, 100))
    button_start_rect = pygame.Rect(game.size // 2 - 100, game.size // 2 + 200, 217, 100)
    running = False

    while not running:
        game.window.fill(game.BLACK)
        game.window.blit(button_start_img, button_start_rect)
        running = game.check_click(button_start_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    while running:
        game.window.fill(game.BLACK)

        game.update_background()
        start_enemy_spawning_thread(game)
        game.move_enemies()
        game.check_enemy_collisions()
        game.handle_wave_transition()
        game.player.move(game.size // 2, game.size // 2)

        render_game(game)
        pygame.display.update()
        game.clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        running = game.handle_events()
        while not running:
            game.window.fill(game.BLACK)
            game.window.blit(button_restart_img, button_restart_rect)
            running = game.check_click(button_restart_rect)
            pygame.display.update()

            if running:
                game.enemies = []
                game.bonuses = []
                game.bullets = []
                game.killed_enemies = 0
                game.spawned_enemies = 0
                game.enemy_spawning = EnemySpawning(game.size, game.enemy_size, game.enemy_speed, game.max_enemies,
                                                    game.enemy_spawn_delay, game.wave_delay, game.enemies)
                game.enemy_handler = EnemyHandler(game.size, game.enemy_size, game.enemy_speed, game.max_enemies,
                                                  game.enemy_spawn_delay, game.wave_delay, game.enemies, game.window, game.bonuses)
                game.player = Player(game.player_size, game.player_x, game.player_y, game.player_speed,
                                     game.bullet_speed, game.bullet_cooldown_time, game.clock)
                game.handle_enemy_spawning()
                break