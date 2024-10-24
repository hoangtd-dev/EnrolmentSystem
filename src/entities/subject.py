import copy

class Subject:
	def __init__(self, id, name):
		self._id = id
		self._name = name

	def get_name(self):
		return copy.copy(self._name)

	def to_dict(self):
		return {
			"id": self._id,
			"name": self._name
		}