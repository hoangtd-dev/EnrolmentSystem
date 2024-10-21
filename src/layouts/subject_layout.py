import tkinter as tk
from tkinter import ttk
from ..base.base_authenticated_layer import BaseAuthenticatedLayer

class SubjectLayout(BaseAuthenticatedLayer):
	def __init__(self, master):
		super().__init__(master)

	def setup_sidebar_widgets(self, master):
		self.create_tabs(master, text='Subject', is_active=True)
		self.create_tabs(master, text='Enrolment', next_layout_key='student_enrolment')

	def setup_content_widgets(self, master):
		self.__configure_enroll_btn(master)

	def __configure_enroll_btn(self, master):
		action_frame = ttk.Frame(master, padding=5)
		action_frame.pack(fill=tk.X)

		clear_all_btn = ttk.Button(action_frame, text="Enrol new subject")
		clear_all_btn.pack(side='left')
