import sys
import pygame
from pygame.sprite import Group
from game_stats import GameStats
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # Initialize game, settings, and screen objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Shooter")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, alien
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    # Make group(set) to store bullets
    bullets = Group()
    aliens = Group()

    # Create alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
