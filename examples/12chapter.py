# 12.1
'''
import sys
import pygame

class BlueWindow():
	# класс для отрисовки окна

	def __init__(self):
		# инициализация
		
		pygame.init()
		self.screen = pygame.display.set_mode((500, 500))
		self.bg_color = (100, 0, 255)
		
	def run_window(self):
		# запуск окна
		
		while True:
			# обрабатывает нажатия клавиш и события мыши
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
			# При каждом проходе цикла перерисовывается экран.
			self.screen.fill(self.bg_color)
			
			# Отображение последнего прорисованного экрана.
			pygame.display.flip()


if __name__ == '__main__':
	# создание экземпляра и запуск окна
	
	window1 = BlueWindow()
	window1.run_window()
'''

# 12.2
import sys
import pygame

class Character():
	"""Класс для управления кораблем."""
		
	def __init__(self, ai_game):
		"""Инициализирует корабль и задает его начальную позицию."""
			
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
			
		# Загружает изображение корабля и получает прямоугольник.
		self.image = pygame.image.load('char.png')
		self.image = pygame.transform.scale(self.image, (180, 98))
		self.rect = self.image.get_rect()
		
		# Каждый новый корабль появляется у нижнего края экрана.
		self.rect.center = self.screen_rect.center

	def blitme(self):
		"""Рисует корабль в текущей позиции."""
	
		self.screen.blit(self.image, self.rect)

class BlueWindow():
	# класс для отрисовки окна

	def __init__(self):
		# инициализация
		
		pygame.init()
		self.screen = pygame.display.set_mode((500, 500))
		self.bg_color = (100, 0, 255)
		self.character = Character(self)
		
	def run_window(self):
		# запуск окна
		
		while True:
			# обрабатывает нажатия клавиш и события мыши
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
			# При каждом проходе цикла перерисовывается экран.
			self.screen.fill(self.bg_color)
			self.character.blitme()
			
			# Отображение последнего прорисованного экрана.
			pygame.display.flip()


if __name__ == '__main__':
	# создание экземпляра и запуск окна
	
	window1 = BlueWindow()
	window1.run_window()
