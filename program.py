from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from database import *
import json

global cbvar1
global cbvar2
global cbvar3
global cbvar4
global cbvar5
global cbvar6
global cbvar7
global cbvar8
global cbvar9
global cbvars

labels = {}
collectiontextboxes = {}
keytextboxes = {}
sorttextboxes = {}
showcheckboxes = {}
conditiontextboxes = {}

def clear_textboxes():
    for i in range(9):
        collectiontextboxes[str(i)].delete(0, END)
        keytextboxes[str(i)].delete(0, END)
        conditiontextboxes[str(i)].delete(0, END)
        cbvars[i].set(0)

def collectionchoosen_handler(event):
    textarea.delete('1.0', END)
    clear_textboxes()
    keys = get_keys(db_name, collectionchoosen.get())
    for i, key in enumerate(keys):
        newline = '\n' if i > 0 else ''
        textarea.insert(END, "{}{}".format(newline, key))
        collectiontextboxes[str(i)].insert(0, collectionchoosen.get())
        keytextboxes[str(i)].insert(0, key)

def contextMenuPopup(event):
    textarea2.selection_clear()
    pass

def dbchoosen_handler(event):
    global db_name
    db_name = dbchoosen.get()
    colls = collection_names(db_name)
    collectionchoosen['values'] = colls
    collectionchoosen.current(0)
    collectionchoosen_handler(None)

def raise_frame(frame):
    frame.tkraise()

def run_query(frame):
    global collection_name
    global cbvars
    
    keynames = []
    conditions = []

    collection_name = collectiontextboxes["0"].get()

    for i, cb in enumerate(cbvars):
        if cbvars[i].get() or conditiontextboxes[str(i)].get():
            keyname = keytextboxes[str(i)].get()
            condition = conditiontextboxes[str(i)].get()
            keynames.append(keyname)
            conditions.append(condition)

    res = query(db_name, collection_name, keynames, conditions)

    textarea2.delete('1.0', END)
    textarea2.insert('1.0', json.dumps(res, indent=4, default=str))

    raise_frame(frame)

root = Tk()

root.rowconfigure(0, weight=1) 
root.columnconfigure(0, weight=1)

container1 = Frame(root, borderwidth=1, relief="solid")
container2 = Frame(root,  borderwidth=1, relief="solid")

container1.columnconfigure(0, weight=1)
container2.columnconfigure(0, weight=1)

# container1 widgets
sf1 = Frame(container1)
hoz1 = Frame(container1, height=2, width=10, bg="grey")
sf2 = Frame(container1)
hoz2 = Frame(container1, height=2, width=10, bg="grey")
canvas = Canvas(container1)
scrollbar = Scrollbar(container1, orient="horizontal", command=canvas.xview)
scrollableframe = Frame(canvas)

scrollableframe.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollableframe)
canvas.configure(xscrollcommand=scrollbar.set)

dbs = db_names()
n = StringVar() 
dbchoosen = ttk.Combobox(sf1, textvariable = n) 
dbchoosen['values'] = dbs
dbchoosen.grid(row = 0, column=0) 
dbchoosen.current() 
dbchoosen.bind("<<ComboboxSelected>>", dbchoosen_handler)

m = StringVar() 
collectionchoosen = ttk.Combobox(sf1, textvariable = m) 
collectionchoosen.grid(row = 0, column=2) 
collectionchoosen.current() 
collectionchoosen.bind("<<ComboboxSelected>>", collectionchoosen_handler)

img1 = Image.open('play.png')
useImg1 = ImageTk.PhotoImage(img1)
runbutton = Button(sf1, image=useImg1, command=lambda:run_query(container2))

keyslabel = Label(sf2, text="Keys:")
textarea = Text(sf2, width=38, height=10)
textarea.config(highlightbackground="black", highlightthickness=1)

cbvar1 = IntVar()
cbvar2 = IntVar()
cbvar3 = IntVar()
cbvar4 = IntVar()
cbvar5 = IntVar()
cbvar6 = IntVar()
cbvar7 = IntVar()
cbvar8 = IntVar()
cbvar9 = IntVar()
cbvars = [cbvar1, cbvar2, cbvar3, cbvar4, cbvar5, cbvar6, cbvar7, cbvar8, cbvar9]
labels["0"] = Label(scrollableframe, text="Collection:")
labels["1"] = Label(scrollableframe, text="Key:")
labels["2"] = Label(scrollableframe, text="Sort:")
labels["3"] = Label(scrollableframe, text="Show:")
labels["4"] = Label(scrollableframe, text="Conditions:")
collectiontextboxes["0"] = Entry(scrollableframe)
keytextboxes["0"] = Entry(scrollableframe)
sorttextboxes["0"] = Entry(scrollableframe)
showcheckboxes["0"] = Checkbutton(scrollableframe, variable=cbvars[0])
conditiontextboxes["0"] = Entry(scrollableframe)
collectiontextboxes["1"] = Entry(scrollableframe)
keytextboxes["1"] = Entry(scrollableframe)
sorttextboxes["1"] = Entry(scrollableframe)
showcheckboxes["1"] = Checkbutton(scrollableframe, variable=cbvars[1])
conditiontextboxes["1"] = Entry(scrollableframe)
collectiontextboxes["2"] = Entry(scrollableframe)
keytextboxes["2"] = Entry(scrollableframe)
sorttextboxes["2"] = Entry(scrollableframe)
showcheckboxes["2"] = Checkbutton(scrollableframe, variable=cbvars[2])
conditiontextboxes["2"] = Entry(scrollableframe)
collectiontextboxes["3"] = Entry(scrollableframe)
keytextboxes["3"] = Entry(scrollableframe)
sorttextboxes["3"] = Entry(scrollableframe)
showcheckboxes["3"] = Checkbutton(scrollableframe, variable=cbvars[3])
conditiontextboxes["3"] = Entry(scrollableframe)
collectiontextboxes["4"] = Entry(scrollableframe)
keytextboxes["4"] = Entry(scrollableframe)
sorttextboxes["4"] = Entry(scrollableframe)
showcheckboxes["4"] = Checkbutton(scrollableframe, variable=cbvars[4])
conditiontextboxes["4"] = Entry(scrollableframe)
collectiontextboxes["5"] = Entry(scrollableframe)
keytextboxes["5"] = Entry(scrollableframe)
sorttextboxes["5"] = Entry(scrollableframe)
showcheckboxes["5"] = Checkbutton(scrollableframe, variable=cbvars[5])
conditiontextboxes["5"] = Entry(scrollableframe)
collectiontextboxes["6"] = Entry(scrollableframe)
keytextboxes["6"] = Entry(scrollableframe)
sorttextboxes["6"] = Entry(scrollableframe)
showcheckboxes["6"] = Checkbutton(scrollableframe, variable=cbvars[6])
conditiontextboxes["6"] = Entry(scrollableframe)
collectiontextboxes["7"] = Entry(scrollableframe)
keytextboxes["7"] = Entry(scrollableframe)
sorttextboxes["7"] = Entry(scrollableframe)
showcheckboxes["7"] = Checkbutton(scrollableframe, variable=cbvars[7])
conditiontextboxes["7"] = Entry(scrollableframe)
collectiontextboxes["8"] = Entry(scrollableframe)
keytextboxes["8"] = Entry(scrollableframe)
sorttextboxes["8"] = Entry(scrollableframe)
showcheckboxes["8"] = Checkbutton(scrollableframe, variable=cbvars[8])
conditiontextboxes["8"] = Entry(scrollableframe)

# container2 widgets
img2 = Image.open('edit.png')
useImg2 = ImageTk.PhotoImage(img2)
editbutton = Button(container2, image=useImg2, command=lambda:raise_frame(container1))
hozline = Frame(container2, height=2, width=10, bg="grey")
textarea2 = Text(container2)
container2.bind_class("Text", sequence='<Button-2>', func=contextMenuPopup) # fixes tkinter disable highlight right click pasting error

# root grid
container1.grid(row=0, column=0, sticky='news')
container2.grid(row=0, column=0, sticky='news')

# container1 grid
sf1.grid(row=0, column=0, sticky='news')
hoz1.grid(row=1, column=0, sticky='news')
sf2.grid(row=2, column=0, sticky='news')
hoz2.grid(row=3, column=0, sticky='news')
canvas.grid(row=4, column=0, sticky='ew')
scrollbar.grid(row=5, column=0, stick='ew')

# sf1 grid
runbutton.grid(row=0, column=4)

# sf2 grid
keyslabel.grid(row=1, column=0, sticky="w")
textarea.grid(row=2, column=0)

# scrollableframe grid
labels["0"].grid(row=0, column=0, sticky="e")
labels["1"].grid(row=1, column=0, sticky="e") 
labels["2"].grid(row=2, column=0, sticky="e")
labels["3"].grid(row=3, column=0, sticky="e")
labels["4"].grid(row=4, column=0, sticky="e")
collectiontextboxes["0"].grid(row=0, column=1) 
collectiontextboxes["1"].grid(row=0, column=2)
collectiontextboxes["2"].grid(row=0, column=3)
collectiontextboxes["3"].grid(row=0, column=4)
collectiontextboxes["4"].grid(row=0, column=5)
collectiontextboxes["5"].grid(row=0, column=6)
collectiontextboxes["6"].grid(row=0, column=7)
collectiontextboxes["7"].grid(row=0, column=8)
collectiontextboxes["8"].grid(row=0, column=9)
keytextboxes["0"].grid(row=1, column=1)
keytextboxes["1"].grid(row=1, column=2)
keytextboxes["2"].grid(row=1, column=3)
keytextboxes["3"].grid(row=1, column=4)
keytextboxes["4"].grid(row=1, column=5)
keytextboxes["5"].grid(row=1, column=6)
keytextboxes["6"].grid(row=1, column=7)
keytextboxes["7"].grid(row=1, column=8)
keytextboxes["8"].grid(row=1, column=9)
sorttextboxes["0"].grid(row=2, column=1)
sorttextboxes["1"].grid(row=2, column=2)
sorttextboxes["2"].grid(row=2, column=3)
sorttextboxes["3"].grid(row=2, column=4)
sorttextboxes["4"].grid(row=2, column=5)
sorttextboxes["5"].grid(row=2, column=6)
sorttextboxes["6"].grid(row=2, column=7)
sorttextboxes["7"].grid(row=2, column=8)
sorttextboxes["8"].grid(row=2, column=9)
showcheckboxes["0"].grid(row=3, column=1)
showcheckboxes["1"].grid(row=3, column=2)
showcheckboxes["2"].grid(row=3, column=3)
showcheckboxes["3"].grid(row=3, column=4)
showcheckboxes["4"].grid(row=3, column=5)
showcheckboxes["5"].grid(row=3, column=6)
showcheckboxes["6"].grid(row=3, column=7)
showcheckboxes["7"].grid(row=3, column=8)
showcheckboxes["8"].grid(row=3, column=9)
conditiontextboxes["0"].grid(row=4, column=1)
conditiontextboxes["1"].grid(row=4, column=2)
conditiontextboxes["2"].grid(row=4, column=3)
conditiontextboxes["3"].grid(row=4, column=4)
conditiontextboxes["4"].grid(row=4, column=5)
conditiontextboxes["5"].grid(row=4, column=6)
conditiontextboxes["6"].grid(row=4, column=7)
conditiontextboxes["7"].grid(row=4, column=8)
conditiontextboxes["8"].grid(row=4, column=9)

# container2 grid
editbutton.grid(row=0, column=0, sticky="w")
hozline.grid(row=2, column=0, sticky='news')
textarea2.grid(row=3, column=0, sticky="news")

raise_frame(container1)

root.mainloop()