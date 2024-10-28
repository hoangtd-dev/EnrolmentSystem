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
		self.__admin = Admin(id='000001', name='admin', email='admin@gmail.com', password='admin')
		self.__students = []
		self.__is_active = True
		self.__active_user = None
		self.__database = Database()

	@abstractmethod
	def run(): raise NotImplementedError

	@abstractmethod
	def load_data(): raise NotImplementedError

	@abstractmethod
	def save_changes(): raise NotImplementedError

	def get_students(self):
		return self.__students
	
	def update_students(self, new_students):
		self.__students = new_students

	def get_active_user(self):
		return self.__active_user

	def get_admin(self):
		return self.__admin

	def update_active_user(self, active_user):
		self.__active_user = active_user

	def is_active(self):
		return self.__is_active

	def update_active_status(self, new_status):
		self.__is_active = new_status

	def read_file(self):
		file_response = self.__database.read_file()
		if file_response.get_status() == FileStatusEnum.SUCCESS:
			self.__students = [Student.create_from_JSON(student) for student in file_response.value()]

			if self.__active_user:
				self.__active_user = next((student for student in self.__students if self.__active_user.get_id() == student.get_id()), None)

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
		self.__students.append(new_student)

	def check_duplicate_email(self, email):
		for student in self.__students:
			if student.get_email() == email:
				return student.get_name()
			
		return None

	def is_email_valid(self, email):
		return re.match(r"^[a-zA-Z]+\.[a-zA-Z]+@university\.com$", email) is not None

	def is_password_valid(self, password):
		return (len(password) != 0 and
				password[0].isupper() and
				len(password) >= 8 and
				len(re.findall(r'[a-zA-Z]', password)) >= 5 and
				len(re.findall(r'\d', password)) >= 3)

	def generate_unique_id(self, str_len):  
		while True:
			id = random.randint(1, 999999)
			id_str = format_id(str_len, id)  
			if id_str and id_str not in [student.get_id() for student in self.__students]: 
				return id_str
			
	def logout(self):
		self.__active_user = None
