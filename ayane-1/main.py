#IMPORTS==========================================================
import threading
import time
from tkinter import * #tkinter for interface
from tkinter import ttk
#PATHS============================================================
skill_file = "data.txt"
#FONTS============================================================
font = "verdana 8"
#COLORS===========================================================
black = "#000000"
white = "#FFFFFF"
red = "#FF0000"
blue = "0000FF"
green = "#00FF00"
yellow = "#FFFF00"
biege = "#FFD089"
grey = "#A2A2A2"
dark_grey = "#727272"
#VARIABLES=========================================================

#FUNCTIONS========================================================
def close_window():
	window.destroy()
#CLASSES==========================================================
class Stopwatch:
	_running_stopwatch = False
	_running_thread = False
	_thread = None
	_elapsed = 0
	def __new__(cls, *args, **kwargs):
		print("call __new__ Stopwatch")
		return super().__new__(cls)
	def __init__(self):
		print("call __init__ Stopwatch")
	def __del__(self):
		print("call __del__ Stopwatch")
	@classmethod
	def _stopwatch(cls):
		while cls._running_stopwatch:
			time.sleep(0.1)
			tmp = time.gmtime(cls._elapsed)
			label_display_stopwatch.configure(text=time.strftime("%H.%M.%S", tmp))
			cls._elapsed += 0.1
	@classmethod
	def start_stopwatch(cls):
		button_pause_stopwatch.configure(state="normal", bg=black)
		button_start_stopwatch.configure(state="disabled", bg=red)
		cls._running_stopwatch = True
		cls._running_thread = True
		if cls._running_thread:
			cls._thread = threading.Thread(target=cls._stopwatch)
			cls._thread.start()
	@classmethod
	def pause_stopwatch(cls):
		button_start_stopwatch.configure(state="normal", bg=black)
		button_pause_stopwatch.configure(state="disabled", bg=red)
		cls._running_stopwatch = False
		cls._running_thread = False
		cls._thread = None
	@classmethod
	def stop_stopwatch(cls):
		button_start_stopwatch.configure(state="normal", bg=black)
		button_pause_stopwatch.configure(state="normal", bg=black)
		cls._running_stopwatch = False
		cls._running_thread = False
		cls._thread = None
		cls._elapsed = 0
		label_display_stopwatch.configure(text="00.00.00")
#THE HEART OF THE PROGRAMM==========================================
if __name__ == "__main__":
	#WINDOW SETTINGS================================================
	window = Tk()
	window.geometry("300x400+0+300")
	window.resizable(False, False)
	window.title("\u03baissmeandill\u03baissumyl\u00F6ve")
	window.iconbitmap("icon.ico")
	background = PhotoImage(file="background.png")
	bg_label = Label(image=background, border=0).place(x=0, y=0)
	#STOPWATCH=====================================================
	label_display_stopwatch = Label(
		master=window,
		font=font,
		text="00.00.00",
		bd=1,
		bg=black,
		fg=biege,
		state="normal",
	)
	label_display_stopwatch.place(x=150, y=0, width=150, height=20)


	button_start_stopwatch = Button(
		master=window,
		text="start",
		font=font,
		bg=black,
		bd=1,
		fg=biege,
		state="normal",
		activebackground=red,
		activeforeground=white,
		command=Stopwatch.start_stopwatch,
	)
	button_start_stopwatch.place(x=150, y=20, width=50, height=20)


	button_pause_stopwatch = Button(
		master=window,
		text="pause",
		font=font,
		bg=black,
		bd=1,
		fg=biege,
		state="normal",
		activebackground=red,
		activeforeground=white,
		command=Stopwatch.pause_stopwatch,
	)
	button_pause_stopwatch.place(x=200, y=20, width=50, height=20)


	button_stop_stopwatch = Button(
		master=window,
		text="stop",
		font=font,
		bg=black,
		bd=1,
		fg=biege,
		activebackground=red,
		activeforeground=white,
		command=Stopwatch.stop_stopwatch,
	)
	button_stop_stopwatch.place(x=250, y=20, width=50, height=20)
	#SKILL LIST=======================================================
	label_skill_list = Label(
		master=window,
		text="okay",
		font=font,
		bg=black,
		bd=1,
		fg=biege,
	)
	label_skill_list.place(x=150, y=41, width=150, height=359)
	#CHANGE WINDOW CLOSING PROTOCOL==================================
	window.protocol("WM_DELETE_WINDOW", close_window)
	#UPDATE DISPLAY==================================================
	window.mainloop()