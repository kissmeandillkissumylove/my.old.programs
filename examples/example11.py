from os.path import join
S7 = '\u26e7'

class FileObject:
	# Обёртка для файлового объекта, чтобы быть уверенным в том, что
	# файл будет закрыт при удалении.

	def __init__(self, path0='~', filename0='example11.txt'):
		# открыть файл filename в filepath в режиме чтения и записи
		self.file0 = open(join(path0, filename0), 'r+')

	def __del__(self):
		self.file0.close()
		del self.file0

#_______________________________________________________________________

class Word(str):
    # Класс для слов, определяющий сравнение по длине слов

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            # Теперь Word это все символы до первого пробела
            word = word[:word.index(' ')]
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

#_______________________________________________________________________

class Nn:
	# __str__ и __repr__ — оба методы для получения строкового представл
	# ения объекта.
	#
	# __str__ это должен быть короткий и более user-friendly.
	# __repr__ вывод более подробной инфы (как они будут показываться в
	# системе).
	#
	# Если определен __str__, то обращение к нему, а если определен __re
	# pr__ то обрщение к __repr__.

	def __init__(self, name, size):
		self.name = name
		self.size = size

	def __str__(self):
		return 'class Nn\u26e7 {}\u26e7 {}'.format(self.name, self.size)

	def __repr__(self):
		return f'{S7}class {Nn.__name__}{S7}id {id(Nn)}{S7}'


class Vector:

	def __init__(self, *args):
		self.values = list(args)

	def __repr__(self):
		return str(self.values)

	def __getitem__(self, item):
		if 0 <= item <= len(self.values):
			return self.values[item]
		else:
			raise IndexError('1')

	def __setitem__(self, key, value):
		if 0 <= key <= len(self.values):
			self.values[key] = value
		elif key > len(self.values):
			diff = key - len(self.values) + 1
			self.values.extend([None]*diff)
			self.values[key] = value
		else:
			raise IndexError('2')

	def __delitem__(self, key):
		if 0 <= key < len(self.values):
			del self.values[key]
		else:
			raise IndexError('3')


if __name__ == '__main__':

	r = Nn('nnn', 3354)
	print(r)

	s = Vector(516,54,66656,568,59,60,645)
	print(s)
	print(s[1], s[6], s[3])
	s[20] = 5000
	print(s)
	for elt in range(1, 14):
		del s[7]
	print(s)