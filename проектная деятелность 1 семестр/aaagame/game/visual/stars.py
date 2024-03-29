import pygame
import math
import random


class Star:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.brightness = 10
        self.speed = math.hypot(*vel)
        self.warp_factor = 1.0
        self.TRAIL_LENGTH = 2

    @property
    def end_pos(self):
        x, y = self.pos
        vx, vy = self.vel
        return (
            x - vx * self.warp_factor * self.TRAIL_LENGTH / 60,
            y - vy * self.warp_factor * self.TRAIL_LENGTH / 60,
        )


class StarBackground:
    def __init__(self, size):
        self.size = size
        self.acceleration = 1.0
        self.drag = 0.71
        self.trail_length = 2
        self.min_warp_factor = 0.1
        self.bounds = pygame.Rect(0, 0, self.size, self.size)
        self.warp_factor = self.min_warp_factor
        self.center_x = self.size // 2
        self.center_y = self.size // 2
        self.stars = []
        self.screen = pygame.display.set_mode((self.size, self.size))
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for star in self.stars:
            b = star.brightness
            color = (b, b, b)
            pygame.draw.line(self.screen, color, star.end_pos, star.pos)

    def update(self, dt):
        self.warp_factor += self.acceleration * dt
        self.warp_factor = self.min_warp_factor + (self.warp_factor - self.min_warp_factor) * self.drag ** dt

        while len(self.stars) < 300:
            angle = random.uniform(-math.pi, math.pi)
            speed = 255 * random.uniform(0.3, 1.0) ** 2
            dx = math.cos(angle)
            dy = math.sin(angle)
            d = random.uniform(25 + self.trail_length, 100)
            pos = self.center_x + dx * d, self.center_y + dy * d
            vel = speed * dx, speed * dy
            self.stars.append(Star(pos, vel))

        for s in self.stars:
            x, y = s.pos
            vx, vy = s.vel
            x += vx * self.warp_factor * dt
            y += vy * self.warp_factor * dt
            s.pos = x, y
            s.brightness = min(s.brightness + self.warp_factor * 200 * dt, s.speed)
            s.vel = vx * 2 ** dt, vy * 2 ** dt

        self.stars = [star for star in self.stars if self.bounds.collidepoint(star.end_pos)]
