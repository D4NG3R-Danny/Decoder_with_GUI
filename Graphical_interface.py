#GITHUB:D4NG3R-D4NNY
from tkinter import *
import tkinter.ttk as ttk
import text_anal
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

#WINDOW#####
root = Tk()
root.title("[My First Program]")
#WindowSize#
WIDTH = 1000
HEIGTH= 1000
###########
#Window####
frame = Frame(root,width=WIDTH,height=HEIGTH)
frame.pack()
#Menubar for Options, etc.
menubar = Menu(root)
#Menubar 
Start = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Start', menu= Start)
Start.add_command(label="1", command=None)
Start.add_separator()
Start.add_command(label="EXIT",command=root.destroy)
##########
Options = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Options', menu= Options)
Options.add_command(label='Create DoL-Graph', command=lambda: distribution())
##########
'''
#/////////////////////////////////////////////////////////////////////////////////
#Drawing block
#/////////////////////////////////////////////////////////////////////////////////
def mouse_draw(event):
    x1,y1,x2,y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 )
    Colour = "#000fff000"
    line = c.create_line( x1, y1, x2,y2, fill = Colour )

def deli(event):
    for i in range(4):
        c.delete(oval+i)
    
c = Canvas(root,height=HEIGTH,width=WIDTH)
oval = c.create_oval(10,10,200,200,fill="yellow",outline='red')
oval1 = c.create_oval(200,10,400,200,fill="yellow",outline='red')
oval2 = c.create_oval(400,10,600,200,fill="yellow",outline='red')
oval3 = c.create_oval(600,10,800,200,fill="yellow",outline='red')

c.bind("<B1-Motion>",mouse_draw)
c.bind("<B3-Motion>",deli)
c.place(x=0,y=0)
#//////////////////////////////////////////////////////////////////////////////////
'''
#Input_Function which return the input above the Decode Message button
#def decode_txt():
#    inputtxt = decodeinput.get("1.0",END)
#    outputtxt.insert("end",text)
#    return inputtxt


def letter_count()-> dict:
    text = decodeinput.get("1.0",END)
    counter = text_anal.letter_count(text)
    outputtxt.insert("end",counter)
    return counter

#Create Graph Button
plotbutton = Button(root,height=10,width=15,text="Create Graph",command=lambda: distribution())
plotbutton.pack()
def distribution():
    text = decodeinput.get("1.0",END)
    dictionary = text_anal.letter_count(text)
    fg = text_anal.count_plot(dictionary)
    canvas1 = FigureCanvasTkAgg(fg, master=root)
    canvas1.draw()
    canvas1.get_tk_widget().place(x= 15,y= 15)
    toolbar = NavigationToolbar2Tk(canvas1, root)
    toolbar.update()
    canvas1.get_tk_widget().pack(side=TOP, fill=BOTH)

#Input_User_Interface
decodeinput = Text(root, height=2, width=100)
decodeinput.place(x=10,y=10)
decode = Button(root,height=1,width=15,text="Decode Message", command=lambda: letter_count())
#decode.pack()
decode.place(x=10,y=30)
#Output_User_Interface
outputtxt = Text(root, height=2, width=100)
outputtxt.place(x=10,y=70)
encode = Button(root,height=1,width=15,text="Output Message")
encode.place(x=10,y=90)
#Button to close Window
quiting = Button(root, text = 'Quit', bd='5', command = root.destroy)
quiting.place(x=WIDTH - 70,y=HEIGTH - 40)

root.config(menu = menubar)
root.mainloop()

#@D4NG3R-D4NNY--> ADD Save function to Menubar to save decrypted or encrypted message
#                 
