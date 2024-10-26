class Enrolment:
	def __init__(self, grade, subject):
		self.grade = grade
		self.subject = subject

	def to_dict(self):
		return {
			"grade": self.grade.to_dict(),
			"subject": self.subject.to_dict()
		}