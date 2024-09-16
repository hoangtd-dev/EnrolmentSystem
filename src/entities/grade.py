class Grade:
	def __init__(self, id):
		self._id = id
		self._type = None
		self._mark = self.__get_random_mark()
		self.__map_mark_to_grade_type()

	def __get_random_mark(self):
		pass

	def __map_mark_to_grade_type(self):
		pass

	def __str__(self):
		pass