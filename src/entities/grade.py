import copy
from ..enums.grade_type_enum import GradeTypeEnum

class Grade:
	def __init__(self, mark, type):
		self._mark = mark
		self._type = type

	def get_mark(self):
		return self._mark

	def get_type(self):
		return self._type

	def to_dict(self):
		return {
			"mark": self._mark,
			"type": self._type
		}