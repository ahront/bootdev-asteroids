import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Shot.containers = (shots, updatable, drawable)
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  player = Player(x, y)
  asteroidfield = AsteroidField()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    for sprite in drawable:
      sprite.draw(screen)
    for sprite in updatable:
      sprite.update(dt)
    for asteroid in asteroids:
      if asteroid.collision(player):
        print('Game over!')
        sys.exit()
    for asteroid in asteroids:
      for shot in shots:
        if asteroid.collision(shot):
          shot.kill()
          asteroid.split()
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
  main()