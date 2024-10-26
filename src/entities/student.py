import copy
from ..enums.role_enum import RoleEnum

from ..base.entities.base_user import BaseUser
from ..enums.grade_type_enum import GradeTypeEnum


from .enrolment import Enrolment
from .subject import Subject
from .grade import Grade

import random

class Student(BaseUser):
	def __init__(self, id, name, email, password, enrolment_list = []):
		super().__init__(id, name, email, password, RoleEnum.STUDENT)
		self._enrolment_list = enrolment_list

	def get_enrolment_list(self):
		return copy.deepcopy(self._enrolment_list)
	
	def to_dict(self):
		return {
				"id": self._id,
				"name": self._name,
				"email": self._email,
				"password": self._password,
				"enrolment_list": [ enrolment.to_dict() for enrolment in self._enrolment_list ]
		}
  
	def from_dict(student_dict):
		enrolment_list = [
			Enrolment(
				Grade(enrolment['grade']['mark'], enrolment['grade']['type']),
				Subject(enrolment['subject']['id'], enrolment['subject']['name'])
			)
			for enrolment in student_dict['enrolment_list']
		]
		return Student(
			student_dict['id'],
			student_dict['name'],
			student_dict['email'],
			student_dict['password'],
			enrolment_list
		)
	
	@staticmethod
	def create_from_JSON(student):
		enrolment_list = [
			Enrolment(
				Grade(enrolment['grade']['mark'], enrolment['grade']['type']),
				Subject(enrolment['subject']['id'], enrolment['subject']['name'])
			) 
			for enrolment in student['enrolment_list']
		]

		return Student(
			student['id'],
			student['name'],
			student['email'],
			student['password'],
			enrolment_list
		)
	
	@staticmethod
	def register(id, name, email, password):
		return Student(id, name, email, password)
	
	def update_password(self, new_password):
		self._password = new_password
	
	def login(self, email, password):
		return True if self._email == email and self._password == password else False

	def enrol_subject(self, subject_name):
		if len(self._enrolment_list) >= 4:
			raise ValueError("Maximum enrolment of 4 subjects reached")

		# Generate subject ID and random mark
		subject_id = random.randint(1, 999)
		mark = random.randint(25, 100)

		# Determine grade based on the mark
		if mark >= 85:
			grade_type = GradeTypeEnum.HIGH_DISTINCTION
		elif mark >= 75:
			grade_type = GradeTypeEnum.DISTINCTION
		elif mark >= 65:
			grade_type = GradeTypeEnum.CREDIT
		elif mark >= 50:
			grade_type = GradeTypeEnum.PASS
		else:
			grade_type = GradeTypeEnum.FAIL

		# Create subject and enrolment
		subject = Subject(subject_id, subject_name)
		grade = Grade(mark, grade_type)
		enrolment = Enrolment(grade, subject)
		self._enrolment_list.append(enrolment)

		# Recalculate the average mark
		self.calculate_average_mark()

  
	def remove_subject(self, subject_id):
		# Find and remove the subject by ID
		self._enrolment_list = [
			enrolment for enrolment in self._enrolment_list if enrolment.subject.get_id() != subject_id
		]
		self.calculate_average_mark()

	def calculate_average_mark(self):
		if not self._enrolment_list:
			return 0

		total_marks = sum([enrolment.grade.get_mark() for enrolment in self._enrolment_list])
		average_mark = total_marks / len(self._enrolment_list)
		print(f"Updated average mark for {self._name}: {average_mark}")
		return average_mark
