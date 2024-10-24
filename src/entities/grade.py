import copy
from ..enums.grade_type_enum import GradeTypeEnum

class Grade:
	def __init__(self, mark, type):
		self._mark = mark
		self._type = type

	def get_mark(self):
		return copy.copy(self._mark)

	def get_type(self):
		return copy.copy(self._type)

	@staticmethod
	def create():
		random_mark = 99 # TODO: Implement random mark function
		grade_type = GradeTypeEnum.HIGH_DISTINCTION # TODO: Implement assign grade type
		return Grade(random_mark, grade_type)

	def to_dict(self):
		return {
			"mark": self._mark,
			"type": self._type
		}