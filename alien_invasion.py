#Mariah Salgado
#CWID:887 119 303
import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pygame.sprite import Group

import game_functions as gf


def run_game():
    #Initializes game and creates a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) 

    pygame.display.set_caption("Alien Invasion")

    #Makes the Play button.
    play_button = Button(ai_settings, screen, "Play")

    #Instance stores game statistics and creates a scoreboard.
    stats = GameStats(ai_settings)
    score_board = Scoreboard(ai_settings, screen, stats)

    #Creates ship, bullets, aliens group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Creates the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
       # Gets rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        #print(len(bullets))

        gf.check_events(ai_settings, screen, stats, score_board, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, score_board, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, score_board, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, score_board, ship, aliens, bullets, play_button)
        
run_game()
