class Grade:
	def __init__(self, mark, type):
		self.__mark = mark
		self.__type = type

	def get_mark(self):
		return self.__mark

	def get_type(self):
		return self.__type

	def to_dict(self):
		return {
			"mark": self.__mark,
			"type": self.__type
		}