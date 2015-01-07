import Tkinter as tk

root = tk.Tk()
root.title('Tkinter introduction revision')

lbl = tk.Label(text='Enter your password: ')
lbl.pack()
ent = tk.Entry(width=30)
ent.pack()
mytext = tk.Text(width=30, height=30)
mytext.pack()
scr = tk.Scrollbar(mytext, orient=tk.VERTICAL, command=mytext.yview)
scr.pack()
root.mainloop()

