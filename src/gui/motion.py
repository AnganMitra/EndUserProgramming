#from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

from Tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
scrollbar.config( command = mylist.yview )
for line in range(10):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )

for line in range(10):
   mylist.insert(END, "This is line number " + str(line))
mainloop()