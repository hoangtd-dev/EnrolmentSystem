from tkinter import ttk

class BaseLayer(ttk.Frame):
	def __init__(self, master, system, **options):
		super().__init__(master, **options)
		self._system = system

	def navigate(self, layout_name):
		self.pack_forget()
		self.master.navigate(layout_name)