from tkinter import ttk

class BaseLayer(ttk.Frame):
	def __init__(self, master, **options):
		super().__init__(master, **options)

	def navigate(self, layout_name):
		self.pack_forget()
		self.master.navigate(layout_name)