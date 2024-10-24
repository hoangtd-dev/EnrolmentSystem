from .base.base_system import BaseSystem
from .layouts.main_layout import MainLayout

class GuiEnrolmentSystem(BaseSystem):
	def __init__(self):
		super().__init__()

	def run(self):
		root = MainLayout()
		root.mainloop()

	def save_changes():
		pass
	
	def load_data():
		pass