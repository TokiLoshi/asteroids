import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from shots import Shot
from asteroidfield import AsteroidField
import sys


def main():
  pygame.get_init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  Shot.containers = (shots, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    for item in updatable:
      item.update(dt)

      for asteroid in asteroids:
        if asteroid.collides_with(player):
          print("Game over!")
          print("Total score: ", player.score)
          sys.exit()
        for shot in shots:
          if asteroid.collides_with(shot):
            player.score += 1
            print(f"Asteroid destroyed! ☄️ Score: {player.score}")
            asteroid.split()
            shot.kill()

    screen.fill("black")
    
    for item in drawable:
      item.draw(screen)
    
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000
    
    

if __name__ == "__main__":
    main()