import random
from ..enums.grade_type_enum import GradeTypeEnum
class Grade:
	def __init__(self):
		self._mark = self.__get_random_mark()
		self._type = self.__get_grade_type_by_mark()

	def get_mark(self):
		return self._mark

	def __get_random_mark(self):
		return random.randint(0, 100)

	def __get_grade_type_by_mark(self):
		if self._mark < 50:
			return GradeTypeEnum.FAIL
		elif 50 <= self._mark < 65:
				return GradeTypeEnum.PASS
		elif 65 <= self._mark < 75:
				return GradeTypeEnum.CREDIT
		elif 75 <= self._mark < 85:
				return GradeTypeEnum.DISTINCTION
		else:
				return GradeTypeEnum.HIGH_DISTINCTION

	def __str__(self):
		return f'{self._mark} ({self._type})'