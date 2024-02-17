def abbrev_name(name):
    letter0 = name[0]
    i = 0
    for letter in name:
        if letter == ' ':
            letter1 = name[i+1]
        i += 1
    ret = f'{letter0.upper()}.{letter1.upper()}'
    return ret

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

def abbrev_name0(name):
	names = name.split()
	ret = '.'.join(word[0].upper() for word in names)
	return ret

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)
    


r = abbrev_name('pppfv pvpv')
print(r)
r = abbrevName('pppfv pvpv')
print(r)
r = abbrev_name0('pppfv pvpv vgvgv gvgv vv v d')
print(r)






