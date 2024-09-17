from .grade import Grade
class Enrolment:
	def __init__(self, subject):
		self._grade = Grade()
		self._subject = subject

	def get_grade(self):
		return self._grade

	def get_subject(self):
		return self._subject

	def __str__(self):
		return f'{self._subject}: {self._grade}'