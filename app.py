import pygame

from screens.Game import GameScreen
from screens.PlaceShips import PlaceShips
from screens.Menu import HomeScreen
from Enums import Screens
from Game import Game


pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("./assets/music_.mp3")

screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Sea Battle")

game = Game()

screens = {
    Screens.PLACE_SHIPS_1.value: PlaceShips(screen_width, screen_height,game,1),
    Screens.MENU.value: HomeScreen(screen_width, screen_height),
    Screens.PLACE_SHIPS_2.value: PlaceShips(screen_width, screen_height,game,2),
    Screens.GAME.value : GameScreen(screen_width, screen_height,game)
}

current_screen = Screens.MENU.value
clock = pygame.time.Clock()
running = True
pygame.mixer.music.play(-1)
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    next_screen = screens[current_screen].handle_events(events)
    current_screen = next_screen

    screens[current_screen].update()
    screens[current_screen].draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
