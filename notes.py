from tkinter import *
import threading
import time

i=0
index =0
def buttonAddDef():
	#print (message.get())
	listbox.insert(END,time.get()[0:5].strip()+ ' '+ message.get().strip())
	print (listbox.get(0, END)[0])


def tick ():
	global i	
#	time.sleep(1)
	if i%2 == 0: 
		root.iconbitmap('folder2.ico')
	else:
		root.iconbitmap('folder.ico')
	i=i+1
	
	root.after(1000, tick)

def buttonDelDef():
	print(listbox.curselection())
	listbox.delete(listbox.curselection())

def buttonChangeDef():
	listbox.insert(listbox.curselection(), time.get()[0:5].strip() + ' '+ message.get().strip() )
	listbox.delete(listbox.curselection())
	

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    global index
    w = evt.widget
    if len(w.curselection()) == 0:
    	listbox.select_set(index)
    	return
    index = int(w.curselection()[0])
    value = w.get(index)
    time.set(value[0:5].strip())
    message.set(value[5:].strip())
    print ('You selected item %d: "%s"' % (index, value))

root=Tk()
root.title("Напоминатор v 20180302")
root.iconbitmap('folder.ico')
root.geometry("300x250")
# ENTRY
label = Label(root, text="Время").grid(row=0, column=1,sticky=W)
label = Label(root, text="КИ").grid(row=0, column=2,sticky=W)

message = StringVar() 
time = StringVar() 
message_time = Entry(root,textvariable=time,width=7).grid(row=1, column=1,sticky=W)
message_MSG = Entry(root,textvariable=message,width=40).grid(row=1, column=2,sticky=W)
#message_entry.place(relx=.5, rely=.1, anchor="c")
#message_entry.pack()

# кнопка по умолчанию
#button1 = Button(root,text=u"Добавить задание", command='')
#button1.pack()
# кнопка с указанием родительского виджета и несколькими аргументами
buttonAdd = Button(root, bg="green", text=u"Добавить!", command=buttonAddDef).grid(row=2, column=2,sticky=W)
buttonDel = Button(root, bg="red", text=u"Удалить!", command=buttonDelDef).grid(row=2, column=2)
buttonChange = Button(root, bg="grey", text=u"Изменить!", command=buttonChangeDef).grid(row=2, column=2,sticky=E)

listbox = Listbox(root,name = 'listbox' )
listbox.bind('<<ListboxSelect>>', onselect)
listbox.grid(row=4, column=1,columnspan=2,sticky=W+E+N+S) #pack(fill=BOTH, expand=2)

for i in range(5):
    listbox.insert(END, "TIME " + str(i))

root.after(1, tick)
root.mainloop()