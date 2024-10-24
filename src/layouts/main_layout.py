import tkinter as tk
from .login_layout import LoginLayout
from .enrolment_layout import EnrolmentLayout
from .subject_layout import SubjectLayout

class MainLayout(tk.Tk):
	def __init__(self, system):
		super().__init__()
		self._system = system
		self.title('Enrolment System')
		self.__place_at_the_center(width=800, height=500)
		self.navigate('login')

	def __place_at_the_center(self, width, height):
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()

		center_x = int((screen_width-width) / 2)
		center_y = int((screen_height-height) / 2)
		self.geometry(f'{width}x{height}+{center_x}+{center_y}')

	def navigate(self, layer_name):
		match layer_name:
			case 'login':
				LoginLayout(self, self._system).pack(fill=tk.BOTH, expand=True)
			case 'student_enrolment':
				EnrolmentLayout(self, self._system).pack(fill=tk.BOTH, expand=True)
			case 'student_subject':
				SubjectLayout(self, self._system).pack(fill=tk.BOTH, expand=True)
