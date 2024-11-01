import tkinter as tk
from tkinter import ttk
from ..base.base_authenticated_layer import BaseAuthenticatedLayer
from ..core.gui_utils import create_custom_table

class SubjectLayout(BaseAuthenticatedLayer):
	def __init__(self, master, system):
		super().__init__(master, system)

	def setup_sidebar_widgets(self, master):
		self.create_tabs(master, text='Enrolment', next_layout_key='student_enrolment')
		self.create_tabs(master, text='Subject', is_active=True)

	def setup_content_widgets(self, master):
		self.__configure_enrolment_list_widgets(master)

	def __configure_enrolment_list_widgets(self, master):
		enrolment_label_frame = ttk.Frame(master, padding=5)
		enrolment_label_frame.pack(fill=tk.X)
		enrolment_label = ttk.Label(enrolment_label_frame, text="Enrolled Subjects: ")
		enrolment_label.pack(side='left')

		enrolment_frame = ttk.Frame(master, padding=10)
		enrolment_frame.pack(fill=tk.BOTH, expand=True)

		active_user = self._system.get_active_user()
		enrolled_subjects = active_user.get_enrolled_subjects()

		columns = {
			'subject_name': 'Subject Name',
			'mark': 'mark',
			'grade': 'grade'
		}

		displayed_enrolled_subjects = []
		for enrolled_subject in enrolled_subjects:
			displayed_enrolled_subjects.append((f'Subject {enrolled_subject.get_id()}', enrolled_subject.get_mark(), enrolled_subject.get_grade()))

		create_custom_table(enrolment_frame, columns, data=displayed_enrolled_subjects)