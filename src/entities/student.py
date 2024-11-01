from ..enums.role_enum import RoleEnum

from ..base.entities.base_user import BaseUser
from ..core.utils import format_id 

from .subject import Subject

import random

class Student(BaseUser):
	def __init__(self, id, name, email, password, enrolled_subjects = []):
		super().__init__(id, name, email, password, RoleEnum.STUDENT)
		self.__enrolled_subjects = enrolled_subjects

	def get_enrolled_subjects(self):
		return self.__enrolled_subjects
	
	def to_dict(self):
		return {
				"id": self.get_id(),
				"name": self.get_name(),
				"email": self.get_email(),
				"password": self.get_password(),
				"enrolled_subjects": [ enrolled_subject.to_dict() for enrolled_subject in self.__enrolled_subjects ]
		}
  
	@staticmethod
	def create_from_JSON(student):
		enrolled_subjects = [
			Subject(
				enrolled_subject['id'],
				enrolled_subject['mark'],
				enrolled_subject['type']
			) 
			for enrolled_subject in student['enrolled_subjects']
		]

		return Student(
			student['id'],
			student['name'],
			student['email'],
			student['password'],
			enrolled_subjects
		)
	
	@staticmethod
	def register(id, name, email, password):
		return Student(id, name, email, password)
	
	def login(self, email, password):
		return True if self.get_email() == email and self.get_password() == password else False

	def enrol_subject(self):
		if len(self.__enrolled_subjects) >= 4:
			raise ValueError("Students are allowed to enrol in 4 subjects only")

		# Generate subject ID and random mark
		while True:
				# Generate a random subject ID (e.g., between 1 and 999)
				random_id = random.randint(1, 999)

				# Format the subject ID using format_id from utils.py
				subject_id = format_id(3, random_id)  # Convert to 3-digit string, e.g., '012'

				# Check if this subject ID is already in the enrolment list
				if not any(enrolled_subject.get_id() == subject_id for enrolled_subject in self.__enrolled_subjects):
					break  # Exit loop if the ID is unique
		mark = random.randint(25, 100)

		# Create subject and enrolment
		subject = Subject(subject_id, mark)
		self.__enrolled_subjects.append(subject)
  
		return subject_id

  
	def remove_subject(self, subject_id):
		subject_id_to_str = str(subject_id)
    	# Check if the subject exists in the enrolment list
		if not any(enrolled_subject.get_id() == subject_id_to_str for enrolled_subject in self.__enrolled_subjects):
			return False  # Return False if the subject is not found

		new_enrolled_subjects = []
		for enrolled_subject in self.get_enrolled_subjects():
			if enrolled_subject.get_id() != subject_id_to_str:
				new_enrolled_subjects.append(enrolled_subject)
		# Update the enrolment list
		self.__enrolled_subjects = new_enrolled_subjects
		return True

  
	def calculate_average_mark(self):
		if len(self.__enrolled_subjects) == 0:
			return 0

		total_marks = sum([enrolled_subject.get_mark() for enrolled_subject in self.__enrolled_subjects])
		average_mark = total_marks / len(self.__enrolled_subjects)
		return average_mark
