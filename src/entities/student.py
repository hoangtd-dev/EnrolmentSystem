from ..enums.role_enum import RoleEnum

from ..base.entities.base_user import BaseUser
from ..core.utils import format_id 

from .enrolment import Enrolment
from .subject import Subject
from .grade import Grade

import random

class Student(BaseUser):
	def __init__(self, id, name, email, password, enrolment_list = []):
		super().__init__(id, name, email, password, RoleEnum.STUDENT)
		self.__enrolment_list = enrolment_list

	def get_enrolment_list(self):
		return self.__enrolment_list
	
	def to_dict(self):
		return {
				"id": self.get_id(),
				"name": self.get_name(),
				"email": self.get_email(),
				"password": self.get_password(),
				"enrolment_list": [ enrolment.to_dict() for enrolment in self.__enrolment_list ]
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
				Subject(enrolment['subject']['id'])
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
	
	def login(self, email, password):
		return True if self.get_email() == email and self.get_password() == password else False

	def enrol_subject(self):
		if len(self.get_enrolment_list()) >= 4:
			raise ValueError("Maximum enrolment of 4 subjects reached")

		# Generate subject ID and random mark
		while True:
				# Generate a random subject ID (e.g., between 1 and 999)
				random_id = random.randint(1, 999)

				# Format the subject ID using format_id from utils.py
				subject_id = format_id(3, random_id)  # Convert to 3-digit string, e.g., '012'

				# Check if this subject ID is already in the enrolment list
				if not any(enrolment.get_subject().get_id() == subject_id for enrolment in self.get_enrolment_list()):
					break  # Exit loop if the ID is unique
		mark = random.randint(25, 100)

		# Create subject and enrolment
		subject = Subject(subject_id)
		grade = Grade(mark)
		enrolment = Enrolment(grade, subject)
		self.__enrolment_list.append(enrolment)
  
		return subject_id

  
	def remove_subject(self, subject_id):
     
		subject_id_to_str = str(subject_id)
    	# Check if the subject exists in the enrolment list
		enrolment_list = self.get_enrolment_list()
		if not any(enrolment.get_subject().get_id() == subject_id_to_str for enrolment in enrolment_list):
			return False  # Return False if the subject is not found

		new_enrolment_list = []
		for enrolment in self.get_enrolment_list():
			if enrolment.get_subject().get_id() != subject_id_to_str:
				new_enrolment_list.append(enrolment)
		# Update the enrolment list
		self.__enrolment_list = new_enrolment_list
		return True

  
	def calculate_average_mark(self):
		if len(self.get_enrolment_list) == 0:
			return 0

		total_marks = sum([enrolment.get_grade().get_mark() for enrolment in self.__enrolment_list])
		average_mark = total_marks / len(self.__enrolment_list)
		return average_mark
