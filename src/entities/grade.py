from ..enums.grade_type_enum import GradeTypeEnum

class Grade:
	def __init__(self, mark, grade_type=None):
		self.__mark = mark
		self.__grade_type = grade_type if grade_type else self.get_classify_grade(mark)

	def get_mark(self):
		return self.__mark

	def get_type(self):
		return self.__grade_type

	@staticmethod
	def get_classify_grade(mark):
		"""Classifies the grade type based on the mark."""
		if mark >= 85:
			return GradeTypeEnum.HIGH_DISTINCTION
		elif mark >= 75:
			return GradeTypeEnum.DISTINCTION
		elif mark >= 65:
			return GradeTypeEnum.CREDIT
		elif mark >= 50:
			return GradeTypeEnum.PASS
		else:
			return GradeTypeEnum.FAIL


	def to_dict(self):
		return {
			"mark": self.__mark,
			"type": self.__grade_type
		}