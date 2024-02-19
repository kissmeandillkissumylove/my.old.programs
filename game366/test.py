import sys
import pygame
from math import pi

WIN_WIDTH = 300
WIN_HEIGH = 300
WIN_COLOR = (50, 50, 50)
SIDE1_COLOR = (225, 0, 0)
SIDE2_COLOR = (255, 76, 76)
SIDE3_COLOR = (170, 0, 0)

class Parallelepiped():
	
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGH))
		# right side
		self.s1x1, self.s1y1 = 40, 10
		self.s1x2, self.s1y2 = 40, 60
		self.s1x3, self.s1y3 = 10, 80
		self.s1x4, self.s1y4 = 10, 30
		# left side
		self.s2x1, self.s2y1 = 70, 30
		self.s2x2, self.s2y2 = 70, 80
		self.s2x3, self.s2y3 = 40, 60
		self.s2x4, self.s2y4 = 40, 10
		# bottom side
		self.s3x1, self.s3y1 = 70, 80
		self.s3x2, self.s3y2 = 40, 100
		self.s3x3, self.s3y3 = 10, 80
		self.s3x4, self.s3y4 = 40, 60
	
	def _draw_side1(self):
		pygame.draw.polygon(surface = self.screen, color = SIDE1_COLOR,
			points = ([self.s1x1, self.s1y1], [self.s1x2, self.s1y2],
				[self.s1x3, self.s1y3], [self.s1x4, self.s1y4]))
		pygame.draw.aalines(surface = self.screen, color = SIDE1_COLOR,
			closed = True,
			points = ([self.s1x1, self.s1y1], [self.s1x2, self.s1y2],
				[self.s1x3, self.s1y3], [self.s1x4, self.s1y4]))
			
	def _draw_side2(self):
		pygame.draw.polygon(surface = self.screen, color = SIDE2_COLOR,
			points = ([self.s2x1, self.s2y1], [self.s2x2, self.s2y2],
				[self.s2x3, self.s2y3], [self.s2x4, self.s2y4]))
		pygame.draw.aalines(surface = self.screen, color = SIDE2_COLOR,
			closed = True,
			points = ([self.s2x1, self.s2y1], [self.s2x2, self.s2y2],
				[self.s2x3, self.s2y3], [self.s2x4, self.s2y4]))
			
	def _draw_side3(self):
		pygame.draw.polygon(surface = self.screen, color = SIDE3_COLOR,
			points = ([self.s3x1, self.s3y1], [self.s3x2, self.s3y2],
				[self.s3x3, self.s3y3], [self.s3x4, self.s3y4]))
		pygame.draw.aalines(surface = self.screen, color = SIDE3_COLOR,
			closed = True,
			points = ([self.s3x1, self.s3y1], [self.s3x2, self.s3y2],
				[self.s3x3, self.s3y3], [self.s3x4, self.s3y4]))
			
	def _draw_parallelepiped(self):
		self._draw_side2()
		self._draw_side1()
		self._draw_side3()
		
	def _move_parallelepiped_right(self):
			# right side
			self.s1x1 += 1
			self.s1y1 += 1
			self.s1x2 += 1
			self.s1y2 += 1
			self.s1x3 += 1
			self.s1y3 -= 1
			self.s1x4 += 1
			self.s1y4 -= 1
			# left side
			self.s2x1 -= 1
			self.s2x2 -= 1
			self.s2x3 += 1
			self.s2y3 += 1
			self.s2x4 += 1
			self.s2y4 += 1
			# bottom side
			self.s3x2 -= 1
			self.s3y2 -= 1
			self.s3x4 += 1
			self.s3y4 += 1
		
	def _move_parallelepiped_left(self):
		# right side
			self.s1x1 -= 1
			self.s1y1 -= 1
			self.s1x2 -= 1
			self.s1y2 -= 1
			self.s1x3 -= 1
			self.s1y3 += 1
			self.s1x4 -= 1
			self.s1y4 += 1
			# left side
			self.s2x1 += 1
			self.s2x2 += 1
			self.s2x3 -= 1
			self.s2y3 -= 1
			self.s2x4 -= 1
			self.s2y4 -= 1
			# bottom side
			self.s3x2 += 1
			self.s3y2 += 1
			self.s3x4 -= 1
			self.s3y4 -= 1
			
	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
				elif event.key == pygame.K_RIGHT:
					self._move_parallelepiped_right()
				elif event.key == pygame.K_LEFT:
					self._move_parallelepiped_left()

	def _run_screen(self):
		while True:
			self._check_events()
			self.screen.fill(WIN_COLOR)
			self._draw_parallelepiped()
			pygame.display.flip()



if __name__ == '__main__':
	screen = Parallelepiped()
	screen._run_screen()
