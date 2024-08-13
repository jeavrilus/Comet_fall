from typing import Any
import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, jeu) -> None:
        super().__init__()
        self.jeu = jeu
        self.image = pygame.image.load("assets/player.png") # chargement de l'img. souhaité
        self.rect = self.image.get_rect() # récupération des coordonnées de l'img souhaité pr pouvoir la déplacer
        self.rect.x = 400
        self.rect.y = 500
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.speed = 4
        self.all_projectiles = pygame.sprite.Group()

    def damage(self, amount):
        if self.health - amount > amount:
            # infliger les degats
            self.health -= amount

    # Creer un jauge de vie
    def update_health_bar(self, surface):
        # dessiner le jauge
        pygame.draw.rect(surface,(60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])
         

    def launch_projectile(self):
        # creer une nouvelle instance de la classe Projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def move_right(self):
        # si le joueur n'entre pas en collision avec un monstre
        if not self.jeu.check_collision(self, self.jeu.all_monsters): # self represente "player" et self.jeu.all_monsters represente "le groupe de monstre"
            self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed