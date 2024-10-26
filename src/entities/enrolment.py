import copy

class Enrolment:
	def __init__(self, grade, subject):
		self.grade = grade
		self.subject = subject

	def get_grade(self):
		return copy.deepcopy(self._grade)

	def get_subject(self):
		return copy.deepcopy(self._subject)

	def to_dict(self):
		return {
			"grade": self.grade.to_dict(),
			"subject": self.subject.to_dict()
		}