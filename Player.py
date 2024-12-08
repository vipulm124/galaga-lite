import pygame

class Player:
    """
    To manage a player
    """
    def __init__(self, gl) -> None:
        self.screen = gl.screen
        self.screen_rect = gl.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
 
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.move_right = False
        self.move_left = False
        self.settings = gl.settings
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        elif self.move_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        
        self.rect.x = self.x