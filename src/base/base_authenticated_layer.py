import tkinter as tk
from tkinter import ttk
from abc import abstractmethod
from .base_layer import BaseLayer

class BaseAuthenticatedLayer(BaseLayer):
	def __init__(self, master, system):
		super().__init__(master, system)
		self._system = system

		self.__top_bar_layer = self.__configure_top_bar_layer()
		self.__setup_top_bar_widgets(self.__top_bar_layer)

		self.__side_bar_layer = self.__configure_sidebar_layer()
		self.setup_sidebar_widgets(self.__side_bar_layer)

		self.__content_layer = self.__configure_content_layer()
		self.setup_content_widgets(self.__content_layer)

	def __configure_top_bar_layer(self):
		top_bar_layer = ttk.Frame(self, height=50, borderwidth=1, relief='groove')
		top_bar_layer.pack(side=tk.TOP, fill=tk.X)
		top_bar_layer.pack_propagate(False)
		return top_bar_layer

	def __setup_top_bar_widgets(self, master):
		hello_label = ttk.Label(master, text=f'Hi, {self._system._active_user.get_name()}', padding=10)
		hello_label.pack(side='left')
		
		logout_action = ttk.Label(master, text='Logout', padding=10)
		logout_action.bind("<Button-1>", lambda event: self.navigate('login'))
		logout_action.pack(side='right')

	def __configure_sidebar_layer(self):
		side_bar_layer = ttk.Frame(self, width=200, borderwidth=1, relief='groove')
		side_bar_layer.pack(side=tk.LEFT, fill=tk.Y)
		side_bar_layer.pack_propagate(False)
		return side_bar_layer

	@abstractmethod
	def setup_sidebar_widgets(self, master):
		pass

	def __configure_content_layer(self):
		content_layer = ttk.Frame(self, borderwidth=1, relief='groove', padding=10)
		content_layer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		return content_layer

	@abstractmethod
	def setup_content_widgets(self, master):
		pass

	def create_tabs(self, master, text, is_active=False, next_layout_key=None):
		tab = ttk.Label(master, text=text, padding=20, borderwidth=1, relief='groove', anchor=tk.CENTER)
		tab.pack(fill=tk.X)

		if is_active:
			tab['foreground'] = 'lightblue'
		
		if next_layout_key:
			tab.bind("<Button-1>", lambda event: self.navigate(next_layout_key))

		return tab
