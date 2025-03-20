import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from aseriodfield import *
from circleshape import *

import sys

def main():
    pygame.init()
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
clock = pygame.time.Clock()
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()


Shot.containers = (shots,updatable, drawable)
AsteroidField.containers = (updatable)
Asteroid.containers = (asteroids, updatable, drawable)
Player.containers = (updatable, drawable)
player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
asteroid_fields = AsteroidField()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    updatable.update(dt)
    for i in asteroids:
        if i.collison(player):
            print('Game over!')
            # sys.exit(0)

    screen.fill('black')
    for obj in drawable:
        obj.draw(screen)
    
    pygame.display.flip()
    dt += clock.tick(60) / 1000
    
if __name__ == '__main__':
    main()

