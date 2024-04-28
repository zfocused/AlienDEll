import pygame

class Ship:
    def __init__(self, ai_game):
        # innitialize ship
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # load ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        # Movement flag
        self.moving_left = False
        self.moving_right = False
        
    
    def update(self):
        # update ship based on movement flag
        #if self.moving_left == True:
            #self.x -= self.settings.ship_speed       
        #if self.moving_right == True:
            #self.x += self.settings.ship_speed
        

        

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.rect.x = self.x

        if self.moving_right and self.rect.right < self.screen_rect.right:
        # update rect object form self.x
            self.x += self.settings.ship_speed
            self.rect.x = self.x
     

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)
