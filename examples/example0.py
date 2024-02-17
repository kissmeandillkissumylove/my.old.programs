import pygame
import sys

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))
r = 30
x = 0 - r
y = WIN_HEIGHT // 2
 
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
				
	sc.fill((50, 50, 150))
	pygame.draw.circle(sc, ORANGE, (x, y), r, width = 6)
	pygame.display.update()
	
	if x >= WIN_WIDTH + r:
		x = 0 - r
	else:
		x += 1
	
	clock.tick(FPS)
