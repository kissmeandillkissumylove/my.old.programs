class F:
	t = 'k'
	n = 'hg'

	def __init__(self, l, i):
		self.l = l
		self.i = i

	def f(self):
		pass

	@classmethod
	def b(cls):
		pass

	@staticmethod
	def c():
		pass


g = F('yty', 'hyhhbn')
g.f()
F.b()
F.c()
g.t = 442
g1 = F('fggb', 'gbgbgbgb')
print(g.t, F.t)
print(g1.t, F.t)
F.t = 54545
print(g.t, g1.t, F.t)