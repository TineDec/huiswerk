from tkinter import *
from tkinter import OptionMenu

interface = Tk()
interface.configure(bg="#f3da0b")

interface.geometry('100x200')

titel = Label(interface, text="Spelen met Python")
titel.configure(bg="#082fa9", fg="#ffffff", font="Helvetica", padx=50, pady=15)
titel.grid(row=1, column=5)

OptionList = [
    "koekjes",
    "chips",
    "chocolade",
    "zuurtjes",
    "fruit"
]

lekkernijen = StringVar(interface)
lekkernijen.set("Kies iets lekkers")
menu = OptionMenu(interface, lekkernijen, *OptionList)
menu.grid(row=30, column=5, padx=5, pady=5)

naam = Label(interface, text="Wat is je naam?")
naam.configure(bg="#f3da0b", fg="#082fa9", font="Verdana", padx=50, pady=15, borderwidth=2, relief="groove")
naam.grid(row=10, column=5, padx=50, pady=15)
input = Entry(interface)
input.grid(row=10, column=6, padx=50, pady=15)

def invoer():
    info = Label(interface, text="Goedemorgen " + input.get(), fg="white", bg="orange",borderwidth=10, font=('Helvetica', 15))
    info.grid(row=10, column=15)

DIT = Button(interface, text="GO!", fg="white", bg="#082fa9",borderwidth=10, font=('Helvetica', 10), command=invoer)
DIT.grid(row=10, column=7)

labelTest = Label(text="", font=('Helvetica', 12), fg='red')

def callback(*args):
    labelTest.configure(text="Je snoept graag {}".format(lekkernijen.get()), fg="white", bg="orange",borderwidth=10, font=('Helvetica', 15))
    labelTest.grid(row=40, column=15)

lekkernijen.trace("w", callback)

DIT = Button(interface, text="START!", fg="white", bg="#082fa9",borderwidth=10, font=('Helvetica', 10), command=callback)
DIT.grid(row=40, column=7)


interface.mainloop()