import pygame
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('C:/Users/Naveen/Alien-Invasion-Master/images/ship1.bmp.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
                self.rect.x +=1
        if self.moving_left:
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.ship_speed
                self.rect.x -=1
            self.rect.x = self.x
            
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
