# Labeler

from tkinter import *

root = Tk()
root.title("testing")
root.geometry("250x250")
app = Frame(root)
app.grid()

label = Label(app, text = "testing...")
label.grid()

root.mainloop()
