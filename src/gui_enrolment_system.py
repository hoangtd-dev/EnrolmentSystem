from .base.base_system import BaseSystem
from .layouts.main_layout import MainLayout

from .enums.file_status_enum import FileStatusEnum

from tkinter.messagebox import showerror

class GuiEnrolmentSystem(BaseSystem):
	def __init__(self):
		super().__init__()

	def run(self):
		self.load_data()
		root = MainLayout(self)
		root.mainloop()

	# SAVE AND LOAD DATA SECTION
	def load_data(self):
		file_response = self.read_file()
		if file_response.get_status() == FileStatusEnum.ERROR:
			showerror(title='Error', message='Cannot load data from database')
	
	def save_changes(self):
		file_response = self.write_file(self.get_students())

		if file_response.get_status() == FileStatusEnum.SUCCESS:
			self.load_data()
		else:
			showerror(title='Error', message='Cannot save data to database')
	# END SAVE AND LOAD DATA SECTION