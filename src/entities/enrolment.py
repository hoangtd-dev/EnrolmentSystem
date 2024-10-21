class Enrolment:
	def __init__(self, grade, subject):
		self._grade = grade
		self._subject = subject

	def to_dict(self):
		return {
			"grade": self._grade.to_dict(),
			"subject": self._subject.to_dict()
		}