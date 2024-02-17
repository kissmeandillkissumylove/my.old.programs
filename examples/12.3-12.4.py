import sys
import pygame
img0name='5fb8f3c13689e74b66c64726c33bc2b1.png'


class SpaceShip:
	# spaceship
	def __init__(self, rocketgame):
		# initializing variables
			# screen
		self.screen = rocketgame.screen
			# get the rectangular area of the surface
		self.screen_rect = rocketgame.screen.get_rect()
			# loads the ship image and gets a rectangle
		self.image = pygame.image.load(img0name)
			# change the image size
		self.image = pygame.transform.scale(self.image, (50, 166))
			# get the rectangular area of the image surfase
		self.rect = self.image.get_rect()
			# image in the center of the window
		self.rect.center = self.screen_rect.center
			# saving the real coordinates of the center of the ship
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
			# movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	def draw_spaceship(self):
		# draw spaceship
			# display the ship on the screen
		self.screen.blit(self.image, self.rect)
	def move_ship(self):
		# move ship
			# the x attribute is updated, not rect.
			# checking that the ship does not go behind the screen
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += 0.3
		if self.moving_left and self.rect.left > 0:
			self.x -= 0.3
		if self.moving_up and self.rect.top > 0:
			self.y -= 0.3
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += 0.3
		# updating the rect attribute based on self.x. and self.y
		self.rect.x = self.x
		self.rect.y = self.y
class RocketGame:
	# game about rocket
	def __init__(self):
		# initializing variables
			# initializing pygame
		pygame.init()
			# screen
		self.screen = pygame.display.set_mode(size=(500, 500))
			# caption
		pygame.display.set_caption("rocket_game")
			# spaceship
		self.spaceship = SpaceShip(self)
	def _check_keydown_events(self, event):
		# check keyboard keystrokes
			# press the right arrow
		if event.key == pygame.K_RIGHT:
			self.spaceship.moving_right = True
			print('\nevent = ', event)
			print('event.type = ', event.type)
			print('event.key = ', event.key)
			# press the left arrow
		elif event.key == pygame.K_LEFT:
			self.spaceship.moving_left = True
			print('\nevent = ', event)
			print('event.type = ', event.type)
			print('event.key = ', event.key)
			# press the ESC
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
			print('\nevent = ', event)
			print('event.type = ', event.type)
			print('event.key = ', event.key)
		elif event.key == pygame.K_UP:
			self.spaceship.moving_up = True
			print('\nevent = ', event)
			print('event.type = ', event.type)
			print('event.key = ', event.key)
		elif event.key == pygame.K_DOWN:
			self.spaceship.moving_down = True
			print('\nevent = ', event)
			print('event.type = ', event.type)
			print('event.key = ', event.key)
	def _check_keyup_events(self, event):
		# reacts to the release of keys
			# release the right arrow
		if event.key == pygame.K_RIGHT:
			self.spaceship.moving_right = False
			print('\nevent = ', event)
			print('event.type = ', event.type)
			print('event.key = ', event.key)
			# release the left arrow
		elif event.key == pygame.K_LEFT:
			self.spaceship.moving_left = False
			print('\nevent = ', event)
			print('event.type = ', event.type)
			print('event.key = ', event.key)
		elif event.key == pygame.K_UP:
			self.spaceship.moving_up = False
			print('\nevent = ', event)
			print('event.type = ', event.type)
			print('event.key = ', event.key)
		elif event.key == pygame.K_DOWN:
			self.spaceship.moving_down = False
			print('\nevent = ', event)
			print('event.type = ', event.type)
			print('event.key = ', event.key)
	def _check_events(self):
		# Handles keystrokes and mouse events
			# a loop for checking events
		for event in pygame.event.get():
				# click the mouse on the cross
			if event.type == pygame.QUIT:
				sys.exit()
				# check keyboard keystrokes
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
				# check the release of keys on the keyboard
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
	def _update_screen(self):
		# updates the images on the screen and displays a new screen
			# the screen is redrawn every time the loop passes.
		self.screen.fill((50, 50, 50))
			# display the ship on the screen
		self.spaceship.draw_spaceship()
			# display the last drawn screen
		pygame.display.flip()
	def run_game(self):
		# run game
		while True:
			self._check_events()
			self.spaceship.move_ship()
			self._update_screen()

if __name__ == '__main__':
	# create an instance and launch the game.
	rg = RocketGame()
	rg.run_game()
