#! /Users/s13a/rsrch-25-mar-2020/tcl/qbe4/venv/bin/python

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from database import *
import json
from tkinter import messagebox
import os

IMAGE_PATH = os.getenv("IMAGE_PATH")

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
dmltextboxes = {}

def checkall_clicked():
    if collectiontextboxes["0"].get():
        cbvar1.set(True)
    if collectiontextboxes["1"].get():
        cbvar2.set(True)
    if collectiontextboxes["2"].get():
        cbvar3.set(True)
    if collectiontextboxes["3"].get():
        cbvar4.set(True)
    if collectiontextboxes["4"].get():
        cbvar5.set(True)
    if collectiontextboxes["5"].get():
        cbvar6.set(True)
    if collectiontextboxes["6"].get():
        cbvar7.set(True)
    if collectiontextboxes["7"].get():
        cbvar8.set(True)
    if collectiontextboxes["8"].get():
        cbvar9.set(True)

def uncheckall_clicked():
    if collectiontextboxes["0"].get():
        cbvar1.set(False)
    if collectiontextboxes["1"].get():
        cbvar2.set(False)
    if collectiontextboxes["2"].get():
        cbvar3.set(False)
    if collectiontextboxes["3"].get():
        cbvar4.set(False)
    if collectiontextboxes["4"].get():
        cbvar5.set(False)
    if collectiontextboxes["5"].get():
        cbvar6.set(False)
    if collectiontextboxes["6"].get():
        cbvar7.set(False)
    if collectiontextboxes["7"].get():
        cbvar8.set(False)
    if collectiontextboxes["8"].get():
        cbvar9.set(False)

def clear_textboxes():
    for i in range(9):
        collectiontextboxes[str(i)].delete(0, END)
        keytextboxes[str(i)].delete(0, END)
        sorttextboxes[str(i)].delete(0, END)
        conditiontextboxes[str(i)].delete(0, END)
        dmltextboxes[str(i)].delete(0, END)
        cbvars[i].set(0)

def clear_textboxes_2():
    for i in range(9):
        sorttextboxes[str(i)].delete(0, END)
        conditiontextboxes[str(i)].delete(0, END)
        dmltextboxes[str(i)].delete(0, END)

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

def query(db_name, collection_name, keynames, sorts, conditions, dmls):
    selections = {}
    projections = {}
    sort = {}
    insertions = {}
    updates = {}

    db = client[db_name]
    collection = db[collection_name]

    projections.update({"_id": False})

    if dmls[0].lower() == "insert":
        for i, dml in enumerate(dmls, 0):
            if i > 0:
                if "[" in dml and "]" in dml:
                    dml = eval(dml)
                else:
                    try: 
                        dml = int(dml)
                    except ValueError:
                        print("leave string a string")
                insertions.update({keynames[i]: dml})
        res = collection.insert(insertions)
    elif dmls[0].lower() == "update":
        for i, dml in enumerate(dmls, 0):
            if i > 0 and conditions[i]:
                if '!=' in conditions[i]:
                    conditions[i] = conditions[i].replace("!=", "").strip()
                    selections.update({keynames[i]: {"$ne": conditions[i]}})
                elif '>=' in conditions[i]:
                    conditions[i] = conditions[i].replace(">=", "").strip()
                    selections.update({keynames[i]: {"$gte": int(conditions[i])}})
                elif '>' in conditions[i]:
                    conditions[i] = conditions[i].replace(">", "").strip()
                    selections.update({keynames[i]: {"$gt": int(conditions[i])}})
                elif '<=' in conditions[i]:
                    conditions[i] = conditions[i].replace("<=", "").strip()
                    selections.update({keynames[i]: {"$lte": int(conditions[i])}})
                elif '<' in conditions[i]:
                    conditions[i] = conditions[i].replace("<", "").strip()
                    selections.update({keynames[i]: {"$lt": int(conditions[i])}})
                elif 'like' in conditions[i].lower():
                    conditions[i] = conditions[i].replace("like", "").replace("Like", "").replace("LIKE", "").strip()
                    conditions[i] = conditions[i].replace("'", "")
                    if conditions[i][0] == "%" and conditions[i][len(conditions[i])-1] == "%":
                        conditions[i] = conditions[i].replace("%", "")
                    elif conditions[i][0] == "%" and conditions[i][len(conditions[i])-1] != "%":
                        conditions[i] = conditions[i].replace("%", "")
                        conditions[i] += "$"
                    elif conditions[i][0] != "%" and conditions[i][len(conditions[i])-1] == "%":
                        conditions[i] = conditions[i].replace("%", "")
                        conditions[i] = "^" + conditions[i]
                    selections.update({keynames[i]: {"$regex": conditions[i]}})
                elif '=' in conditions[i] or '' in conditions[i]: # default is =
                    conditions[i] = conditions[i].replace("=", "").strip()
                    try: 
                        conditions[i] = int(conditions[i])
                    except ValueError:
                        print("leave string a string")
                    selections.update({keynames[i]: {"$eq": conditions[i]}})
                updates.update({keynames[i]: dml})
        updates = {"$set": updates}
        res = collection.update_many(selections, updates)
        res = res.modified_count
    elif dmls[0].lower() == "delete": 
        if messagebox.askyesno(message="Are you sure you want to delete?", icon="question", title="Delete"):
            for i, dml in enumerate(dmls, 0):
                if conditions[i]:
                    if '!=' in conditions[i]:
                        conditions[i] = conditions[i].replace("!=", "").strip()
                        selections.update({keynames[i]: {"$ne": conditions[i]}})
                    elif '>=' in conditions[i]:
                        conditions[i] = conditions[i].replace(">=", "").strip()
                        selections.update({keynames[i]: {"$gte": int(conditions[i])}})
                    elif '>' in conditions[i]:
                        conditions[i] = conditions[i].replace(">", "").strip()
                        selections.update({keynames[i]: {"$gt": int(conditions[i])}})
                    elif '<=' in conditions[i]:
                        conditions[i] = conditions[i].replace("<=", "").strip()
                        selections.update({keynames[i]: {"$lte": int(conditions[i])}})
                    elif '<' in conditions[i]:
                        conditions[i] = conditions[i].replace("<", "").strip()
                        selections.update({keynames[i]: {"$lt": int(conditions[i])}})
                    elif 'like' in conditions[i].lower():
                        conditions[i] = conditions[i].replace("like", "").replace("Like", "").replace("LIKE", "").strip()
                        conditions[i] = conditions[i].replace("'", "")
                        if conditions[i][0] == "%" and conditions[i][len(conditions[i])-1] == "%":
                            conditions[i] = conditions[i].replace("%", "")
                        elif conditions[i][0] == "%" and conditions[i][len(conditions[i])-1] != "%":
                            conditions[i] = conditions[i].replace("%", "")
                            conditions[i] += "$"
                        elif conditions[i][0] != "%" and conditions[i][len(conditions[i])-1] == "%":
                            conditions[i] = conditions[i].replace("%", "")
                            conditions[i] = "^" + conditions[i]
                        selections.update({keynames[i]: {"$regex": conditions[i]}})
                    elif '=' in conditions[i] or '' in conditions[i]: # default is =
                        conditions[i] = conditions[i].replace("=", "").strip()
                        try: 
                            conditions[i] = int(conditions[i])
                        except ValueError:
                            print("leave string a string")
                        selections.update({keynames[i]: {"$eq": conditions[i]}})
            res = collection.delete_many(selections)
            res = res.deleted_count
    else:
        for i, keyname in enumerate(keynames):
            if conditions[i]:
                if '!=' in conditions[i]:
                    conditions[i] = conditions[i].replace("!=", "").strip()
                    selections.update({keynames[i]: {"$ne": conditions[i]}})
                elif '>=' in conditions[i]:
                    conditions[i] = conditions[i].replace(">=", "").strip()
                    selections.update({keynames[i]: {"$gte": int(conditions[i])}})
                elif '>' in conditions[i]:
                    conditions[i] = conditions[i].replace(">", "").strip()
                    selections.update({keynames[i]: {"$gt": int(conditions[i])}})
                elif '<=' in conditions[i]:
                    conditions[i] = conditions[i].replace("<=", "").strip()
                    selections.update({keynames[i]: {"$lte": int(conditions[i])}})
                elif '<' in conditions[i]:
                    conditions[i] = conditions[i].replace("<", "").strip()
                    selections.update({keynames[i]: {"$lt": int(conditions[i])}})
                elif 'like' in conditions[i].lower():
                    conditions[i] = conditions[i].replace("like", "").replace("Like", "").replace("LIKE", "").strip()
                    conditions[i] = conditions[i].replace("'", "")
                    if conditions[i][0] == "%" and conditions[i][len(conditions[i])-1] == "%":
                        conditions[i] = conditions[i].replace("%", "")
                    elif conditions[i][0] == "%" and conditions[i][len(conditions[i])-1] != "%":
                        conditions[i] = conditions[i].replace("%", "")
                        conditions[i] += "$"
                    elif conditions[i][0] != "%" and conditions[i][len(conditions[i])-1] == "%":
                        conditions[i] = conditions[i].replace("%", "")
                        conditions[i] = "^" + conditions[i]
                    selections.update({keynames[i]: {"$regex": conditions[i]}})
                elif '[' in conditions[i] and ']' in conditions[i]:
                    selections.update({keynames[i]: {"$all": eval(conditions[i])}})
                elif '=' in conditions[i] or '' in conditions[i]: # default is =
                    conditions[i] = conditions[i].replace("=", "").strip()
                    try: 
                        conditions[i] = int(conditions[i])
                    except ValueError:
                        pass # leave string a string
                    selections.update({keynames[i]: {"$eq": conditions[i]}})
            if sorts[i]:
                if sorts[i][0:3].lower() == "asc":
                    sort.update({keynames[i]: 1})
                elif sorts[i][0:3].lower() == "des":
                    sort.update({keynames[i]: -1})                
            projections.update({keynames[i]: 1})
        res = collection.find(selections, projections)
        for k, v in sort.items():
            res.sort(k, v)
        res = [ele for ele in res if ele != {}] # filter out blanks
        res = list(res)

    return res

def run_query(frame):
    global collection_name
    global cbvars
    
    keynames = []
    sorts = []
    conditions = []
    dmls = []

    collection_name = collectiontextboxes["0"].get()

    for i, cb in enumerate(cbvars):
        if cbvars[i].get() or conditiontextboxes[str(i)].get() or dmltextboxes[str(i)].get():
            keyname = keytextboxes[str(i)].get()
            sort = sorttextboxes[str(i)].get()
            condition = conditiontextboxes[str(i)].get()
            keynames.append(keyname)
            sorts.append(sort)
            conditions.append(condition)
            dmls.append(dmltextboxes[str(i)].get())

    res = query(db_name, collection_name, keynames, sorts, conditions, dmls)

    textarea2.delete('1.0', END)
    textarea2.insert('1.0', json.dumps(res, indent=4, default=str))

    raise_frame(frame)

def configure(event):
    canvas.after(50, canvas.xview_moveto, 0)

root = Tk()

root.geometry("1100x500")

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
buttonframe = Frame(container1)

scrollableframe.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.after(50, canvas.xview_moveto, 0) # hack to start scollbar at leftmost position
canvas.bind("<Configure>", configure) # and to keep it that way

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

img1 = Image.open(f'{IMAGE_PATH}/play.png')
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
labels["5"] = Label(scrollableframe, text= "DML:")

for i in range(9): # the order you create widgets determines their tab order 
    dmltextboxes[str(i)] = Entry(scrollableframe)

for i in range(9): 
    collectiontextboxes[str(i)] = Entry(scrollableframe)
    keytextboxes[str(i)] = Entry(scrollableframe)
    sorttextboxes[str(i)] = Entry(scrollableframe)
    showcheckboxes[str(i)] = Checkbutton(scrollableframe, variable=cbvars[i])
    conditiontextboxes[str(i)] = Entry(scrollableframe)

checkallbutton = Button(scrollableframe, text="Check All", command=checkall_clicked)
uncheckallbutton = Button(scrollableframe, text="Uncheck All", command=uncheckall_clicked)
clearallbutton = Button(scrollableframe, text="Clear All", command=clear_textboxes_2)

# container2 widgets
img2 = Image.open(f'{IMAGE_PATH}/edit.png')
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
buttonframe.grid(row=6, column=0, sticky='w')

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
labels["5"].grid(row=5, column=0, sticky="e")
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
dmltextboxes["0"].grid(row=5, column=1)
dmltextboxes["1"].grid(row=5, column=2)
dmltextboxes["2"].grid(row=5, column=3)
dmltextboxes["3"].grid(row=5, column=4)
dmltextboxes["4"].grid(row=5, column=5)
dmltextboxes["5"].grid(row=5, column=6)
dmltextboxes["6"].grid(row=5, column=7)
dmltextboxes["7"].grid(row=5, column=8)
dmltextboxes["8"].grid(row=5, column=9)
checkallbutton.grid(row=6, column=1)
uncheckallbutton.grid(row=6, column=2)
clearallbutton.grid(row=6, column=3)

# container2 grid
editbutton.grid(row=0, column=0, sticky="w")
hozline.grid(row=2, column=0, sticky='news')
textarea2.grid(row=3, column=0, sticky="news")

raise_frame(container1)

root.mainloop()