STR = 'string:'
NUM = 'number:'
LST = 'list:'
DIC = 'dictionary:'
TUP = 'tuple:'
SET = 'set:'
BOO = 'bool:'
TCH = 'type checking:'
BDS = 'basics of Data sorting:'

#_______________________________________________________________________
# number: int(), bin(), round(), hex(), str(),

# rounding
print(NUM, round(10/3, 2), round(10/3, 5))
# Функция int() позволяет выполнять конвертацию в тип int.
# Во втором аргументе можно указывать систему счисления:
print(NUM, int('11', 2), int('20', 16))
# Конвертация в int типа float
print(NUM, int(3.333), int(3.9))
# bin позволяет получить двоичное представление числа (ret - строка)
print(NUM, bin(8), bin(255), bin(int(16/2)))
# hex шестнадцатеричное значение
print(NUM, hex(32), hex(10))
# несколько преобразований одновременно
print(NUM, int('ff', 16), bin(int('ff', 16)))

print()
#_______________________________________________________________________
# string: find(), replace(), split(), len(), startswith(), endswith(),
#         join(), upper(), lower(), swapcase(), capitalize(), title(),
# 		  istitle(), count(), strip(), lstrip(), rstrip(), format(),

ret, str = 'ret', 'str'
ret += str
# если подстрока найдена, метод вернёт позицию её первого элемента,
# если нет — вернёт -1
print(STR, ret, ret.find('ts'), ret.find('tsf'))
# поиск подстроки с заменой, заменим skill на school
print(STR, ret.replace('ts', 'aa'), ret)
# разбить строку по разделителю
ret = 'n_g_h_t'
print(STR, ret.split('_'))
# example
ret = '''
...: text
...: more text here
...: much more txt here'''
print(STR, ret)
# Строку можно умножать на число
ret = 'python'
print(STR, ret*2, ret[0], ret[5], ret[-1], ret[1:4])
# срезы можно делать с 'шагом'
ret = '0123456789'
print(STR, ret, ret[1::2], ret[::2], ret[::3])
# Срезы можно использовать для получения строки в обратном порядке
print(STR, ret[::], ret[:], ret[::-1])
# len()
print(STR, len(ret))
# str.startswith(prefix[, start[, end]]) -> bool
# Методам startswith() и endswith() можно передавать несколько значений
# (обязательно как кортеж)
ret, a, b = 'python', 'th', 'on'
print(STR, ret.startswith(a, 0, -1), ret.startswith(a, 2, -1))
# Для определения постфикса в строке используйте str.endswith().
print(STR, ret.endswith(b, 3, -1), ret.endswith(b))
# Метод join
values = ['10', '20', '30']
print(STR, ','.join(values))
# работа с регистром
ret = 'FastPython'
print(STR, ret.upper(), ret.lower(), ret.swapcase())
ret = 'fast python'
print(STR, ret.capitalize(), ret.title())
print(STR, ret.istitle(), end=' ')
ret = 'Fast Python'
print(ret.istitle())
# count()
ret = 'pythoniscool'*3
print(STR, ret, ret.count('python'), ret.count('o'))
# strip()
ret = '\tpython\t'
print(STR, ret, ret.strip(), ret.lstrip(), ret.rstrip())
# По умолчанию метод strip() убирает пробельные символы.
# В этот набор символов входят: \t\n\r\f\v
# Методу strip можно передать как аргумент любые символы.
# Тогда в начале и в конце строки будут удалены все символы,
# которые были указаны в строке:
ret = '[]]]p[y]t]hon[][][][[[[['
print(STR, ret, ret.strip('[]'))
# format()
print(STR, 'python {}.{}.{} version for {}'.format(3, 10, 9, 'win10'))
# выравниванием по правой стороне
ret1, ret2, ret3 = ['100', 'aabb.cc80.7000', 'Gi0/1']
print(STR, "{:>15} {:>15} {:>15}".format(ret1, ret2, ret3))
# Выравнивание по левой стороне:
print(STR, "{:15} {:15} {:15}".format(ret1, ret2, ret3))
# https://pyneng.readthedocs.io/ru/latest/book/04_data_structures/string_format.html
# Например, можно указать, сколько цифр после запятой выводить:
print(STR, "{:.5f}".format(10/3))
# конвертировать числа в двоичный формат:
print(STR, '{:b} {:b} {:b} {:b}'.format(192, 100, 1, 1))
# При этом по-прежнему можно указывать дополнительные параметры,
# например, ширину столбца:
print(STR, '{:8b} {:8b} {:8b} {:8b}'.format(192, 100, 1, 1))
# А также можно указать, что надо дополнить числа нулями:
print(STR, '{:08b} {:08b} {:08b} {:08b}'.format(192, 100, 1, 1))
#
print(STR, '{ip}/{mask}'.format(mask=24, ip='10.1.1.1'))
print(STR, '{1}/{0}'.format(24, '10.1.1.1'))
# пример оптимизации
ip_template = '''
\tIP address:
\t{:<8} {:<8} {:<8} {:<8}
\t{:08b} {:08b} {:08b} {:08b}
'''
print(STR, ip_template.format(192, 100, 1, 1, 192, 100, 1, 1).rstrip())
ip_template = '''
\tIP address:
\t{0:<8} {1:<8} {2:<8} {3:<8}
\t{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(STR, ip_template.format(192, 100, 1, 1).rstrip())
# Объединение литералов строк
ret = ('Python'
       '3.10.9')
print(STR, ret)

print()
#_______________________________________________________________________
# list: list(), reverse(), sorted(), append(), extend(), pop(),
# 		 remove(), index(), insert(), sort(), zip(),

# Создание списка с помощью функции list():
ret = 'Python'
ret = list(ret)
print(LST, ret)
print(LST, ret[1::], ret[-1], ret[::-1])
# reverse()
print(LST, ret.reverse(), ret)
ret = [['P'], ['y'], ['t'], ['h'], ['o'], ['n']]
print(LST, ret, ret[0], ret[0][0], len(ret), len(ret[0]))
# sorted()
print(LST, sorted(ret))
ret = ['P', 'y', 't', 'h', 'o', 'n']
print(LST, sorted(ret))
# extend()
vlans, vlans2 = ['10', '20', '30', '100-200'], ['300', '400', '500']
vlans.extend(vlans2)
print(LST, vlans)
vlans, vlans2 = ['10', '20', '30', '100-200'], ['300', '400', '500']
vlans += vlans2
print(LST, vlans)
# Без указания номера удаляется последний элемент списка. (pop())
# remove - удаление эл-та по значению
# Метод index используется для того, чтобы проверить, под каким
# номером в списке хранится элемент:
print(LST, vlans.index('400'))
vlans.insert(1, '15')
print(LST, vlans)
# сортировка
vlans.sort()
print(LST, vlans)
# list comprehensions:
items = ['10', '20', 'a', '30', 'b', '40']
only_digits = []
for item in items:
    if item.isdigit():
        only_digits.append(int(item))
print(LST, only_digits)
# same example with using list complecations
items = ['10', '20', 'a', '30', 'b', '40']
only_digits = [int(item) for item in items if item.isdigit()]
print(LST, only_digits)
# next example
vlans = [[10, 21, 35], [101, 115, 150], [111, 40, 50]]
result = [vlan for vlan_list in vlans for vlan in vlan_list]
print(LST, result)
# next example
vlans, names = [100, 110, 150, 200], ['mngmt', 'voice', 'video', 'dmz']
ret = ['vlan {}\t name {}'.format(vlan, name) for vlan, name in zip(vlans, names)]
print(LST, '\n\t  '.join(ret))

print()
#_______________________________________________________________________
# dictionary: clear(), copy(), get(), setdefault(), keys(), values(),
#             items(), del(), update(), dict(), dict.fromkeys(),

# Получить значения из вложенного словаря: dictionary['key1']['key2']
#
# Функция sorted сортирует ключи словаря по возрастанию и возвращает
# новый список с отсортированными ключами:
dic = { 'first'  : 1,
        'second' : 2,
        'third'  : 3,
        'aa'     : 0,
        }
print(DIC, sorted(dic))
# get()
print(DIC, dic.get('ios'), dic.get('first'), dic.get('ios', 'nothing'))
# setdefault()
dic.setdefault('ios')
print(DIC, dic)
print(DIC, dic.setdefault('second'))
dic.setdefault('model', 'Cisco3580')
print(DIC, dic)
# keys, values, items
# Все три метода возвращают специальные объекты view, которые отображают
# ключи, значения и пары ключ-значение словаря соответственно.
# Очень важная особенность view заключается в том, что они меняются
# вместе с изменением словаря. И фактически они лишь дают способ
# посмотреть на соответствующие объекты, но не создают их копию.
print(DIC, dic.keys())
print(DIC, dic.values())
print(DIC, dic.items())
# https://pyneng.readthedocs.io/ru/latest/book/04_data_structures/dict_methods.html#setdefault
# del()
del dic['first']
print(DIC, dic)
# Метод update позволяет добавлять в словарь содержимое другого словаря
r1 = {'name': 'London1', 'location': 'London Str'}
r1.update({'vendor': 'Cisco', 'ios':'15.2'})
print(DIC, r1)
r1.update({'name': 'london-r1', 'ios':'15.4'})
print(DIC, r1)
# Конструктор dict позволяет создавать словарь несколькими способами.
r1 = dict(model='4451', ios='15.4')
print(DIC, r1)
r1 = dict([('model', '4451'), ('ios', '15.4')])
print(DIC, r1)
# В ситуации, когда надо создать словарь с известными ключами,
# но пока что пустыми значениями (или одинаковыми значениями),
# очень удобен метод fromkeys():
d_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
r1 = dict.fromkeys(d_keys)
print(DIC, r1)
# Но можно указывать и свой вариант значения:
router_models = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']
models_count = dict.fromkeys(router_models, 0)
print(DIC, models_count)
# Этот вариант создания словаря подходит не для всех случаев.
# Например, при использовании изменяемого типа данных в значении,
# будет создана ссылка на один и тот же объект:
router_models = ['ISR2811', 'ISR2911', 'ISR2921', 'ASR9002']
routers = dict.fromkeys(router_models, [])
print(DIC, routers)
routers['ASR9002'].append('london_r1')
print(DIC, routers)
# Для такой задачи лучше подходит dict comprehensions
# С помощью генератора списка также удобно получать элементы
# из вложенных словарей:
london_co = {
    'r1' : {
    'hostname': 'london_r1',
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'hostname': 'london_r2',
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'hostname': 'london_sw1',
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101'
    }
}
ret = [london_co[device]['ios'] for device in london_co]
print(DIC, ret)
ret = [london_co[device]['ip'] for device in london_co]
print(DIC, ret)
# dict comprehensions
print(DIC, {num: num**2 for num in range(1, 11)})
# вариант с помощью генератора словаря:
r1 = {
    'iOs'      : '15.4',
    'ip'       : '10.255.0.1',
    'hOstname' : 'london_r1',
    'loCation' : '21 New Globe Walk',
    'modeL'    : '4451',
    'venDOR'   : 'Cisco'}
lower_r1 = {key.lower(): value for key, value in r1.items()}
print(DIC, lower_r1)
# next
london_co = {
    'r1' : {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor'  : 'Cisco',
        'model'   : '4451',
        'ios'     : '15.4',
        'ip'      : '10.255.0.1'
    },
    'r2' : {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor'  : 'Cisco',
        'model'   : '4451',
        'ios'     : '15.4',
        'ip'      : '10.255.0.2'
    },
    'sw1' : {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor'  : 'Cisco',
        'model'   : '3850',
        'ios'     : '3.6.XE',
        'ip'      : '10.255.0.101'
    }
}
result = {device: {key.upper(): value for key, value in params.items()}
          for device, params in london_co.items()}
print(DIC, result)

print()
#_______________________________________________________________________
# tuple: tuple()

# Кортеж из одного элемента (обратите внимание на запятую):
tup0 = ('password',)
# tuple by list
list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
tuple_keys = tuple(list_keys)
print(TUP, tuple_keys)
# Функция sorted сортирует элементы кортежа по возрастанию и возвращает
# новый список с отсортированными элементами:

print()
#_______________________________________________________________________
# set(), add(), discard(), clear(), union(), intersection()

# Метод add() добавляет элемент во множество
set1 = {10, 20, 30, 40}
set1.add(50)
print(SET, set1)
# Метод discard() позволяет удалять элементы, не выдавая ошибку,
# если элемента в множестве нет:
set1.discard(55)
set1.discard(50)
print(SET, set1)
# Метод clear() очищает множество
set1.clear()
print(SET, set1)
# Объединение множеств и оператор |
vlans1, vlans2 = {10, 20, 30, 50, 100}, {100, 101, 102, 200}
print(SET, vlans1.union(vlans2))
print(SET, (vlans1 | vlans2))
# Пересечение множеств
print(SET, vlans1.intersection(vlans2))
print(SET, vlans1 & vlans2)
# Нельзя создать пустое множество с помощью литерала (так как в таком
# случае это будет не множество, а словарь):
set1 = {}
print(SET, type(set1))
set2 = set()
print(SET, type(set2))
# Множество из строки и списка
print(SET, set('long long long long string'),
      set([10, 20, 30, 10, 10, 30]))

print()
#_______________________________________________________________________
# bool()

# истинное значение: любое ненулевое число, любая непустая строка,
# любой непустой объект
# ложное значение: 0, None, пустая строка, пустой объект
items, empty_list = [1, 2, 3], []
print(BOO, bool(empty_list), bool(items), bool(0), bool(1))


print()
#_______________________________________________________________________
# type checking: isdigit(), isalpha(), isalnum(), type()

print(TCH, "a".isdigit(), "a10".isdigit(), "10".isdigit())
# Метод isalpha позволяет проверить, состоит ли строка из одних букв
print(TCH, "a".isalpha(), "a100".isalpha(), "a--  ".isalpha())
print(TCH, "a ".isalpha())
# Метод isalnum позволяет проверить, состоит ли строка из букв или цифр
print(TCH, "a".isalnum(), "a10".isalnum())
# type
print(TCH, type("string"), type("string") == str)
print(TCH, type((1,2,3)))
# Вызов методов цепочкой
line = "switchport trunk allowed vlan 10,20,30"
vlans = line.split()[-1].split(",")
print(TCH, vlans)

print()
#_______________________________________________________________________
# basics of Data sorting: sorted()

# При сортировке данных типа списка списков или списка кортежей,
# sorted сортирует по первому элементу вложенных списков (кортежей),
# а если первый элемент одинаковый, по второму:
data = [[1, 100, 1000], [2, 2, 2], [1, 2, 3], [4, 100, 3]]
print(BDS, sorted(data))
vlans = ['1', '30', '11', '3', '10', '20', '30', '100']
print(BDS, sorted(vlans))
ip_list = ["10.1.1.1", "10.1.10.1", "10.1.2.1", "10.1.11.1"]
print(BDS, sorted(ip_list))

# https://pyneng.readthedocs.io/ru/latest/book/04_data_structures/further_reading.html

print()
#_______________________________________________________________________
# open()

ret = open('python.txt', 'w')
ret.write('1t1t1t\n')
ret.write('2b2b2b\n')
ret.close()
ret = open('python.txt', 'r')
ret = ret.read()
print(ret.rstrip(), end='\n\n')

# https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-open/

print()
#_______________________________________________________________________
# задания

# 1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

print(nat[:40] + 'GigabitEthernet' + nat[52:])

print(nat.replace('FastEthernet', 'GigabitEthernet'))
# 2
mac = "AAAA:BBBB:CCCC"

print('.'.join(mac.split(':')))

print(mac.replace(':', '.'))
# 3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
print(config.split()[-1].split(','))
print(int(i)**2 for i in config.split()[-1].split(','))
print([int(i)**2 for i in config.split()[-1].split(',')])
# 4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(sorted(set(vlans)))
# 5
c1 = "switchport trunk allowed vlan 1,2,3,5,8"
c2 = "switchport trunk allowed vlan 1,3,8,9"
print(list(set(c1.split()[-1].split(',')) &
           set(c2.split()[-1].split(','))))
# 6
o = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
o = o.replace('[', '').replace(']', '').replace(',', '').split()
n1, n2, n3 = 'Prefix', 'AD/Metric', 'Next-Hop'
n4, n5 = 'Last update', 'Outbound Interface'
print('''
{0:<22}{5[0]}
{1:<22}{5[1]}
{2:<22}{5[3]}
{3:<22}{5[4]}
{4:<22}{5[5]}
'''.format(n1, n2, n3, n4, n5, o))

o = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
print('''
{0:<22}{5[0]}
{1:<22}{5[1]}
{2:<22}{5[3]}
{3:<22}{5[4]}
{4:<22}{5[5]}
'''.format('Prefix', 'AD/Metric', 'Next-Hop', 'Last update',
      'Outbound Interface',
        o.replace('[', '').replace(']', '').replace(',', '').split()))
# 7
mac = "AAAA:BBBB:CCCC"
print('{0[0]:b}{0[1]:b}{0[2]:b}'
      ''.format([int(i, 16) for i in mac.split(':')]))
# 8
ip = '10.1.1.1'
print('''
{0[0]:<10} {0[1]:<10} {0[2]:<10} {0[3]:<10}
{0[0]:010b} {0[1]:010b} {0[2]:010b} {0[3]:010b}
'''.format([int(elt) for elt in ip.split('.')]))
































