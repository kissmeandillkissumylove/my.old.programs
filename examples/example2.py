import math
import hashlib


# ______________________________________________________________________


def longest(a1, a2):
	arr, ret = [], ''
	for elt in a1:
		if elt not in arr:
			arr.append(elt)
	for elt in a2:
		if elt not in arr:
			arr.append(elt)
	arr.sort()
	for elt in arr:
		ret += elt
	return ret


def longest_codewars(a1, a2):
	return ''.join(sorted(set(a1 + a2)))


print('1.', longest("aretheyhere", "yestheyarehere"))
print('2.', longest_codewars("aretheyhere", "yestheyarehere"))


# ______________________________________________________________________


def solution(text, ending):
	return text[-len(ending):] == ending


def solution_codewars(string, ending):
	return string.endswith(ending)


print('3.', solution('world', 'ld'))
print('4.', solution_codewars('world', 'ld'))


# ______________________________________________________________________


def validate_pin(pin):
	return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()


def validate_pin_codewars(pin):
	return len(pin) in (4, 6) and pin.isdigit()


print('5.', validate_pin('45545'), validate_pin('4554'))
print('6.', validate_pin_codewars('45545'), end=' ')
print(validate_pin_codewars('4554'))


# ______________________________________________________________________


def array_diff(a, b):
	for elt in b:
		while (elt in a):
			a.remove(elt)
	return a


def array_diff_codewars(a, b):
	return [x for x in a if x not in set(b)]


print('7.', array_diff([1, 2, 2], [2]))
print('8.', array_diff_codewars([1, 2, 2], [2]))


# ______________________________________________________________________


def move_zeros(lst):
	iterator = 0
	while (0 in lst):
		iterator += 1
		lst.remove(0)
	for elt in range(iterator):
		lst.append(0)
	return lst


def move_zeros_codewars(arr):
	l = [i for i in arr if isinstance(i, bool) or i != 0]
	return l + [0] * (len(arr) - len(l))


def move_zeros_codewars1(arr):
	l = [i for i in arr if i != 0]
	return l + [0] * (len(arr) - len(l))


check_list1 = [9, 0, 0, 9, 1, 2, 0, 1, 0, 0, 1, 9, 0, 0, 9]
print('9.', move_zeros(check_list1))
print('10.', move_zeros_codewars(check_list1))
print('11.', move_zeros_codewars1(check_list1))


# ______________________________________________________________________


def rooks(n, k):
	return math.factorial(k) * math.comb(n, k) ** 2


def rooks(n, k):
	if k == 0: return 1
	if k > n: return 0
	if k == 1: return n * n
	return int(n * n * rooks(n - 1, k - 1) / k)


print('12.', rooks(4, 2))
print('13.', rooks(4, 2))


# ______________________________________________________________________


def to_sha256(s):
	return hashlib.sha256(s.encode()).hexdigest()


def to_sha256_codewars(s):
	"""preparing the message"""

	message = ''.join([hex(ord(char))[2:] for char in s])
	message_length = hex(len(s) * 8)[2:]
	message_length = '0' * (16 - len(message_length)) + message_length
	message += '8'
	message += '0' * ((240 - len(message)) % 128)
	message += message_length
	message = [message[i:i + 128] for i in range(0, len(message), 128)]

	h0 = 0x6a09e667
	h1 = 0xbb67ae85
	h2 = 0x3c6ef372
	h3 = 0xa54ff53a
	h4 = 0x510e527f
	h5 = 0x9b05688c
	h6 = 0x1f83d9ab
	h7 = 0x5be0cd19

	k = [
		0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
		0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
		0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
		0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
		0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
		0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
		0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
		0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
		0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
		0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
		0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
		0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
		0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
		0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
		0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
		0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
	]

	def rightrotate(hex_int, shift):
		return ((hex_int >> shift) + (hex_int << (32 - shift))) % (
				2 ** 32)

	def rightshift(hex_int, shift):
		return (hex_int >> shift)

	for chunk in message:

		w = [int('0x' + chunk[i * 8:i * 8 + 8], 16) for i in range(16)]

		for i in range(16, 64):
			s0 = rightrotate(w[i - 15], 7) ^ rightrotate(
				w[i - 15], 18) ^ rightshift(w[i - 15], 3)

			s1 = rightrotate(w[i - 2], 17) ^ rightrotate(
				w[i - 2], 19) ^ rightshift(w[i - 2], 10)

			w.append((w[i - 16] + s0 + w[i - 7] + s1) % (2 ** 32))

		a = h0
		b = h1
		c = h2
		d = h3
		e = h4
		f = h5
		g = h6
		h = h7

		for i in range(64):

			S1 = rightrotate(e, 6) ^ rightrotate(
				e, 11) ^ rightrotate(e, 25)

			ch = (e & f) ^ ((0xffffffff - e) & g)
			temp1 = (h + S1 + ch + k[i] + w[i]) % (2 ** 32)

			S0 = rightrotate(a, 2) ^ rightrotate(
				a, 13) ^ rightrotate(a, 22)

			maj = (a & b) ^ (a & c) ^ (b & c)
			temp2 = (S0 + maj) % (2 ** 32)

			h = g
			g = f
			f = e
			e = (d + temp1) % (2 ** 32)
			d = c
			c = b
			b = a
			a = (temp1 + temp2) % (2 ** 32)

		h0 = (h0 + a) % (2 ** 32)
		h1 = (h1 + b) % (2 ** 32)
		h2 = (h2 + c) % (2 ** 32)
		h3 = (h3 + d) % (2 ** 32)
		h4 = (h4 + e) % (2 ** 32)
		h5 = (h5 + f) % (2 ** 32)
		h6 = (h6 + g) % (2 ** 32)
		h7 = (h7 + h) % (2 ** 32)

	def f8(str_):
		return '0' * (8 - len(str_)) + str_

	return f8(hex(h0)[2:]) + f8(hex(h1)[2:]) + f8(hex(h2)[2:]) +\
		f8(hex(h3)[2:]) + f8(hex(h4)[2:]) + f8(hex(h5)[2:]) +\
		f8(hex(h6)[2:]) + f8(hex(h7)[2:])


print('14.', to_sha256('hello world suka'))
print('15.', to_sha256_codewars('hello world suka'))


# разбор


s = 'a'

message = ''.join([hex(ord(char))[2:] for char in s])
print('16.', message)
print('17.', ord(s))
print('18.', hex(ord(s)))
print('19.', hex(ord(s))[2:])

message_length = hex(len(s) * 8)[2:]
print('20.', message_length)
print('21.', len(s) * 8)
print('22.', hex(len(s) * 8))
print('23.', hex(len(s) * 8)[2:])

print('24.', len(message_length))
message_length = '0' * (16 - len(message_length)) + message_length
print('25.', message_length)


# ______________________________________________________________________


def controller(events):

    state = 0
    movement = False
    direction = True
    output = ''

    for event in events:

        if event == 'P':
            movement = not movement

        if event == 'O':
            direction = not direction

        state = state + (-1, 1)[direction] * movement

        if state in (0, 5):
            direction = not state
            movement  = False

        output += str(state)

    return output


def controller_codewars(events):

	out = []
	state = 0
	dir = 1
	moving = False

	for c in events:

		if c == 'O':
			dir *= -1

		elif c == 'P':
			moving = not moving

		if moving:
			state += dir

		if state in [0, 5]: moving, dir = False, 1 if state == 0 else -1

		out.append(str(state))

	return ''.join(out)


def controller_codewars1(events):

    pos = 0
    speed = 0
    dir = 1
    res = ''

    for e in events:

        if   e == 'P':
	        speed = not speed

        elif e == 'O' and speed:
	        dir *= -1

        pos = pos + speed * dir

        if pos in (0, 5) and speed:
	        speed= 0
	        dir = dir * -1

        res += str(pos)

    return res


print('26.', controller('...P..O..........'))
print('27.', controller_codewars('...P..O..........'))
print('28.', controller_codewars1('...P..O..........'))


# ______________________________________________________________________


def validBraces_codewars(string):

    braces = {
	    '(': ')',
	    '[': ']',
	    '{': '}'
    }
    stack = []

    for character in string:

        if character in braces.keys():
            stack.append(character)

        else:

            if len(stack) == 0 or braces[stack.pop()] != character:
                return False

    return len(stack) == 0


print('29.', validBraces_codewars('{()(){[()([])]}()}'))


# ______________________________________________________________________


def unique_in_order(iterable):

	i = 0
	array = []

	for elt in iterable:
		array.append(elt)

	while len(array):

		try:

			if array[i] == array[i + 1]:
				del array[i + 1]

			else:
				i += 1

		except IndexError:

			return array

	return array


def unique_in_order_co(iterable):

    res = []

    for item in iterable:

        if len(res) == 0 or item != res[-1]:
            res.append(item)

    return res


print('30.', unique_in_order('AAAABBBCCDAABBB'))


# ______________________________________________________________________


def find_uniq(arr):

    arr.sort()

    if(arr[0] < arr[-1] and arr[0] < arr[-2]):
        n = arr[0]

    else:
        n = arr[-1]

    return n


print('31.', find_uniq([1, 1, 1, 1, 1, 1, 0, 1, 1]))


# ______________________________________________________________________


import re

def domain_name(url):
    return re.search(
	    '(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')



#_______________________________________________________________________


def good_vs_evil(good, evil):

	g = good.split()
	e = evil.split()
	g_s, e_s = 0, 0
	g1, e1 = [], []

	for elt in g:
		g1.append(int(elt))

	for elt in e:
		e1.append(int(elt))

	g_s = g1[0]*1 + g1[1]*2 + g1[2]*3 + g1[3]*3 + g1[4]*4 + g1[5]*10

	e_s = e1[0]*1 + e1[1]*2 + e1[2]*2 + e1[3]*2 + e1[4]*3 + e1[5]*5 + e1[6]*10

	if g_s > e_s:
		return 'Battle Result: Good triumphs over Evil'
	elif g_s < e_s:
		return 'Battle Result: Evil eradicates all trace of Good'
	elif g_s == e_s:
		return 'Battle Result: No victor on this battle field'


print('32.', good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))


#_______________________________________________________________________


def bingo(ticket, win):
	n = ticket[win - 1]
	for cha in n[0]:
		if ord(cha) == n[1]:
			return 'Winner!'
	return 'Loser!'

print('33.', bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3))

def bingo_codewars(ticket, win):
	won = sum(chr(n) in xs for xs, n in ticket) >= win
	return 'Winner!' if won else 'Loser!'

print('34.', bingo_codewars(
	[['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3))


#_______________________________________________________________________


def sum_arrays(array1, array2):
	if array1 == []:
		return array2
	if array2 == []:
		return array1

	num1, num2 = '', ''

	for elt in array1:
		num1 += str(elt)
	for elt in array2:
		num2 += str(elt)

	num1, num2 = int(num1), int(num2)

	res = str(num1 + num2)
	arr = []
	it = 0
	op = ''
	for elt in res:
		if elt == '-':
			op = '-'
			continue
		else:
			arr.append(int(op + elt))
			op = ''
		it += 1

	return arr


print('34.', sum_arrays([1],[-5,7,6]))


# abs(value) - ||


# Вы можете добиться того же результата без использования явного цикла
# for, используя map(). Взгляните на следующую реализацию приведенного
# выше примера:
#
# >>> def square(number):
# ...       return number ** 2
# ...
#
# >>> numbers = [1, 2, 3, 4, 5]
# >>> squared = map(square, numbers)
# >>> list(squared)
# [1, 4, 9, 16, 25]



def sum_arrays_codewars(array1,array2):
    if not array1 and not array2:
        return []
    else:
        n1 = int("".join(map(str,array1))) if array1 else 0
        n2 = int("".join(map(str,array2))) if array2 else 0
        nT = n1+n2
        lst = list(map(int,str(abs(nT))))
        if nT < 0:
            lst[0] = -lst[0]
        return lst


print('35.', sum_arrays_codewars([1],[-5,7,6]))


#_______________________________________________________________________


# def defined_cube(y):
#     return y*y*y
#
#
# lambda_cube = lambda y: y*y*y
# print(defined_cube(2))
# print(lambda_cube(2))


#_______________________________________________________________________


def pick_peaks(arr):
	dict = {
		'pos': [],
		'peaks': []
	}

	iterator = 1
	for elt in arr[1:]:

		try:
			if elt > arr[iterator - 1] and elt > arr[iterator + 1]:

				dict['pos'].append(iterator)
				dict['peaks'].append(elt)

			elif elt > arr[iterator - 1] and elt == arr[iterator + 1]:

				iterator0 = iterator
				for elt0 in arr[iterator0:]:

					try:

						if elt0 == arr[iterator0 + 1]:
							iterator0 += 1
							continue
						if elt0 < arr[iterator0 + 1]:
							pass
						if elt > arr[iterator0 + 1]:
							dict['pos'].append(iterator)
							dict['peaks'].append(elt)

					except IndexError:
						pass

		except IndexError:
			pass

		iterator += 1

	return dict


print('36.', pick_peaks(
	[18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18,
	 -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]))


def pick_peaks_codewars(arr):
	peak, pos = [], []
	res = {"pos": [], "peaks": []}

	for i in range(1, len(arr)):
		if arr[i] > arr[i - 1]:
			peak, pos = [arr[i]], [i]

		elif arr[i] < arr[i - 1]:
			res["peaks"] += peak
			res["pos"] += pos
			peak, pos = [], []

	return res


print('37.', pick_peaks_codewars(
	[18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18,
	 -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]))


#_______________________________________________________________________


def sum_strings(x, y):
    return str(int(x) + int(y))



















































































