import math
import random
from enemy.enemy_types import *
from enemy.drop_bonus import Bonus

class EnemyHandler:
    def __init__(self, size, enemy_size, enemy_speed, max_enemies, enemy_spawn_delay, wave_delay, enemies, window, bonuses):
        self.size = size
        self.enemy_size = enemy_size
        self.enemy_speed = enemy_speed
        self.max_enemies = max_enemies
        self.enemy_spawn_delay = enemy_spawn_delay
        self.wave_delay = wave_delay
        self.enemies = enemies
        self.window = window
        self.bonuses = bonuses

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()

    def check_enemy_collisions_bullet(self, bullets):
        bullets_to_remove = []
        for bullet in bullets:
            for enemy in self.enemies:
                distance = math.sqrt((bullet.x - enemy.x) ** 2 + (bullet.y - enemy.y) ** 2)
                if distance < (bullet.hitbox + enemy.hitbox) / 2:
                    bullets_to_remove.append(bullet)
                    self.enemies.remove(enemy)
                    if isinstance(enemy, UFO):
                        bonus_type = random.choice(["repair", "moon_shard", "shield"])
                        bonus = Bonus(enemy.x, enemy.y, bonus_type)
                        self.bonuses.append(bonus)
                    break

        for bullet in bullets_to_remove:
            bullets.remove(bullet)

    def check_enemy_collision_player(self, player):
        for enemy in self.enemies:
            if player.x < enemy.x + enemy.hitbox and \
                    player.x + player.size > enemy.x and \
                    player.y < enemy.y + enemy.hitbox and \
                    player.y + player.size > enemy.y:
                if player.has_shield:
                    player.has_shield = False
                else:
                    player.health -= 1
                self.enemies.remove(enemy)
                if player.health <= 0:
                    return False
        return True