from abc import abstractmethod

from ..entities.admin import Admin

class BaseSystem():
	def __init__(self):
		self._admin = Admin(id='000001', name='admin', email='admin@gmail.com', password='admin')
		self._students = []
		self._subjects = []
		self._is_active = True
		self._active_user = None

	@abstractmethod
	def run(): raise NotImplementedError

	def is_active(self):
		return self._is_active

	def update_active_status(self, new_status):
		self._is_active = new_status

	def load_data(self):
		pass

	def save_file(self):
		pass