import math


class Enemy:
    def __init__(self, x, y, size, speed, center_x, center_y):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.center_x = center_x
        self.center_y = center_y
        self.hitbox = size

        self.angle = 0
        self.previous_x = x
        self.previous_y = y

    def move(self):
        dx = self.center_x - self.x
        dy = self.center_y - self.y
        distance_to_center = math.sqrt(dx ** 2 + dy ** 2)

        if distance_to_center > 75:
            direction_x = dx / distance_to_center
            direction_y = dy / distance_to_center
            self.x += direction_x * self.speed
            self.y += direction_y * self.speed
        else:
            target_x = self.center_x + math.sin(self.angle) * 75
            target_y = self.center_y + math.cos(self.angle) * 75
            self.x = self.lerp(self.x, target_x, 0.1)
            self.y = self.lerp(self.y, target_y, 0.1)
            self.angle += 0.1

    def lerp(self, start, end, t):
        return start + (end - start) * t

    def collides_with(self, player_x, player_y, player_size):
        distance = math.sqrt((self.x - player_x) ** 2 + (self.y - player_y) ** 2)
        if distance < (self.size + player_size) / 2:
            return True
        return False
