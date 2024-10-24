import copy

class Enrolment:
	def __init__(self, grade, subject):
		self._grade = grade
		self._subject = subject

	def get_grade(self):
		return copy.deepcopy(self._grade)

	def get_subject(self):
		return copy.deepcopy(self._subject)

	def to_dict(self):
		return {
			"grade": self._grade.to_dict(),
			"subject": self._subject.to_dict()
		}