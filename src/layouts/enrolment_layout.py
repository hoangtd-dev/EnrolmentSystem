import tkinter as tk
from tkinter import ttk
from ..base.base_authenticated_layer import BaseAuthenticatedLayer

from tkinter.messagebox import showerror, showinfo

class EnrolmentLayout(BaseAuthenticatedLayer):
	def __init__(self, master, system):
		super().__init__(master, system)

	def setup_sidebar_widgets(self, master):
		self.create_tabs(master, text='Enrolment', is_active=True)
		self.create_tabs(master, text='Subject', next_layout_key='student_subject')

	def setup_content_widgets(self, master):
		self.__configure_enroll_btn(master)

	def __configure_enroll_btn(self, master):
		action_frame = ttk.Frame(master, padding=5)
		action_frame.pack(fill=tk.X)

		clear_all_btn = ttk.Button(action_frame, text="Enrol new subject", command=self.__enrol_subject)
		clear_all_btn.pack(side='left')
	
	def __enrol_subject(self):
		active_user = self._system.get_active_user()
		try:
			subject_id = active_user.enrol_subject()
			self._system.save_changes()

			current_enrolment_count = len(active_user.get_enrolled_subjects())
			showinfo(message=f'Enrolling in Subject-{subject_id}. \n You are now enrolled in {current_enrolment_count} out of 4 subjects')

		except ValueError as e:
			showerror(title='Error', message=e)

