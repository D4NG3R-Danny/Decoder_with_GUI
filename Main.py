#Github:D4NG3R-Danny
import tkinter as tk
from tkinter import FLAT, Toplevel, messagebox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

WIDTH = 1200
HEIGTH= 800

### MAIN WINDOW #############
root = tk.Tk()
root.title("TADe 1.0")#TextAnalyzerDecipher

canvas = tk.Canvas(root,width=WIDTH,height=HEIGTH,bg="#371a12",highlightbackground="red",cursor="heart",confine=True,\
        relief=tk.GROOVE)
canvas.grid(columnspan=4,rowspan=4,sticky="NWES")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
#
root.maxsize(WIDTH,HEIGTH)
root.minsize(WIDTH,HEIGTH)
#############################

## Functions #####################
def letter_count(text: str)-> dict:
    counter = {}
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    for alphas in alphabet:
        counter.setdefault(alphas,-1)
        counter[alphas] += 1
    for letters in text:
        if letters == " ":
                counter.setdefault(" ",0)
                counter[" "] += 1
                continue
        elif letters == "\n":
                counter.setdefault("\ n",0)
                counter["\ n"] += 1
                continue
        counter.setdefault(letters.lower(),0)
        counter[letters.lower()] += 1
    return counter

def distribution():
        text = letter_count(entry_get())

        values_data = []
        keys_data   = []
        for keys, values in text.items():
                values_data.append(values)
                keys_data.append(keys)

        fig = plt.figure(figsize=(6,3.8))
        plt.bar(keys_data,values_data, width=1,edgecolor="white")

        New_window = Toplevel(background="#371a12") #<----here
        distribution_graph = FigureCanvasTkAgg(fig,master= New_window)
        distribution_graph.get_tk_widget().grid(row=0,column=1,sticky="NW",padx=0,pady=0,ipadx=0)
        distribution_graph.draw()
        New_window.mainloop()
        

#def text_output():
#        text = letter_count(entry_get())
#        values_data = []
#        keys_data   = []
#        for keys, values in text.items():
#                values_data.append(values)
#                keys_data.append(keys)
#        Output.insert(1.0,text)
        

def Select():#Execute selected function
        indexlist = index()
        answer = leftlist.get(indexlist)
        if answer == "Distribution Graph":
                distribution()
        #elif answer == "Lettercount":
        #        text_output()
        return None

def github_about():#Function executed at About_Cascade
        messagebox.showinfo("Contact-information","Github:"+"\n"+"D4NG3R-Danny")

def index():#Returns the index-1 of the selected element in the listbox
        index_leftlist = leftlist.curselection()[0]#Pls dont add a + 1 to return the correct index of list. Tkinter is stupid somehow.
        return index_leftlist  

def entry_get():#Get the text into a variable without the newline char
        text = leftentry.get(1.0,"end-1c")
        return text

def delete_text():
        leftentry.delete(1.0,"end")
#################################  

## WIDGETS ######################
option_titel = tk.Label(root,text="Options:",bg="#371a12",fg="#bc9073")
option_titel.grid(column=0,row=0,sticky="NW")
#Topleft Widget
leftlist = tk.Listbox(root,bg="#6f2f14",fg="#c7a28b",height=20,width=20,bd=5,cursor="arrow",relief=FLAT)
leftlist.insert(1,"Options:")
leftlist.insert(2,"Distribution Graph")
leftlist.insert(3,"Lettercount")
leftlist.grid(row=1,column=0,sticky="NW")
#Button in between
Select_Option = tk.Button(root,text="  Select  ",fg="white",bg="#6f2f14",activebackground="#9b582e",command=Select)
Select_Option.grid(row=2,column=0,sticky="NW",padx=0,pady=0)

Unselect_Option = tk.Button(root,text="Unselect",fg="white",bg="#6f2f14",activebackground="#9b582e",command=None)
Unselect_Option.grid(row=2,column=0,sticky="NW",padx=87,pady=0)
#Bottomleft Text-Widget 
leftentry = tk.Text(root,bg="#c7a28b",fg="#562a0d",relief=FLAT,height=26,width=30)
leftentry.grid(row=3,column=0,sticky="SW")
#Bottomright Widget
right_output = tk.Text(root,relief=tk.SUNKEN,height=26,width=30,bg="#bc9073")
right_output.grid(row=3,column=0,sticky="NW",padx=246)


#Bottom MiddleLeft
#Output = tk.Text(root,bg="#c7a28b",fg="#562a0d",width=42,height=23)
#Output.grid(row=2,column=1,sticky="SW")


### Menubar ########################
menubar = tk.Menu(root,bg="#ba661d")

#Start_Cascade
Start = tk.Menu(menubar)
menubar.add_cascade(label="Start",menu=Start)

Start.add_command(label="Delete Text",command=delete_text)
Start.add_command(label="text",command=entry_get)
Start.add_command(label="index",command=index)
Start.add_command(label="Quit", command=root.quit)

#About_Cascade
About = tk.Menu(menubar)
menubar.add_cascade(label="About",menu=About)

About.add_command(label="Contact",command=github_about)
####################################

#Mainloop has to be at the end
root.config(menu=menubar)
root.mainloop()

##NOTES##
#cursor="watch" looks like loading cursor
#bg="#4353465a" backgroundcolor can be a hexadecimal