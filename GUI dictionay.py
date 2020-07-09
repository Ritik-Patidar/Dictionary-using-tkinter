from tkinter import *
window = Tk()

import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def show():
    word = (e1_value.get()) 
    output = translate(word)
    t1.delete("1.0", END)
    t1.insert(END,output)

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "word not found"
    
    
b1= Button(window,text="Search",command=show)
b1.grid(row=1,column=2)

e1_value = StringVar()
e1 = Entry(window,textvariable = e1_value )
e1.grid(row=0,column=2)

e2 = Label(window,text ="Word :")
e2.grid(row=0,column=1)

t1=Text(window,height=10,width=40)
t1.grid(row=2,column=2)

window.mainloop()