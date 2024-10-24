import tkinter as tk
from tkinter import ttk
from ..base.base_authenticated_layer import BaseAuthenticatedLayer
from ..core.gui_utils import create_custom_table

class SubjectLayout(BaseAuthenticatedLayer):
	def __init__(self, master, system):
		super().__init__(master, system)

	def setup_sidebar_widgets(self, master):
		self.create_tabs(master, text='Subject', is_active=True)
		self.create_tabs(master, text='Enrolment', next_layout_key='student_enrolment')

	def setup_content_widgets(self, master):
		self.__configure_enrolment_list_widgets(master)

	def __configure_enrolment_list_widgets(self, master):
		enrolment_label_frame = ttk.Frame(master, padding=5)
		enrolment_label_frame.pack(fill=tk.X)
		enrolment_label = ttk.Label(enrolment_label_frame, text="Enrolment List: ")
		enrolment_label.pack(side='left')

		enrolment_frame = ttk.Frame(master, padding=10)
		enrolment_frame.pack(fill=tk.BOTH, expand=True)

		active_user = self._system.get_active_user()
		enrolments = active_user.get_enrolment_list()

		columns = {
			'subject_name': 'Subject Name',
			'mark': 'mark',
			'grade': 'grade'
		}

		displayed_enrolments = []
		for enrolment in enrolments:
			displayed_enrolments.append((enrolment.get_subject().get_name(), enrolment.get_grade().get_mark(), enrolment.get_grade().get_type()))

		create_custom_table(enrolment_frame, columns, data=displayed_enrolments)