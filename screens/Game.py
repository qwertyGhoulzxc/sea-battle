import pygame
from utils.Button import Button
from Enums import Colors, Screens

class GameScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = pygame.image.load("./assets/bg_1.jpg")

        #реализовать event нажития на клетку доски в как getAttacked

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.isOver(pygame.mouse.get_pos()):
                    print("Play button clicked!")
                    return Screens.PLACE_SHIPS_1.value
        return Screens.MENU.value

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.play_button.draw(surface)

    def update(self):
        pass
