"""software for learning english
10.05.2023 https://github.com/kissmeandillkissumylove"""

from tkinter import *


class App(Frame):
	"""App main class."""

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()

	def run(self):
		"""call methods for activate app."""
		self._app_settings()
		bg_label = Label(
			bg="#000000",
			bd=0,

		)
		bg_label.place(x=0, y=0, width=400, height=400)

	def _app_settings(self):
		"""app settings."""
		self.master.title("\u03baissmeandill\u03baissumyl\u00F6ve")
		self.master.geometry("400x400")
		self.master.resizable(False, False)
		self.master.iconbitmap("../data/icon.ico")


def main():
	"""main function."""
	myapp = App()
	myapp.run()
	myapp.mainloop()


if __name__ == "__main__":
	main()
