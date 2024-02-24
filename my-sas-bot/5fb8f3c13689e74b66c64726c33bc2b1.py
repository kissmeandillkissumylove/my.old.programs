import time
import numpy as np
from mss import mss
import pyautogui as pg

monitor = {
		"left": 8,
		"top": 31,
		"width": 640,
		"height": 480,
}

def find_color(our_color, monitor={}):
	m = mss()
	# получение пикселя с экрана монитора
	img = m.grab(monitor)
	# преобразование пикселя в матрицу
	img_arr = np.array(img)
	# Поиск цвета (b, g, r, alpha)
	our_map = (our_color[2], our_color[1], our_color[0], 255)
	indexes = np.where(np.all(img_arr == our_map, axis=-1))
	our_crd = np.transpose(indexes)
	return our_crd


our_color = [164, 164, 164]
while True:
	time1 = time.time()
	result = find_color(our_color, monitor)
	time2 = time.time()
	if result.__len__():
		x = result[0][1] + monitor.get('left')
		y = result[0][0] + monitor.get('top')
		print(time2 - time1, [x, y])
		pg.moveTo(x, y)

    # Ожидание
	time.sleep(3)




























































