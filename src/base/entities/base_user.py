class BaseUser:
	def __init__(self, id, name, email, password, role):
		self._id = id
		self._name = name
		self._email = email
		self._password = password
		self._role = role
		self._is_login = False

	def __str__(self):
		return f'id: {self._id} - name: {self._name} - role: {self._role}'
	