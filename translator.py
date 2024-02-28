# imports
from tkinter import *
from googletrans import Translator

# functions
def translate_to_russian():
	text = text_input.get('1.0', END)
	translated_text = translator.translate(text, dest='ru')
	text_output.delete('1.0', END)
	text_output.insert('1.0', translated_text.text)

def translate_to_english():
	text = text_input.get('1.0', END)
	translated_text = translator.translate(text, dest='en')
	text_output.delete('1.0', END)
	text_output.insert('1.0', translated_text.text)

# init translator
translator = Translator()

# main window settings
main_win = Tk()
main_win.title('ayane miuro translator')
main_win.geometry('400x400+900+260')
main_win.resizable(width=False, height=False)
main_win.iconbitmap('min.ico')
main_win.configure(
	bg = '#7C522D',
	bd = 0
	)

# unput text field
text_input = Text(
	main_win,
	bd = 0,
	font = ('verdana', 10),
	bg = '#252525',
	wrap = WORD,
	fg = '#C4C0C0',
	insertbackground = 'red',
	padx=5,
	pady=5
	)

# output text field
text_output = Text(
	main_win,
	bd = 0,
	font = ('verdana', 10),
	bg = '#252525',
	wrap = WORD,
	fg = '#C4C0C0',
	insertbackground = 'red',
	padx=5,
	pady=5
	)

# button for russian translation
button_ru = Button(
	main_win,
	bd = 1,
	font = ('verdana', 10),
	bg = '#3F8148',
	activebackground = '#60B6AD',
	fg = 'black',
	text = 'ru',
	command = translate_to_russian
	)

# button for english translation
button_en = Button(
	main_win,
	bd = 1,
	font = ('verdana', 10),
	bg = '#3F8148',
	activebackground = '#60B6AD',
	fg = 'black',
	text = 'en',
	command = translate_to_english
	)

# render all items
text_input.place(x=5, y=20, width=390, height=180)
text_output.place(x=5, y=220, width=390, height=175)
button_ru.place(x=5, y=200, width=40, height=20)
button_en.place(x=45, y=200, width=40, height=20)

# main loop
main_win.mainloop()
