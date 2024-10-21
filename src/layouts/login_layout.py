import tkinter as tk
from tkinter import ttk
from ..core.gui_utils import create_input_field
from ..base.base_layer import BaseLayer

class LoginLayout(BaseLayer):
	def __init__(self, master):
		super().__init__(master, padding=10)
		
		wrapper_layer = ttk.Frame(self)
		wrapper_layer.pack(fill=tk.X)

		self.configure_widgets(master=wrapper_layer)

	def configure_widgets(self, master):
		(email_input, show_email_error) = create_input_field(master, label_text='Email:', is_focus=True, error_message='Wrong email format')
		# show_email_error()

		(password_input, show_password_error) = create_input_field(master, label_text='Password:', error_message='Wrong password format', show="*")
		# show_password_error()

		button = ttk.Button(master, text="Login", command=lambda:self.navigate('student_subject'))
		button.pack(fill=tk.X, expand=True, pady=5)