from ..enums.role_enum import RoleEnum

from ..base.entities.base_user import BaseUser

from .enrolment import Enrolment
from .subject import Subject
from .grade import Grade


class Student(BaseUser):
	def __init__(self, id, name, email, password, enrolment_list = []):
		super().__init__(id, name, email, password, RoleEnum.STUDENT)
		self._enrolment_list = enrolment_list
	
	def to_dict(self):
		return {
				"id": self._id,
				"name": self._name,
				"email": self._email,
				"password": self._password,
				"enrolment_list": [ enrolment.to_dict() for enrolment in self._enrolment_list ]
		}
	
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
