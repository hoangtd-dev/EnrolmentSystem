from abc import abstractmethod
import copy

from ..entities.admin import Admin
from ..entities.student import Student

from ..enums.role_enum import RoleEnum

class BaseSystem():
	def __init__(self):
		self._admins = [
			Admin(id='000001', name='admin', email='admin@gmail.com', password='admin', role=RoleEnum.Admin)
		]
		self._students = [
			Student(id='000002', name='student 1', email='student1@gmail.com', password='123', role=RoleEnum.Student),
			Student(id='000003', name='student 2', email='student2@gmail.com', password='123', role=RoleEnum.Student)
		]
		self._subjects = []
		self._is_active = True
		self._active_user = None

	@abstractmethod
	def run(): raise NotImplementedError

	def get_all_students(self):
		return copy.deepcopy(self._students)

	def remove_student_by_id(self, student_id):
		new_students = [student for student in self._students if student.get_id() != student_id]
		if len(new_students) == len(self._students):
			return False
		else:
			self._students = new_students
			return True

	def remove_all_students(self):
		self._students = []

	def update_students(self, new_students):
		self._students = new_students

	def is_active(self):
		return self._is_active

	def update_active_status(self, new_status):
		self._is_active = new_status

	def load_data(self):
		pass

	def login(self, email, password):
		users = self._admins + self._students
		for user in users:
			if user.login(email, password):
				self._active_user = user
				return True
		return False

	def logout(self) -> None:
		self._active_user = None
	
	def register_student(self, email, password, name):
		# check email/pass format check_email_format() and check_password_format()
		# generate student id
		# new student
		# get random admin and update in Student.update_admin(admin_id)
		# update admin list
		pass

	def generate_student_id(self):
		# get total student count __get_new_student_id()
		# call generate_id with argument = 6
		pass

	def generate_subject_id(self):
		# get total student count __get_new_subject_id()
		# call generate_id with argument = 3
		pass

	def get_random_subject(self):
		pass

	def save_file(self):
		pass

	def __get_new_student_id(self):
		pass

	def __get_new_subject_id(self):
		pass
	