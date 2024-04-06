from enemy.enemy import Enemy

enemy_types = {
    "SpeedyBug": {
        "size": 50,
        "speed": 10,
        "spawn_x": 0,
        "spawn_y": 1000
    },
    "SpeedyBug2": {
        "size": 50,
        "speed": 15,
        "spawn_x": 200,
        "spawn_y": 1000
    },
    "UFO": {
        "size": 75,
        "speed": 8,
        "spawn_x": 0,
        "spawn_y": 500
    },
    "WavyBug": {
        "size": 100,
        "speed": 17,
        "spawn_x": 0,
        "spawn_y": 0
    },
    "BigBug": {
        "size": 120,
        "speed": 2,
        "spawn_x": 500,
        "spawn_y": 0
    }
}


class SpeedyBug(Enemy):
    def __init__(self, x, y, size, speed, target_x, target_y):
        super().__init__(x, y, size, speed, target_x, target_y)

    def update(self):
        pass


class SpeedyBug2(Enemy):
    def __init__(self, x, y, size, speed, target_x, target_y):
        super().__init__(x, y, size, speed, target_x, target_y)

    def update(self):
        pass


class UFO(Enemy):
    def __init__(self, x, y, size, speed, target_x, target_y):
        super().__init__(x, y, size, speed, target_x, target_y)

    def update(self):
        pass


class WavyBug(Enemy):
    def __init__(self, x, y, size, speed, target_x, target_y):
        super().__init__(x, y, size, speed, target_x, target_y)

    def update(self):
        pass


class BigBug(Enemy):
    def __init__(self, x, y, size, speed, target_x, target_y):
        super().__init__(x, y, size, speed, target_x, target_y)

    def update(self):
        pass
