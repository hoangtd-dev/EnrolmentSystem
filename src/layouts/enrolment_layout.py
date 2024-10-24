import tkinter as tk
from tkinter import ttk
from ..base.base_authenticated_layer import BaseAuthenticatedLayer
from ..core.gui_utils import create_custom_table

class EnrolmentLayout(BaseAuthenticatedLayer):
	def __init__(self, master, system):
		super().__init__(master, system)

	def setup_sidebar_widgets(self, master):
		self.create_tabs(master, text='Subject', next_layout_key='student_subject')
		self.create_tabs(master, text='Enrolment', is_active=True)

	def setup_content_widgets(self, master):
		self.__configure_enrolment_list_widgets(master)

	def __configure_enrolment_list_widgets(self, master):
		enrolment_label_frame = ttk.Frame(master, padding=5)
		enrolment_label_frame.pack(fill=tk.X)
		enrolment_label = ttk.Label(enrolment_label_frame, text="Enrolment List: ")
		enrolment_label.pack(side='left')

		enrolment_frame = ttk.Frame(master, padding=10)
		enrolment_frame.pack(fill=tk.BOTH, expand=True)

		columns = {
			'subject_name': 'Subject Name',
			'type': 'Type',
			'score': 'Score'
		}

		# FAKE DATA
		enrolments = []
		for n in range(1, 100):
			enrolments.append((f'subject name {n}', f'type {n}', f'score {n}'))

		create_custom_table(enrolment_frame, columns, data=enrolments)
