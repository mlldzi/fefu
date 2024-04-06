import pygame
import time
import math
from bullet import Bullet


class Player:
    def __init__(self, size, x, y, speed, bullet_speed, bullet_cooldown_time, clock):
        self.size = size
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, size, size)
        self.speed = speed

        self.bullet_speed = bullet_speed
        self.bullet_cooldown_time = bullet_cooldown_time
        self.bullets = []
        self.last_shot_time = 0
        self.clock = clock

        self.health = 7
        self.has_shield = True


    def move(self, center_x, center_y):
        keys = pygame.key.get_pressed()
        dx = center_x - self.x
        dy = center_y - self.y
        distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
        radius = math.sqrt((self.x - center_x) ** 2 + (self.y - center_y) ** 2)
        shield_radius = radius - 10  # Reduce shield radius by 10 units
        angle = math.atan2(self.y - center_y, self.x - center_x)

        if distance_to_center > 1:
            if keys[pygame.K_a]:
                angle += math.radians(self.speed)
            if keys[pygame.K_d]:
                angle -= math.radians(self.speed)

            self.x = center_x + radius * math.cos(angle)
            self.y = center_y + radius * math.sin(angle)

    def create_bullets(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= self.bullet_cooldown_time:
            bullet1 = Bullet(self.x, self.y, self.bullet_speed, 5)
            self.last_shot_time = current_time
            return [bullet1]
        else:
            return []
