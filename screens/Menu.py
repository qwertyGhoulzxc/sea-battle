import pygame
from utils.Button import Button
from Enums import Colors, Screens

class HomeScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = pygame.image.load("./assets/bg_1.jpg")

        button_width = 200
        button_height = 80
        center_x = (screen_width - button_width) // 2
        center_y = (screen_height - button_height) // 2
        self.play_button = Button(Colors.BLUE.value, center_x, center_y, button_width, button_height, "Play")

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.isOver(pygame.mouse.get_pos()):
                    return Screens.PLACE_SHIPS_1.value
        return Screens.MENU.value

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.play_button.draw(surface,Colors.WHITE.value)

    def update(self):
        pass
