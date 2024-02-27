import sys
import pygame
import constants5654 as cnst


pygame.init()
screen = pygame.display.set_mode((cnst.WIN_SIZE))
pygame.display.set_caption(cnst.CAPTION)
pygame.display.set_icon(pygame.image.load(cnst.ICON))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)



wid, hei = 0, 0
R, G, B = 0, 0, 0
rect_x = 100
rect_y = 200
speed = 2
pos = [0, 0]
s_x = 10
s_y = 20
rec = [0, 0]
rect_move_left = rect_move_right = False
rect_move_up = rect_move_down = False
s_m = s_p = False
start_draw = False


rungame = True
while rungame:


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			rungame = False

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print(f'pressed {event.key} button')
				rect_move_left = True

			elif event.key == pygame.K_RIGHT:
				print(f'pressed {event.key} button')
				rect_move_right = True

			elif event.key == pygame.K_UP:
				print(f'pressed {event.key} button')
				rect_move_up = True

			elif event.key == pygame.K_DOWN:
				print(f'pressed {event.key} button')
				rect_move_down = True

			elif event.key == pygame.K_EQUALS:
				s_p = True

			elif event.key == pygame.K_MINUS:
				s_m = True

			elif event.key == pygame.K_u:
				if R in range(0, 250):
					R += 5

			elif event.key == pygame.K_j:
				if R in range(5, 255):
					R -= 5

			elif event.key == pygame.K_i:
				if G in range(0, 250):
					G += 5

			elif event.key == pygame.K_k:
				if G in range(5, 255):
					G -= 5

			elif event.key == pygame.K_o:
				if B in range(0, 250):
					B += 5

			elif event.key == pygame.K_l:
				if B in range(5, 255):
					B -= 5

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				print(f'released {event.key} button')
				rect_move_left = False

			elif event.key == pygame.K_RIGHT:
				print(f'released {event.key} button')
				rect_move_right = False

			elif event.key == pygame.K_UP:
				print(f'released {event.key} button')
				rect_move_up = False

			elif event.key == pygame.K_DOWN:
				print(f'released {event.key} button')
				rect_move_down = False

			elif event.key == pygame.K_EQUALS:
				s_p = False

			elif event.key == pygame.K_MINUS:
				s_m = False

		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			start_draw = True
			rec = event.pos

		elif event.type == pygame.MOUSEMOTION:
			pos = list(event.pos)
			print(f'mouse pos: {pos}')

			if start_draw:
				dr_rec = event.pos
				wid = dr_rec[0] - rec[0]
				hei = dr_rec[1] - rec[1]

				pygame.display.update()

		elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			start_draw = False


	if rect_move_left: rect_x -= speed
	if rect_move_right: rect_x += speed
	if rect_move_up: rect_y -= speed
	if rect_move_down: rect_y += speed
	if s_m:
		s_x -= 1
		s_y -= 1
	if s_p:
		s_x += 1
		s_y += 1


	screen.fill(cnst.WBLUE)
	pygame.draw.rect(screen, cnst.WGREEN, (pos[0], pos[1], s_x, s_y))
	pygame.draw.rect(screen, [R, G, B], (rect_x, rect_y, s_x, s_y))
	pygame.draw.rect(screen, cnst.RED,
	                 (rec[0], rec[1], wid, hei))


	if pygame.mouse.get_focused():
		kek = pygame.mouse.get_pos()
		pygame.draw.circle(screen, cnst.BLUE, kek, 7)


	pygame.display.update()


	clock.tick(cnst.FPS)
