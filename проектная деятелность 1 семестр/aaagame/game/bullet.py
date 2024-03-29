import math


class Bullet:
    def __init__(self, x, y, speed, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.hitbox = radius

    def move(self, center):
        dx = center - self.x
        dy = center - self.y
        distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
        if distance_to_center > 25:
            direction_x = dx / distance_to_center
            direction_y = dy / distance_to_center
            if distance_to_center > self.speed:
                self.x += direction_x * self.speed
                self.y += direction_y * self.speed
            else:
                self.x = center
                self.y = center

