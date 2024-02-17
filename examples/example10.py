##
## 1
'''
class F():
	def _print(self):
		print('func _print F')


class G(F):
	def _print(self):
		super()._print()
		print('func _print G')



if __name__ == '__main__':
	elt = G()
	elt._print()
	print()
	elt0 = F()
	elt0._print()
'''
##
## 2
'''
class PC():
	def __init__(self, computer, ram, ssd):
		self.computer = computer
		self.ram = ram
		self.ssd = ssd


class Laptop(PC):
	def __init__(self, computer, ram, ssd, model):
		super().__init__(computer, ram, ssd)
		self.model = model



if __name__ == '__main__':
	elt = Laptop('Lenovo', 2, 512, 1420)
	print('this pc is: {}'.format(elt.computer))
	print('this pc has: {} ram'.format(elt.ram))
	print('this pc has: {} ssd'.format(elt.ssd))
	print('this pc has this model: {}'.format(str(elt.model)))
'''
##
## 3
'''
from typing import NoReturn

class Rectangle:
	def __init__(self, length: int, width: int) -> NoReturn:
		self.length = length
		self.width = width
	def area(self):
		return self.length * self.width
	def perimeter(self):
		return 2 * self.length + 2 * self.width

class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)
			
			

if __name__ == '__main__':
	elt = Square(2)
	print(elt.area(), elt.perimeter())
	elt = Rectangle(2, 4)
	print(elt.area(), elt.perimeter())
'''
##
## 4

class N():
	def __init__(self):
		print('init class N')
	def method_a(self, a):
		print('its method_a from class N: ', a)

class M(N):
	def __init__(self):
		print('init class M')
		super().__init__()
	def method_a(self, a):
		print('its method_a from class M: ', a)
		super().method_a(a + 1)

class K(M):
	def __init__(self):
		print('init class K')
		super().__init__()
	def method_a(self, a):
		print('its method_a from class K: ', a)
		super().method_a(a + 1)
		
class U(K):
	def __init__(self):
		print('init class U')
		super().__init__()
	def method_a(self, a):
		print('its method_a from class U: ', a)
		super().method_a(a + 1)



if __name__ == '__main__':
	elt = U()
	elt.method_a(1)
