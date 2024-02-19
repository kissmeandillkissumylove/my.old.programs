import sys
import pygame

HEIGH365 = 600
WIDTH365 = 500

class Background365(pygame.sprite.Sprite):
	def __init__(self, image_file, location):
		pygame.sprite.Sprite.__init__(self)								# ...
		self.image = pygame.image.load(image_file)
		self.image = pygame.transform.scale(
			self.image, (WIDTH365, HEIGH365))
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

class Game365():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode([WIDTH365, HEIGH365])
		pygame.display.set_caption('game365')
		self.background = Background365('456554645.png', [0,0])

	def check_events365(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					print('ESC', end = ' ')
					sys.exit()
					
	def run_game365(self):
		while True:
			self.check_events365()
			self.screen.fill([214, 65, 65])
			self.screen.blit(
				self.background.image, self.background.rect)			# ...
			

				
			pygame.display.flip()


if __name__ == '__main__':
	game0 = Game365()
	game0.run_game365()
	







'''
pygame.draw.line(surface = self.screen, color = (214, 65, 65),
	start_pos = (0, 0), end_pos = (200, 200),
	width = 1)
	
pygame.draw.rect(surface = self.screen, color = (214, 65, 65),
	rect = (20, 20, 200, 40), width = 5)
	
pygame.draw.aaline(surface = self.screen, color = (255, 255, 255), 
	start_pos = [10, 70], end_pos = [290, 55])
	
pygame.draw.lines(surface = self.screen, color = (255, 255, 255),
	closed = True, points = ((0, 0), (200, 200), (300, 100)),
	width = 1)
	
pygame.draw.aalines(surface = self.screen, color = (255, 255, 255),
	closed = True, points = ((0, 0), (200, 200), (300, 100)))
	
pygame.draw.polygon(surface = self.screen, color = (255, 255, 255),
	points = [[150, 10], [180, 50], [90, 90], [30, 30]])
	
pygame.draw.circle(surface = self.screen, color = (200, 200, 200),
	center = (250, 300), radius = 20,
	width = 5, draw_top_right = True)
	
pygame.draw.ellipse(surface = self.screen, color = (150, 200, 50),
	rect = (20, 200, 220, 120), width = 1)
	
pygame.draw.arc(surface = self.screen,
	color = (150, 200, 50), rect = (0, 0, 500, 600),
	start_angle = 0, stop_angle = 3.14,
	width = 32)



























'''
