import pygame
import sys
from Settings import Settings
from Player import Player
from Bullet import Bullet

class GalagaLite:
    def __init__(self) -> None:
        """
        Main class to manage game, assets and behaviours
        """
        pygame.init()
        # for cross device speed consistency
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Galaga - Lite")
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.bg_color = self.settings.bg_color

    
    def run_game(self):
        """
        start the main loop of the game
        """
        while True:
            self._check_events()
            self.player.update()
            self._update_bullets()

            # get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            
            self._update_screen()
            self.clock.tick(60)
    

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
                
            
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)
                
    


    def _check_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.move_right = True
        elif event.key == pygame.K_LEFT:
            self.player.move_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()



    def _check_key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.move_right = False
        elif event.key == pygame.K_LEFT:
             self.player.move_left = False

  


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.player.blitme()
        pygame.display.flip()

    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        self.bullets.update()

        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)



if __name__ == "__main__":
    """
    Make instance of the game and run it
    """
    gl = GalagaLite()
    gl.run_game()