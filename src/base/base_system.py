from abc import abstractmethod
import copy

from ..entities.admin import Admin
from ..entities.student import Student

from ..core.utils import format_id
from ..core.instants import NUMBER_OF_USER_ID_LENGTH

class BaseSystem():
	def __init__(self):
		self._admins = [
			Admin(id='000001', name='admin', email='admin@gmail.com', password='admin')
		]
		self._students = [
			Student(id='000002', name='student 1', email='student1@gmail.com', password='123'),
			Student(id='000003', name='student 2', email='student2@gmail.com', password='123')
		]
		self._is_active = True
		self._active_user = None

	@abstractmethod
	def run(): raise NotImplementedError

	def is_active(self):
		return self._is_active

	def update_active_status(self, new_status):
		self._is_active = new_status

	def get_all_students(self):
		return copy.deepcopy(self._students)

	def update_students(self, new_students):
		self._students = new_students

	def remove_student_by_id(self, student_id):
		new_students = [student for student in self._students if student.get_id() != student_id]
		
		if len(new_students) == len(self._students):
			return False
		
		self._students = new_students
		return True

	def remove_all_students(self):
		self._students = []

	def load_data(self):
		pass

	def save_file(self):
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
	
	def generate_new_student_id(self):
		next_id = max([int(user.get_id()) for user in self._students + self._admins]) + 1
		return format_id(NUMBER_OF_USER_ID_LENGTH, next_id)

	def register_student(self, id, email, password, name):		
		self._students.append(Student.register(id, name, email, password))

	# WAITING FOR REQUIREMENT
	# def generate_subject_id(self):
	# 	next_id = max([int(subject.get_id()) for subject in self._subjects]) + 1
	# 	return format_id(NUMBER_OF_SUBJECT_ID_LENGTH, next_id)

	# def get_random_subject(self):
	# 	pass