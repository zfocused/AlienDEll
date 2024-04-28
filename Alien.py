import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Initialize the game, and create game resources."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((self.settings.screen_with, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = Settings().bg_color
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    """Start the main loop for the game"""
    def run_game(self):
        # Watch for keyboard and mouse events.
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullets.update()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                     self._fire_bullet()
            if event.type == pygame.KEYUP:
                self._check_keyup_events()

    def _check_keydown_events(self, _event):
        if _event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
        if _event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
    def _check_keyup_events(self):
        self.ship.moving_left = False
        self.ship.moving_right = False
    
    def _fire_bullet(self):
         # create a new bullet and add it to the bullets group
         new_bullet = Bullet(self)
         self.bullets.add(new_bullet)

    # set background color
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
            # Make a game instance, and run the game.
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()
        pygame.display.flip()

# print parameters
print(f'Backgoud is {AlienInvasion().bg_color} screen resolution is {AlienInvasion().screen} settings are {AlienInvasion().settings}')


# Make a game instance, and run the game.
if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()
    
