import re
import random
from abc import abstractmethod

from ..entities.admin import Admin
from ..entities.database import Database

from ..enums.file_status_enum import FileStatusEnum
from ..entities.file import FileStatus

from ..entities.student import Student
from ..core.utils import format_id

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
	def save_changes(): raise NotImplementedError

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
		
	def register_student(self, name, email, password):
		unique_id = self.generate_unique_id(6)
		new_student = Student.register(unique_id, name, email, password)
		self._students.append(new_student)

	def check_duplicate_email(self, email):
		for student in self._students:
			if student.get_email() == email:
				return student.get_name()
			
		return None

	def is_email_valid(self, email):
		return re.match(r"^[a-zA-Z]+\.[a-zA-Z]+@university\.com$", email) is not None

	def is_password_valid(self, password):
		return (password[0].isupper() and
				len(password) >= 8 and
				len(re.findall(r'[a-zA-Z]', password)) >= 5 and
				len(re.findall(r'\d', password)) >= 3)

	def generate_unique_id(self, str_len):  
		while True:
			id = random.randint(1, 999999)
			id_str = format_id(str_len, id)  
			if id_str and id_str not in [student.get_id() for student in self._students]: 
				return id_str
			
	def logout(self):
		self._active_user = None
