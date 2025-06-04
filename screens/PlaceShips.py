import pygame

from utils.Button import Button
from Enums import Colors, Screens
from utils.InputBox import InputBox


class PlaceShips:
    def __init__(self, screen_width, screen_height,game,player_number,):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = pygame.image.load("./assets/bg_1.jpg")
        self.game = game
        self.player = self.game.player1 if player_number == 1 else self.game.player2
        self.next_screen = Screens.PLACE_SHIPS_2.value if player_number == 1 else Screens.GAME.value
        self.current_screen = Screens.PLACE_SHIPS_1.value if player_number == 1 else Screens.PLACE_SHIPS_2.value
        self.input_box = InputBox(600, 400, 200, 40, self.player.get_name())
        self.rotate_btn = Button(Colors.BLUE.value, 500, 400, 50, 50, "R")
        self.next_btn = Button(Colors.BLUE.value, 700, 500, 230, 50, "Next ->")
        self.actual_data = False



    def handle_events(self, events):
        for event in events:
            self.input_box.handle_event(event)
            self.player.set_name(self.input_box.text)
            self.player.board.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rotate_btn.isOver(pygame.mouse.get_pos()):
                    self.player.board.rotate_ship()

                if self.next_btn.isOver(pygame.mouse.get_pos())and len(self.player.board.ships_list) == 10 :
                    self.actual_data = False
                    return self.next_screen
        return self.current_screen

    def draw(self, surface):
        if not self.actual_data:
            self.input_box.set_text(self.player.get_name())
            self.actual_data = True

        surface.blit(self.background, (0, 0))
        self.player.board.draw(surface)
        self.rotate_btn.draw(surface,Colors.WHITE.value)
        self.next_btn.draw(surface,Colors.WHITE.value)
        self.input_box.update()
        self.input_box.draw(surface)

    def update(self):
        pass