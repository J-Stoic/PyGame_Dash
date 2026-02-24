import sys
import time
import math
import random

import pygame
import pygame.locals


WIDTH, HEIGHT = 1000, 500

GRAVITY = 0.75
MAX_FALL_SPEED = 18

MOVE_ACCEL = 1.75
MAX_RUN_SPEED = 12.5
AIR_CONTROL = 0.68

GROUND_FRICTION = 0.78
AIR_FRICTION = 0.99

JUMP_VELOCITY = 14.5

PLAYER_SIZE = 44
ARM_W, ARM_H = 8, 16

START_GROUND_Y = HEIGHT - 40

STAR_BUFFER_AHEAD = 2200
STAR_CLEANUP_BEHIND = 1200
STAR_SPARSE_PER_CHUNK = 160
STAR_CLUSTERS_PER_CHUNK = 6
STAR_CLUSTER_SIZE_RANGE = (16, 50)

TRAIL_MAX_POINTS = 34
TRAIL_SPACING = 6.0


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        screen.fill("#000000")

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            #time.monotonic() + x amount of time

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()