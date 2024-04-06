import pygame
import sys

sys.path.append("game")
sys.path.append("game/visual")
from game import Game
from events import handle_main_events


def start():
    game = Game()
    game.window = pygame.display.set_mode((game.size, game.size))

    running = True
    while running:
        handle_main_events(game)

    pygame.quit()


if __name__ == "__main__":
    start()