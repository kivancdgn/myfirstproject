p# myfirstproject
-import pygame

class GameEngine:
    def __init__(self, title="Tony Engine", width=800, height=600, fps=60):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def run(self):
        while self.running:
            self.screen.fill((20, 20, 20))  # Ekranı siyah yapar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()

            for e in self.entities:
                e.update(keys)
                e.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()
--burasıda engine--
# game.py
import pygame
from engine import GameEngine

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Oyun motorunu başlat
engine = GameEngine("Tony Engine", 800, 600)
player = Player(100, 100)
engine.add_entity(player)
engine.run()

#Şimdi Kod bu kadardı 1. Başlatma 2. satırda analiz bu kadar şuan 
//
  //
def uptade(labe, keys);800
self.speed = add_entity
Finish("Run")



