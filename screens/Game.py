import pygame
from utils.Button import Button
from Enums import Colors, Screens

class GameScreen:
    def __init__(self, screen_width, screen_height,game):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = pygame.image.load("./assets/bg_1.jpg")
        self.game = game
        font = pygame.font.SysFont("arial", 30)
        self.text_player1 = font.render(self.game.player1.name, True, (255, 255, 255))  # белый цвет
        self.text_rect1 = self.text_player1.get_rect(topleft=(100, 50))
        self.text_player2 = font.render(self.game.player2.name, True, (255, 255, 255))  # белый цвет
        self.text_rect2 = self.text_player1.get_rect(topleft=(550, 50))
        self.left_arrow_coords =  [(475, 275), (525, 245), (525, 305)]
        self.right_arrow_coords = [(475, 245), (475, 305), (525, 275)]


    def handle_events(self, events):
        for event in events:
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # if self.play_button.isOver(pygame.mouse.get_pos()):
                #     print("Play button clicked!")
                #     return Screens.PLACE_SHIPS_1.value
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game.turn == 1:
                    coords = self.game.player2.board.handle_game_event(event)
                    if len(coords) > 0:
                        self.game.attack(coords)
                elif self.game.turn == 2:
                    coords = self.game.player1.board.handle_game_event(event)
                    if len(coords) > 0:
                        self.game.attack(coords)

        return Screens.GAME.value

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        pygame.draw.polygon(surface, Colors.CORAL.value, self.right_arrow_coords if self.game.turn == 1 else
        self.left_arrow_coords)

        surface.blit(self.text_player1 , self.text_rect1)
        surface.blit(self.text_player2 , self.text_rect2)
        self.game.draw(surface)


    def update(self):
        pass
