PTH0 = 'c://Users//KISS//Documents//dont_delete!!!.txt'
MENU = '-----1. exit\n' + '-----2. add new word\n' + \
	'-----3. find word\n'
###
###
###
def prt_lne():
	print('_' * 20)
###
###
def main():

	while True:

		prt_lne()
		print(MENU)
		prt_lne()

		ans = input('-----choose action: ')

		if ans == '1':

			break

		if ans == '2':

			fle0 = open(PTH0, 'a+')
			ans = input('-----enter ur word: ')
			ans += '-'
			ans += input('-----enter the translation: ')
			ans += '\n'
			fle0.write(ans)
			fle0.close()

		if ans == '3':

			ans = input('-----enter ur word: ')
			fle0 = open(PTH0, 'r')
			got_fle0 = fle0.readlines()
			for elt in got_fle0:
				elt = elt.split('-')
				if elt[0] == ans:
					print(elt[0] + '-' + elt[1])
			fle0.close()
###
###
###
if __name__ == '__main__':
	main()
###
###
###
# r - открывает файл только для чтения,
# w - открыт для записи (перед записью файл будет очищен),
# x - эксклюзивное создание, бросается исключение FileExistsError, если
#     файл уже существует.
# a - открыт для добавления в конец файла (на некоторых Unix-системах пи
#     шет в конец файла вне зависимости от позиции курсора)
# + - символ обновления (чтение + запись).
# t - символ текстового режима.
# b - символ двоичного режима (для операционных систем, которые различаю
#     т текстовые и двоичные файлы).
#
#
#
# Варианты использования режимов:
# 'r' - Открывает файл только для чтения. Указатель файла помещается в н
#       ачале файла. Это режим "по умолчанию".
# 'rb' - Открывает файл в бинарном режиме только для чтения. Указатель ф
#        айла помещается в начале файла. Это режим "по умолчанию".
# 'r+' - Открывает файл для чтения и записи. Указатель файла помещается
#        в начало файла.
# 'rb+' - Открывает файл в бинарном режиме для чтения и записи. Указател
#         ь файла помещается в начале файла. Это режим "по умолчанию".
# 'w' - Открывает файл только для записи. Перезаписывает файл, если файл
#       существует. Если файл не существует, создает новый файл для запи
#       си.
# 'wb' - Открывает файл в бинарном режиме только для записи. Перезаписыв
#        ает файл, если файл существует. Если файл не существует, создае
#        т новый файл для записи.
# 'w+' - Открывает файл для записи и чтения. Перезаписывает существующий
#        файл, если файл существует. Если файл не существует, создается
#        новый файл для чтения и записи.
# 'wb+' - Открывает файл в бинарном режиме для записи и чтения. Перезапи
#         сывает существующий файл, если файл существует. Если файл не с
#         уществует, создается новый файл для чтения и записи.
# 'a' - Открывает файл для добавления. Указатель файла находится в конце
#       файла, если файл существует. То есть файл находится в режиме доб
#       авления. Если файл не существует, он создает новый файл для запи
#       си.
# 'ab' - Открывает файл в бинарном режиме для добавления. Указатель файл
#        а находится в конце файла, если файл существует. То есть файл н
#        аходится в режиме добавления. Если файл не существует, он созда
#        ет новый файл для записи.
# 'a+' - Открывает файл для добавления и чтения. Указатель файла находит
#        ся в конце файла, если файл существует. Файл открывается в режи
#        ме добавления. Если файл не существует, он создает новый файл д
#        ля чтения и записи.
# 'ab+' - Открывает файл в бинарном режиме для добавления и чтения. Указ
#         атель файла находится в конце файла, если файл существует. Фай
#         л открывается в режиме добавления. Если файл не существует, он
#         создает новый файл для чтения и записи.