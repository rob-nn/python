# Longevity

from tkinter import *

class Application(Frame):
	""" GUI application which can reveal the secret of longevity. """
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		# create instruction label
		self.inst_lbl = Label(self, text = "Enter password for the secret of longevity")
		self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
		self.pw_lbl = Label(self, text="Passwords: ")
		self.pw_lbl.grid(row=1, column =0, sticky =W)
		self.pw_ent= Entry(self)
		self.pw_ent.grid(row=1, column=1, stick=W)

		self.submit_bttn = Button(self, text="Submit", command=self.reveal)
		self.submit_bttn.grid()

		self.secret_text = Text(self, width=35, height=5, wrap=WORD)

		self.secret_text.grid(row=3, column=1, columnspan=2, sticky=W)

	
	def reveal(self):
		contents = self.pw_ent.get()

		if contents == "secret":
			message = "Here's the secret to livivng to 100: live to 99 and then be VERY careful."
		else:
			message = "That's not the correct password, so I can't share the secret with you."	
		self.secret_text.delete(0.0, END)
		self.secret_text.insert(0.0, message)	


# main
root = Tk()
root.title("Longevity")
root.geometry("300x150")

app = Application(root)
root.mainloop()
