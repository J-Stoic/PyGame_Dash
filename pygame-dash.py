# Add "Mx-El" on GitHub as a contributor


import sys

import pygame
import pygame.locals


WIDTH, HEIGHT = 1000, 500
PLAYER_SIZE = 30
GROUND_Y = 420
GRAVITY = 0.8
MOVE_SPEED = 5
JUMP_STRENGTH = -14

GOAL_COLOR = (255, 215, 0)
START_X = 60
START_Y = 200

class Player:
    def __init__(self, x, y, jump_sound):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.vel_y = 0
        self.on_ground = False
        self.jump_sound = jump_sound

    def update(self, keys, platforms):
        dx = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= MOVE_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += MOVE_SPEED

        self.rect.x += dx
        for platform in platforms:
            if self.rect.colliderect(platform):
                if dx > 0:
                    self.rect.right = platform.left
                elif dx < 0:
                    self.rect.left = platform.right

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False
            if self.jump_sound:
                self.jump_sound.play()

        self.vel_y += GRAVITY
        self.rect.y += int(self.vel_y)
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.bottom
                    self.vel_y = 0


def load_level(level_num):
    if level_num == 1:
        platforms = [
            pygame.Rect(0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y),
            pygame.Rect(180, 350, 140, 20),
            pygame.Rect(380, 300, 140, 20),
            pygame.Rect(600, 240, 140, 20),
            pygame.Rect(820, 190, 140, 20),
            pygame.Rect(960, 190, 20, GROUND_Y - 190),
        ]
        goal = pygame.Rect(900, 150, 40, 40)
    elif level_num == 2:
        platforms = [
            pygame.Rect(0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y),
            pygame.Rect(200, 360, 120, 20),
            pygame.Rect(370, 325, 20, 120),
            pygame.Rect(450, 250, 120, 20),
            pygame.Rect(650, 200, 20, 140),
            pygame.Rect(730, 150, 140, 20),
            pygame.Rect(960, 150, 20, GROUND_Y - 150),
        ]
        goal = pygame.Rect(900, 110, 40, 40)
    elif level_num == 3:
        platforms = [
            pygame.Rect(0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y),
            pygame.Rect(130, 360, 100, 20),
            pygame.Rect(280, 320, 20, 100),
            pygame.Rect(360, 280, 110, 20),
            pygame.Rect(520, 240, 20, 100),
            pygame.Rect(600, 200, 110, 20),
            pygame.Rect(760, 160, 20, 100),
            pygame.Rect(820, 240, 120, 20),
            pygame.Rect(960, 240, 20, GROUND_Y - 240),
        ]
        goal = pygame.Rect(900, 200, 40, 40)
    elif level_num == 4:
        platforms = [
            pygame.Rect(0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y),
            pygame.Rect(150, 370, 100, 20),
            pygame.Rect(300, 330, 20, 90),
            pygame.Rect(380, 290, 110, 20),
            pygame.Rect(540, 250, 20, 90),
            pygame.Rect(620, 210, 110, 20),
            pygame.Rect(780, 170, 20, 90),
            pygame.Rect(840, 130, 100, 20),
            pygame.Rect(960, 130, 20, GROUND_Y - 130),
        ]
        goal = pygame.Rect(900, 90, 40, 40)
    else:
        platforms = [
            pygame.Rect(0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y),
            pygame.Rect(120, 360, 90, 20),
            pygame.Rect(260, 320, 20, 100),
            pygame.Rect(340, 280, 90, 20),
            pygame.Rect(480, 240, 20, 100),
            pygame.Rect(560, 200, 90, 20),
            pygame.Rect(700, 160, 20, 100),
            pygame.Rect(780, 120, 90, 20),
            pygame.Rect(900, 80, 20, 100),
            pygame.Rect(960, 80, 20, GROUND_Y - 80),
        ]
        goal = pygame.Rect(930, 40, 40, 40)

    return platforms, goal


def reset_player(jump_sound):
    return Player(START_X, START_Y, jump_sound)


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()
    jump_sound = pygame.mixer.Sound("/Users/jamesbohn/Downloads/Jump Bounce SFX.wav")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("PyGame Dash")
    font = pygame.font.SysFont(None, 36)

    current_level = 1
    game_finished = False

    platforms, goal = load_level(current_level)
    player = reset_player(jump_sound)

    while True:
        screen.fill("#000000")
        if game_finished:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            pygame.display.flip()
            fps_clock.tick(fps)
            continue

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.update(keys, platforms)

        if player.rect.top > HEIGHT:
            player = reset_player(jump_sound)

        if player.rect.colliderect(goal):
            if current_level == 5:
                print("The End")
                game_finished = True
            else:
                current_level += 1
                platforms, goal = load_level(current_level)
                player = reset_player(jump_sound)

        for platform in platforms:
            pygame.draw.rect(screen, (100, 200, 100), platform)

        pygame.draw.rect(screen, (80, 160, 255), player.rect)

        level_text = font.render("Level: " + str(current_level), True, (255, 255, 255))
        screen.blit(level_text, (10, 10))

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()