import math
from functions import apply_bonus_effect


class Bonus:
    def __init__(self, x, y, bonus_type):
        self.x = x
        self.y = y
        self.size = 25
        self.hitbox = self.size
        self.bonus_type = bonus_type

    def move(self, center):
        dx = center - self.x
        dy = center - self.y
        distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
        direction_x = dx / distance_to_center
        direction_y = dy / distance_to_center
        self.y = self.y - direction_y
        self.x = self.x - direction_x

    def check_bonus_collision(self, player, bonuses):
        for bonus in bonuses:
            if player.x < bonus.x + bonus.hitbox and \
                    player.x + player.size > bonus.x and \
                    player.y < bonus.y + bonus.hitbox and \
                    player.y + player.size > bonus.y:
                apply_bonus_effect(player, bonus)
                bonuses.remove(bonus)
