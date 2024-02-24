import cv2


def view_image(image, name_of_window, x, ex, y, ey):
	# example:
	# my_image = cv2.imread('./imgdata/0.bmp')
	# my_image = my_image[0:480, 0:640]
	# view_image(my_image, 'window_name')
	cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
	cv2.imshow(name_of_window, image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()














img = cv2.imread('./imgdata/0.bmp')
scale_percent = 32 # Процент от изначального размера
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
view_image(resized, "После изменения размера на 20 %")






















