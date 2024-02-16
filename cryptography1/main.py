def xor(msg, key):
	msg = list(msg)
	for elt in range(len(msg)):
		try: msg[elt] = chr(ord(msg[elt]) ^ int(key))
		except: return '---key is not int type---'
	return ''.join(msg)


if __name__ == '__main__':
	msg = input('your message: ')
	key = int(input('key: '))
	msg = xor(msg, key)
	print(msg)
