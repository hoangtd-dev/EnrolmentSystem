import tkinter as tk
from tkinter import ttk
from ..core.gui_utils import create_input_field
from ..base.base_layer import BaseLayer
from tkinter.messagebox import showerror

class LoginLayout(BaseLayer):
	def __init__(self, master, system):
		super().__init__(master, system, padding=10)
		
		wrapper_layer = ttk.Frame(self)
		wrapper_layer.pack(fill=tk.X)

		self.configure_widgets(master=wrapper_layer)

	def configure_widgets(self, master):
		self._is_email_valid = False
		self._is_password_valid = False
		self._is_login_valid = False

		self._email_input_variable = tk.StringVar()
		self._password_input_variable = tk.StringVar()

		email_layer = ttk.Frame(master)
		email_layer.pack(fill=tk.X)
		(email_input, show_email_error, hide_email_error) = create_input_field(email_layer, label_text='Email:', textvariable=self._email_input_variable, is_focus=True, error_message='Wrong email format')

		password_layer = ttk.Frame(master)
		password_layer.pack(fill=tk.X)
		(password_input, show_password_error, hide_password_error) = create_input_field(password_layer, label_text='Password:', textvariable=self._password_input_variable, error_message='Wrong password format', show="*")

		self._email_input_variable.trace_add('write', lambda *args: self.__email_validation(show_email_error, hide_email_error, args))
		self._password_input_variable.trace_add('write', lambda *args: self.__password_validation(show_password_error, hide_password_error, args))

		button = ttk.Button(master, text="Login", command=lambda: self.__handle_login())
		button.pack(fill=tk.X, expand=True, pady=5)

	def __email_validation(self, show_fn, hide_fn, *args):
		self._is_email_valid = True if self._system.is_email_valid(self._email_input_variable.get()) else False
		if self._is_email_valid:
			hide_fn()
		else:
			show_fn()

	def __password_validation(self, show_fn, hide_fn, *args):
		password = self._password_input_variable.get()
		self._is_password_valid = True if len(password) > 0 and self._system.is_password_valid(password) else False
		if self._is_password_valid:
			hide_fn()
		else:
			show_fn()

	def __handle_login(self):
		if not self._is_password_valid or not self._is_email_valid: return

		password = self._password_input_variable.get()
		email = self._email_input_variable.get()
		students = self._system.get_students()

		for student in students:
			if student.login(email, password):
					self._system.update_active_user(student)

		if self._system.get_active_user():
			self.navigate('student_subject')
		else:
			showerror(title='Error', message='Account does not exist in system.')




