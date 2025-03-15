import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        # pygame.mouse.set_visible(False)
        pygame.display.set_caption("Game")

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def update_screen(self):
            self.screen.fill(self.settings.bg_color)                
            pygame.display.flip()

class Player:
    pass

class Enemy:
    pass

class Settings:
    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (25, 25, 112)

if __name__ == "__main__":
    Game().run_game()