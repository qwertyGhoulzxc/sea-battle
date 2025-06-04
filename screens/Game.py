import pygame
from utils.Button import Button
from Enums import Colors, Screens

class GameScreen:
    def __init__(self, screen_width, screen_height,game):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background = pygame.image.load("./assets/bg_1.jpg")
        self.game = game
        self.left_arrow_coords =  [(475, 275), (525, 245), (525, 305)]
        self.right_arrow_coords = [(475, 245), (475, 305), (525, 275)]
        self.font = pygame.font.SysFont("arial", 30)
        self.new_game_btn = Button(Colors.GRAY.value, screen_width / 2- 150, self.screen_height / 2 +75,100,50,
                                   'new game',20)
        self.revenge_btn = Button(Colors.GRAY.value, screen_width / 2 + 75, self.screen_height / 2+ 75,100,50,
                                   'revenge',20)


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                isGameOver = True if (self.game.gameOver == 1 or self.game.gameOver == 2) else False
                if self.game.turn == 1 and not isGameOver:
                    coords = self.game.player2.board.handle_game_event(event)
                    if len(coords) > 0:
                        self.game.attack(coords)
                elif self.game.turn == 2 and not isGameOver:
                    coords = self.game.player1.board.handle_game_event(event)
                    if len(coords) > 0:
                        self.game.attack(coords)
                if self.revenge_btn.isOver(pygame.mouse.get_pos()) and isGameOver:
                    self.game.revenge()
                    return Screens.PLACE_SHIPS_1.value
                if self.new_game_btn.isOver(pygame.mouse.get_pos()) and isGameOver:
                    self.game.newGame()
                    return Screens.PLACE_SHIPS_1.value

        return Screens.GAME.value

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        pygame.draw.polygon(surface, Colors.CORAL.value, self.right_arrow_coords if self.game.turn == 1 else
        self.left_arrow_coords)

        text_player1 = self.font.render(self.game.player1.get_name(), True, (255, 255, 255))
        text_rect1 = text_player1.get_rect(topleft=(100, 50))
        text_player2 = self.font.render(self.game.player2.get_name(), True, (255, 255, 255))
        text_rect2 = text_player1.get_rect(topright=(900, 50))
        surface.blit(text_player1 , text_rect1)
        surface.blit(text_player2 , text_rect2)
        self.game.draw(surface,)
        self.modal_window(surface)


    def update(self):
        pass

    def modal_window(self,surface):
        if self.game.gameOver == 1 or self.game.gameOver == 2:
            winner = self.game.player1 if self.game.gameOver == 2 else self.game.player2

            font_50 = pygame.font.SysFont("arial", 50)
            font_40 = pygame.font.SysFont("arial", 40)
            font_30 = pygame.font.SysFont("arial", 30)
            pygame.draw.rect(surface, Colors.BLUE.value, (self.screen_width/2-200, self.screen_height/2-150, 400, 300))
            winner_text = font_50.render('Winner:', True, (255, 255, 255))
            winner_text_rect = winner_text.get_rect(topright=(self.screen_width/2+75, self.screen_height/2-150))
            winner_name_text = font_40.render(winner.get_name(), True, (255, 255, 255))
            winner_name_text_rect = winner_text.get_rect(topright=(self.screen_width / 2 + 75, self.screen_height / 2 - 100))

            player1_name_text = font_30.render(self.game.player1.get_name(), True, (255, 255, 255))
            player1_name_text_rect = player1_name_text.get_rect(topleft=(self.screen_width / 2-200, self.screen_height/2-35))

            player2_name_text = font_30.render(self.game.player2.get_name(), True, (255, 255, 255))
            player2_name_text_rect = player2_name_text.get_rect(
                topright=(self.screen_width / 2+200, self.screen_height/2-35))

            result_text = font_40.render(str(self.game.player1.score)+ " : " + str(self.game.player2.score), True, (255, 255, 255))
            result_text_rect = result_text.get_rect( topleft = (self.screen_width/2-25 , self.screen_height/2) )
            surface.blit(result_text, result_text_rect)
            surface.blit(winner_text, winner_text_rect)
            surface.blit(winner_name_text, winner_name_text_rect)
            surface.blit(player1_name_text, player1_name_text_rect)
            surface.blit(player2_name_text, player2_name_text_rect)
            self.revenge_btn.draw(surface)
            self.new_game_btn.draw(surface)