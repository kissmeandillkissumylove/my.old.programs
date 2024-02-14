# # imports
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

import PIL
from PIL import Image, ImageDraw, ImageTk
from random import *

from datetime import datetime
from googletrans import Translator


# # variables
labelbgcolor = '#a0a0a0'
buttonbgcolor = '#009900'
buttonactivebackgroundcolor = '#ff0000'
programmfont = ('helvetica', 8)
num = 0
temp = 0
after_id = ''


veiw_colors = {
	'dark' : {
		'text_bg': 'black',
		'text_fg': 'lime',
		'cursor': 'brown',
		'select_bg': '#8d917a'
		},
	'light': {
		'text_bg': 'white',
		'text_fg': 'black',
		'cursor': '#a5a5a5',
		'select_bg': '#faeedd' 
		}
	}
	
fonts = {
	'consolas' : {
		'font': 'consolas 10'
		},
	'simhei': {
		'font': 'simhei 10'
		},
	'verdana': {
		'font': 'verdana 10'
		}
	}



# # defs
def clickbuttonnebo():
	global num
	num = num + 1
	labelnebo.configure(text = num)

def clickbuttoninsert():
	entrynebo.insert(0, 'hi')
	
def clickbuttondelete():
	entrynebo.delete(0, END)

def clickbuttonget():
	labelnebo['text'] = entrynebo.get()

def mstick():
	global temp, after_id
	after_id = windowmain.after(1000, mstick)
	f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
	labeltimer.configure(text=str(f_temp))
	temp += 1

def startmstick():
	buttonstarttimer['bg'] = buttonactivebackgroundcolor
	buttonstoptimer['bg'] = buttonbgcolor
	mstick()
	
def stopmstick():
	buttonstoptimer['bg'] = buttonactivebackgroundcolor
	buttonstarttimer['bg'] = buttonbgcolor
	windowmain.after_cancel(after_id)
	
def continuemstick():
	buttonstarttimer['bg'] = buttonbgcolor
	buttonstoptimer['bg'] = buttonbgcolor
	mstick()
	
def change_theme(theme):
	texttext['bg'] = veiw_colors[theme]['text_bg']
	texttext['fg'] = veiw_colors[theme]['text_fg']
	texttext['insertbackground'] = veiw_colors[theme]['cursor']
	texttext['selectbackground'] = veiw_colors[theme]['select_bg']
	
def change_fonts(fontss):
	texttext['font'] = fonts[fontss]['font']
	
def notepad_exit():
	answer = messagebox.askokcancel('exit', 'are u sure?')
	if answer:
		windowmain.destroy()
		
def open_file():
	file_path = filedialog.askopenfilename(title='select file', filetypes=(('text documents (*.txt)', '*.txt'), ('all files', '*.*')))
	if file_path:
		texttext.delete('1.0', END)
		texttext.insert('1.0', open(file_path).read())

def save_file():
	file_path = filedialog.asksaveasfilename(filetypes=(('text documents (*.txt)', '*.txt'), ('all files', '*.*')))
	f = open(file_path, 'w', encoding='utf-8')
	text = texttext.get('1.0', END)
	f.write(text)
	f.close()
		


# # main window settings
windowmain = Tk()
windowmain['bg'] = '#202020'
windowmain.geometry('402x502')
# windowmain.resizable(width=False, height=False)
windowmain.title('ayane miuro')
windowmain.iconbitmap('min.ico')

img = Image.open('back.png')
img_res = img.resize((402, 502))
img_ret = ImageTk.PhotoImage(img_res)
windowmain.image = img_ret
back = Label(windowmain, image=windowmain.image, bd=0)
back.place(x=0, y=0)




# # nebogame button settings
imagenebo = PhotoImage(file = 'nebo.png')
buttonnebo = Button(windowmain,
	activebackground = 'blue',
	bg = buttonbgcolor,
	image = imagenebo,
	command = clickbuttonnebo,
	bd = 1,
	)


# # label of buttonnebo
labelnebo = Label(windowmain,
	bg = labelbgcolor,
	text = num,
	font = programmfont,
	bd = 1,
	)
	

# # entry for label of buttonnebo
entrynebo = Entry(windowmain,
	font = programmfont,
	bd = 1,
	)
	

# # insert in entry button
buttoninsert = Button(windowmain,
	activebackground = 'blue',
	bg = buttonbgcolor,
	font = programmfont,
	text = 'ins',
	command = clickbuttoninsert,
	bd = 1,
	)


# # delete entry button
buttondelete = Button(windowmain,
	activebackground = 'blue',
	bg = buttonbgcolor,
	font = programmfont,
	text = 'del',
	command = clickbuttondelete,
	bd = 1,
	)


# # get entry button
buttonget = Button(windowmain,
	activebackground = 'blue',
	bg = buttonbgcolor,
	font = programmfont,
	text = 'get',
	command = clickbuttonget,
	bd = 1,
	)
	
	
# # label
labeltimer = Label(windowmain,
	bg = labelbgcolor,
	font = programmfont,
	text = '00:00',
	bd = 1,
	)
	

# button
buttonstarttimer = Button(windowmain,
	activebackground = 'blue',
	bg = buttonbgcolor,
	bd = 1,
	font = programmfont,
	text = 'sta',
	command = startmstick,
	)
	

# button
buttonpausetimer = Button(windowmain,
	activebackground = 'blue',
	bg = buttonbgcolor,
	bd = 1,
	font = programmfont,
	text = 'pau',
	command = continuemstick,
	)


# button
buttonstoptimer = Button(windowmain,
	activebackground = 'blue',
	bg = buttonbgcolor,
	bd = 1,
	font = programmfont,
	text = 'sto',
	command = stopmstick,
	)


# frame
frametext = Frame(windowmain)


# text
texttext = Text(frametext,
	bg = labelbgcolor,
	fg = 'black',
	padx = 5,
	pady = 5,
	wrap = WORD,
	insertbackground = 'black',
	selectbackground = 'brown',
	# spacing3 = 10,
	width = 37
	)


# scroll
scrolltext = Scrollbar(frametext,
	command = texttext.yview
	)


# menu
main_menu = Menu(windowmain)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label = 'open', command=open_file)
file_menu.add_command(label = 'save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label = 'close', command=notepad_exit)

# view
veiw_menu = Menu(main_menu, tearoff=0)
veiw_menu_sub = Menu(veiw_menu, tearoff=0)
font_menu_sub = Menu(veiw_menu, tearoff=0)
veiw_menu_sub.add_command(label = 'dark', command=lambda: change_theme('dark'))
veiw_menu_sub.add_command(label = 'light', command=lambda: change_theme('light'))
veiw_menu.add_cascade(label = 'theme', menu=veiw_menu_sub)

font_menu_sub.add_command(label = 'consolas', command=lambda: change_fonts('consolas'))
font_menu_sub.add_command(label = 'simhei', command=lambda: change_fonts('simhei'))
font_menu_sub.add_command(label = 'verdana', command=lambda: change_fonts('verdana'))
veiw_menu.add_cascade(label = 'font', menu=font_menu_sub)


def activate_point(event):
	x1, y1 = (event.x - 1), (event.y - 1)
	x2, y2 = (event.x + 1), (event.y + 1)
	cv.create_line(x1, y1, x2, y2, fill='black', width=5)
	draw.line((x1, y1, x2, y2), fill='black', width=5)

def save_img():
	filename = f'image_{randint(0, 1000000)}.png'
	image1.save(filename)
	messagebox.showinfo('saving', 'saved: %s' %filename)

save_img_menu = Menu(main_menu, tearoff=0)
save_img_menu_sub = Menu(save_img_menu, tearoff=0)
save_img_menu_sub.add_command(label = 'save-img', command=save_img)


main_menu.add_cascade(label='file', menu=file_menu)
main_menu.add_cascade(label='view', menu=veiw_menu)
main_menu.add_cascade(label='save-img', menu=save_img_menu_sub)


windowmain.config(menu=veiw_menu)
windowmain.config(menu=file_menu)
windowmain.config(menu=main_menu)



	
# button
def open_win():
	win = Toplevel()
	win.geometry('200x200')
	win.grab_set()
	l = Label(win, text='Toplevel', font='arial 15 bold', fg='brown').pack()
	# win.overrideredirect(1)
	win.title('')
	win.iconbitmap('min.ico')
	win.after(3000, lambda: win.destroy())

	
btn = Button(windowmain,
	activebackground = 'blue',
	bg = buttonbgcolor,
	bd = 1,
	font = programmfont,
	text = 'open',
	command = open_win,
	)

# les8

s = ttk.Style()
s.configure('.', bg='yellow')
print(s.theme_names(), s.theme_use('xpnative'))

# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

Button(windowmain, text='one').place(x=1, y=122, width=40, height=40)
ttk.Button(windowmain, text='two').place(x=41, y=122, width=40, height=40)



# draw

cv = Canvas(windowmain, bg='white')

image1 = PIL.Image.new('RGB', (80, 78), 'white')
draw = ImageDraw.Draw(image1)

cv.bind('<B1-Motion>', activate_point)
cv.place(x=1, y=162, width=80, height=80)


# translator

translator = Translator()

def toen():
	text = t.get('1.0', END)
	a = translator.translate(text, dest='en')
	t1.delete('1.0', END)
	t1.insert('1.0', a.text)

def toru():
	text = t.get('1.0', END)
	a = translator.translate(text, dest='ru')
	t1.delete('1.0', END)
	t1.insert('1.0', a.text)

def topl():
	text = t.get('1.0', END)
	a = translator.translate(text, dest='pl')
	t1.delete('1.0', END)
	t1.insert('1.0', a.text)
	
def tofr():
	text = t.get('1.0', END)
	a = translator.translate(text, dest='fr')
	t1.delete('1.0', END)
	t1.insert('1.0', a.text)
	
t = Text(windowmain,
	font = 'verdana 8',
	bd = 1,
	)
t.place(x=1, y=243, width=175, height=80)
	
btn1 = Button(windowmain,
	text = 'ru',
	font = 'verdana 8',
	bd = 1,
	bg = 'black',
	fg = 'white',
	activeforeground = 'white',
	activebackground = 'blue',
	command = toru,
	)
btn1.place(x=175, y=243, width=25, height=40)

btn2 = Button(windowmain,
	text = 'en',
	font = 'verdana 8',
	bd = 1,
	bg = 'black',
	fg = 'white',
	activeforeground = 'white',
	activebackground = 'blue',
	command = toen,
	)
btn2.place(x=200, y=243, width=25, height=40)

btn3 = Button(windowmain,
	text = 'pl',
	font = 'verdana 8',
	bd = 1,
	bg = 'black',
	fg = 'white',
	activeforeground = 'white',
	activebackground = 'blue',
	command = topl,
	)
btn3.place(x=175, y=283, width=25, height=40)

btn4 = Button(windowmain,
	text = 'fr',
	font = 'verdana 8',
	bd = 1,
	bg = 'black',
	fg = 'white',
	activeforeground = 'white',
	activebackground = 'blue',
	command = tofr,
	)
btn4.place(x=200, y=283, width=25, height=40)

t1 = Text(windowmain,
	font = 'verdana 8',
	bd = 1,
	)
t1.place(x=225, y=243, width=176, height=80)



	
# # pack all items
buttonnebo.place(x=1, y=1, width=40, height=40)
labelnebo.place(x=41, y=1, width=40, height=40)
entrynebo.place(x=81, y=1, width=239, height=40)
buttoninsert.place(x=321, y=1, width=27, height=40)
buttondelete.place(x=348, y=1, width=27, height=40)
buttonget.place(x=375, y=1, width=27, height=40)
labeltimer.place(x=1, y=42, width=80, height=20)
buttonstarttimer.place(x=1, y=62, width=27, height=20)
buttonpausetimer.place(x=28, y=62, width=27, height=20)
buttonstoptimer.place(x=55, y=62, width=27, height=20)
frametext.place(x=82, y=42, width=319, height=200)
texttext.pack(expand=1, fill=BOTH, side=LEFT)
scrolltext.pack(side=LEFT, fill=Y)
texttext.config(yscrollcommand=scrolltext.set)
btn.place(x=1, y=82, width=40, height=40)


# # main loop
windowmain.mainloop()
