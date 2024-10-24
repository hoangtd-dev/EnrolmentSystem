from .base.base_system import BaseSystem
from .layouts.main_layout import MainLayout

from .enums.file_status_enum import FileStatusEnum

class GuiEnrolmentSystem(BaseSystem):
	def run(self):
		self.load_data()
		root = MainLayout(self)
		root.mainloop()

	# SAVE AND LOAD DATA SECTION
	def load_data(self):
		file_response = self.read_file()
		if file_response.get_status() == FileStatusEnum.ERROR:
			# Show error with notification layout
			pass
	
	def save_changes(self):
		file_response = self.write_file(self._students)

		if file_response.get_status() == FileStatusEnum.SUCCESS:
			self.load_data()
		else:
			# Show error with notification layout
			pass
	# END SAVE AND LOAD DATA SECTION