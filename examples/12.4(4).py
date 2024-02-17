import sys
import pygame

pygame.init()
print('\npygame.event = ', pygame.event)

screen = pygame.display.set_mode(size=(500, 500))
while True:
	for event in pygame.event.get():
		print('\nevent = ', event)
		print('event.type = ', event.type)
