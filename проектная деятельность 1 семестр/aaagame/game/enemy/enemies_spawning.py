import pygame
import threading
from enemy.enemy_types import *
from functions import get_enemy_stats

enemies_per_wave = {
    0: 0,
    1: 2,
    2: 10,
    3: 12,
    4: 8,
    5: 5
}


class EnemySpawning:
    def __init__(self, game_size, enemy_size, enemy_speed, wave_size, enemy_spawn_delay, wave_delay, enemies):
        self.game_size = game_size
        self.enemy_size = enemy_size
        self.enemy_speed = enemy_speed
        self.enemies = enemies

        self.wave_size = wave_size
        self.enemy_spawn_delay = enemy_spawn_delay
        self.wave_delay = wave_delay

        self.enemies_spawned = 0
        self.current_wave = 0
        self.enemies_in_wave = enemies_per_wave[self.current_wave]
        self.last_enemy_spawn_time = pygame.time.get_ticks()
        self.last_wave_time = pygame.time.get_ticks()

        self.center = self.game_size // 2

        self.spawn_thread = threading.Thread(target=self.spawn_enemies_thread)
        self.spawn_thread.daemon = True
        self.spawn_thread.start()

    def spawn_enemy(self, enemy_type, count=1):
        wave_x, wave_y, size, speed = get_enemy_stats(enemy_type)
        for _ in range(count):
            enemy = enemy_type(wave_x, wave_y, size, speed, self.center, self.center)
            self.enemies_spawned += 1
            self.enemies.append(enemy)
            pygame.time.wait(self.enemy_spawn_delay)

    def spawn_enemy_inversion(self, enemy_type, count=1):
        wave_x, wave_y, size, speed = get_enemy_stats(enemy_type)
        for _ in range(count):
            enemy = enemy_type(abs(1000 - wave_x), wave_y, size, speed, self.center, self.center)
            self.enemies_spawned += 1
            self.enemies.append(enemy)
            pygame.time.wait(self.enemy_spawn_delay)

    def spawn_new_enemy(self):
        def spawn_enemy_helper(spawn_method, enemy_type, count):
            threads.append(threading.Thread(target=spawn_method, args=(enemy_type, count)))

        threads = []
        if self.current_wave == 1:
            spawn_enemy_helper(self.spawn_enemy, SpeedyBug, 1)
            spawn_enemy_helper(self.spawn_enemy_inversion, SpeedyBug, 1)

        elif self.current_wave == 2:
            spawn_enemy_helper(self.spawn_enemy, SpeedyBug2, 5)
            spawn_enemy_helper(self.spawn_enemy_inversion, SpeedyBug2, 5)

        elif self.current_wave == 3:
            spawn_enemy_helper(self.spawn_enemy, UFO, 1)
            spawn_enemy_helper(self.spawn_enemy_inversion, UFO, 1)
            spawn_enemy_helper(self.spawn_enemy, SpeedyBug, 5)
            spawn_enemy_helper(self.spawn_enemy_inversion, SpeedyBug, 5)

        elif self.current_wave == 4:
            spawn_enemy_helper(self.spawn_enemy, WavyBug, 2)
            spawn_enemy_helper(self.spawn_enemy_inversion, WavyBug, 2)
            spawn_enemy_helper(self.spawn_enemy, SpeedyBug2, 2)
            spawn_enemy_helper(self.spawn_enemy_inversion, SpeedyBug2, 2)

        elif self.current_wave == 5:
            spawn_enemy_helper(self.spawn_enemy, WavyBug, 1)
            spawn_enemy_helper(self.spawn_enemy_inversion, WavyBug, 1)
            spawn_enemy_helper(self.spawn_enemy, UFO, 1)
            spawn_enemy_helper(self.spawn_enemy_inversion, UFO, 1)
            spawn_enemy_helper(self.spawn_enemy, BigBug, 1)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def handle_enemy_spawning(self):
        current_time = pygame.time.get_ticks()
        if self.enemies_spawned == 0:
            self.spawn_new_enemy()
            self.last_enemy_spawn_time = current_time

    def handle_wave_transition(self):
        current_time = pygame.time.get_ticks()
        if (self.enemies_spawned >= 0 and
                len(self.enemies) == 0 and current_time - self.last_wave_time > self.wave_delay):
            self.current_wave += 1
            if self.current_wave == 6:
                self.current_wave = 1
            self.enemies_spawned = 0
            self.last_wave_time = current_time

    def spawn_enemies_thread(self):
        while True:
            self.handle_enemy_spawning()
            self.handle_wave_transition()
            pygame.time.wait(self.enemy_spawn_delay)
