from pygame.sprite import Sprite
import pygame 

class Bullet(Sprite):

    def __init__(self, gl) -> None:
        super().__init__()
        self.screen = gl.screen
        self.bullet_settings = gl.settings
        self.color = self.bullet_settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.bullet_settings.bullet_width, self.bullet_settings.bullet_height)
        self.rect.midtop = gl.player.rect.midtop


        self.y = float(self.rect.y)

    def update(self):
        # move bullet up the screen
        self.y -= self.bullet_settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)