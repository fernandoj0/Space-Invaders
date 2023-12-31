import pygame

from pygame.sprite import Sprite

from game.utils.constants import BULLET, SCREEN_WIDTH, SCREEN_HEIGHT

# sprite es un objeto de pygame (objeto dibujable)
class BulletSpaceship:
    def __init__(self, spaceship_xpos, spaceship_ypos):
        self.image = BULLET
        self.image_width = 30
        self.image_height = 30
        self.image = pygame.transform.scale(self.image, (self.image_width,self.image_height))
        self.rect = self.image.get_rect()
        # definimos los valores de self.rect.x e y con los que iniciara la nave
        self.rect.x = spaceship_xpos
        self.rect.y = spaceship_ypos-self.image_height # nos permite que la nave completa aparezca por encima del borde inferior de la pantalla
        # definimos la valocidad en 5
        self.speed = 5
        self.is_active = True

    def update(self):
        if self.rect.y > -self.image_width:
            self.is_alive = False
        self.rect.y -= self.speed


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))



        

