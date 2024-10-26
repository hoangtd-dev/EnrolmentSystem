class Enrolment:
	def __init__(self, grade, subject):
		self.__grade = grade
		self.__subject = subject

	def get_grade(self):
		return self.__grade

	def get_subject(self):
		return self.__subject

	def to_dict(self):
		return {
			"grade": self.__grade.to_dict(),
			"subject": self.__subject.to_dict()
		}