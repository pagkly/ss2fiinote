#from Tkinter import *

from tkinter import *
from tkinter import Tk
import tkinter as tk

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()
