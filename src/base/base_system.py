from abc import abstractmethod

from ..entities.admin import Admin
from ..entities.database import Database

from ..enums.file_status_enum import FileStatusEnum
from ..entities.file import FileStatus

from ..entities.student import Student

class BaseSystem():
	def __init__(self):
		self._admin = Admin(id='000001', name='admin', email='admin@gmail.com', password='admin')
		self._students = []
		self._subjects = []
		self._is_active = True
		self._active_user = None
		self.__database = Database()

	@abstractmethod
	def run(): raise NotImplementedError

	@abstractmethod
	def load_data(): raise NotImplementedError

	@abstractmethod
	def save_changes(data): raise NotImplementedError

	def is_active(self):
		return self._is_active

	def update_active_status(self, new_status):
		self._is_active = new_status

	def read_file(self):
		file_response = self.__database.read_file()
		if file_response.get_status() == FileStatusEnum.SUCCESS:
			self._students = [Student.create_from_JSON(student) for student in file_response.value()]
			return FileStatus(FileStatusEnum.SUCCESS)
		else:
			return FileStatus(FileStatusEnum.ERROR, file_response.get_error())

	def write_file(self, data):
		file_response = self.__database.write_file(data)

		if file_response.get_status() == FileStatusEnum.SUCCESS:
			return FileStatus(FileStatusEnum.SUCCESS)
		else:
			return FileStatus(FileStatusEnum.ERROR, file_response.get_error())