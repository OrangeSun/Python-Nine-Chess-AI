import tkinter
import ctypes
import Nine_Game

'''
Introduction by OrangeSun:

[Class]UI : 
	[Init] :
		self : tkinter object
		self.btn : buttons
		self.btsn : the text on button's center
		self.id : the text on button's top
		self.auc : author name (me)
		self.blc/blt : states
		self.reset(): the function to clear the 'bstn'
[Function]click(numbers): the buttons' click events
[Object]a: the 'class ui' object's name  
!!! if you change this name, you should change the name in 'click(n)' too !!! 
'''

# Windows Height DPI #
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)


class UI(tkinter.Tk):

	def __init__(self):
		# Lab UI #
		super(UI, self).__init__()
		self.title("UI")
		self.geometry('850x660')
		# Strings (Button String) #
		self.bts1 = tkinter.StringVar()
		self.bts2 = tkinter.StringVar()
		self.bts3 = tkinter.StringVar()
		self.bts4 = tkinter.StringVar()
		self.bts5 = tkinter.StringVar()
		self.bts6 = tkinter.StringVar()
		self.bts7 = tkinter.StringVar()
		self.bts8 = tkinter.StringVar()
		self.bts9 = tkinter.StringVar()
		self.blt = tkinter.StringVar()  # State Messages String
		# Buttons #
		self.bt1 = tkinter.Button(self, textvariable=self.bts1, width=20, height=2, command=lambda x=1: click(x))
		self.bt2 = tkinter.Button(self, textvariable=self.bts2, width=20, height=2, command=lambda x=2: click(x))
		self.bt3 = tkinter.Button(self, textvariable=self.bts3, width=20, height=2, command=lambda x=3: click(x))
		self.bt4 = tkinter.Button(self, textvariable=self.bts4, width=20, height=2, command=lambda x=4: click(x))
		self.bt5 = tkinter.Button(self, textvariable=self.bts5, width=20, height=2, command=lambda x=5: click(x))
		self.bt6 = tkinter.Button(self, textvariable=self.bts6, width=20, height=2, command=lambda x=6: click(x))
		self.bt7 = tkinter.Button(self, textvariable=self.bts7, width=20, height=2, command=lambda x=7: click(x))
		self.bt8 = tkinter.Button(self, textvariable=self.bts8, width=20, height=2, command=lambda x=8: click(x))
		self.bt9 = tkinter.Button(self, textvariable=self.bts9, width=20, height=2, command=lambda x=9: click(x))
		# Labels #
		self.auc = tkinter.Label(self, text='Github@OrangeSun')
		self.blc = tkinter.Label(self, textvariable=self.blt, font=('KaiTi', 12))
		self.id0 = tkinter.Label(self, text='0')
		self.id1 = tkinter.Label(self, text='1')
		self.id2 = tkinter.Label(self, text='2')
		self.id3 = tkinter.Label(self, text='3')
		self.id4 = tkinter.Label(self, text='4')
		self.id5 = tkinter.Label(self, text='5')
		self.id6 = tkinter.Label(self, text='6')
		self.id7 = tkinter.Label(self, text='7')
		self.id8 = tkinter.Label(self, text='8')
		# Grids #
		self.id0.grid(row=1, column=1)
		self.id1.grid(row=1, column=2)
		self.id2.grid(row=1, column=3)
		self.id3.grid(row=3, column=1)
		self.id4.grid(row=3, column=2)
		self.id5.grid(row=3, column=3)
		self.id6.grid(row=5, column=1)
		self.id7.grid(row=5, column=2)
		self.id8.grid(row=5, column=3)
		self.auc.grid(row=8, column=2)
		self.blc.grid(row=7, column=2)
		self.bt1.grid(row=2, column=1, padx=15, pady=20, ipadx=10, ipady=30)
		self.bt2.grid(row=2, column=2, padx=15, pady=20, ipadx=10, ipady=30)
		self.bt3.grid(row=2, column=3, padx=15, pady=20, ipadx=10, ipady=30)
		self.bt4.grid(row=4, column=1, padx=15, pady=20, ipadx=10, ipady=30)
		self.bt5.grid(row=4, column=2, padx=15, pady=20, ipadx=10, ipady=30)
		self.bt6.grid(row=4, column=3, padx=15, pady=20, ipadx=10, ipady=30)
		self.bt7.grid(row=6, column=1, padx=15, pady=20, ipadx=10, ipady=30)
		self.bt8.grid(row=6, column=2, padx=15, pady=20, ipadx=10, ipady=30)
		self.bt9.grid(row=6, column=3, padx=15, pady=20, ipadx=10, ipady=30)

	def reset(self):
		self.bts1.set('')
		self.bts2.set('')
		self.bts3.set('')
		self.bts4.set('')
		self.bts5.set('')
		self.bts6.set('')
		self.bts7.set('')
		self.bts8.set('')
		self.bts9.set('')


# Events (if ui variable_name changes, this 'a' should be changed.) #

def click(n):
	eval('a.bts'+str(n)).set('X')
	a.update()
	r, b = Nine_Game.game(n)
	if b >= 0:
		eval('a.bts'+str(b)).set('O')
	a.blt.set(r)
	if (r == '--- You Winner ---') or (r == '--- You Loser ---') or (r == '--- Bad Game ---'):
		a.reset()
	return


a = UI()
a.mainloop()
'''
# Lab UI #
self = tkinter.Tk()
# Strings (Button String) #
bts1 = tkinter.StringVar()
bts2 = tkinter.StringVar()
bts3 = tkinter.StringVar()
bts4 = tkinter.StringVar()
bts5 = tkinter.StringVar()
bts6 = tkinter.StringVar()
bts7 = tkinter.StringVar()
bts8 = tkinter.StringVar()
bts9 = tkinter.StringVar()

blt = tkinter.StringVar()  # State Messages String


# Button Events
def click(n):
	eval('bts'+str(n)).set('X')
	Nine_Game.game(n)


# Buttons #
bt1 = tkinter.Button(self, textvariable=bts1, width=20, height=2, command=lambda x=1: click(x))
bt2 = tkinter.Button(self, textvariable=bts2, width=20, height=2, command=lambda x=2: click(x))
bt3 = tkinter.Button(self, textvariable=bts3, width=20, height=2, command=lambda x=3: click(x))
bt4 = tkinter.Button(self, textvariable=bts4, width=20, height=2, command=lambda x=4: click(x))
bt5 = tkinter.Button(self, textvariable=bts5, width=20, height=2, command=lambda x=5: click(x))
bt6 = tkinter.Button(self, textvariable=bts6, width=20, height=2, command=lambda x=6: click(x))
bt7 = tkinter.Button(self, textvariable=bts7, width=20, height=2, command=lambda x=7: click(x))
bt8 = tkinter.Button(self, textvariable=bts8, width=20, height=2, command=lambda x=8: click(x))
bt9 = tkinter.Button(self, textvariable=bts9, width=20, height=2, command=lambda x=9: click(x))

# selfels #
auc = tkinter.selfel(self, text='---Github@OrangeSun---')
blc = tkinter.selfel(self, textvariable=blt)
id0 = tkinter.selfel(self, text='0')
id1 = tkinter.selfel(self, text='1')
id2 = tkinter.selfel(self, text='2')
id3 = tkinter.selfel(self, text='3')
id4 = tkinter.selfel(self, text='4')
id5 = tkinter.selfel(self, text='5')
id6 = tkinter.selfel(self, text='6')
id7 = tkinter.selfel(self, text='7')
id8 = tkinter.selfel(self, text='8')

# Grids #
id0.grid(row=1, column=1)
id1.grid(row=1, column=2)
id2.grid(row=1, column=3)
id3.grid(row=3, column=1)
id4.grid(row=3, column=2)
id5.grid(row=3, column=3)
id6.grid(row=5, column=1)
id7.grid(row=5, column=2)
id8.grid(row=5, column=3)
auc.grid(row=8, column=2)
blc.grid(row=7, column=2)
bt1.grid(row=2, column=1, padx=15, pady=20, ipadx=10, ipady=30)
bt2.grid(row=2, column=2, padx=15, pady=20, ipadx=10, ipady=30)
bt3.grid(row=2, column=3, padx=15, pady=20, ipadx=10, ipady=30)
bt4.grid(row=4, column=1, padx=15, pady=20, ipadx=10, ipady=30)
bt5.grid(row=4, column=2, padx=15, pady=20, ipadx=10, ipady=30)
bt6.grid(row=4, column=3, padx=15, pady=20, ipadx=10, ipady=30)
bt7.grid(row=6, column=1, padx=15, pady=20, ipadx=10, ipady=30)
bt8.grid(row=6, column=2, padx=15, pady=20, ipadx=10, ipady=30)
bt9.grid(row=6, column=3, padx=15, pady=20, ipadx=10, ipady=30)

self.mainloop()


def reset():
	bts1.set('')
	bts2.set('')
	bts3.set('')
	bts4.set('')
	bts5.set('')
	bts6.set('')
	bts7.set('')
	bts8.set('')
	bts9.set('')
'''
