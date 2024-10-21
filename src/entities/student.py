from ..enums.role_enum import RoleEnum

from ..base.entities.base_user import BaseUser

class Student(BaseUser):
	def __init__(self, id, name, email, password):
		super().__init__(id, name, email, password, RoleEnum.STUDENT)
		self._enrolment_list = []