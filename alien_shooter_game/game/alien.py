import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """class to represent alien in fleet"""

    def __init__(self, ai_settings, screen):
        """initialize alien"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien position
        self.x = float(self.rect.x)

    def draw_alien(self):
        """Draw the alien at the current position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move alien to the right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
