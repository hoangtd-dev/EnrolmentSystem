class BaseUser:
	def __init__(self, id, name, email, password, role):
		self._id = id
		self._name = name
		self._email = email
		self._password = password
		self._role = role
		self._is_login = False

	def get_id(self):
		return self._id
	
	def get_email(self):
		return self._email
	
	def get_password(self):
		return self._password
	
	def get_name(self):
		return self._name
	
	def __str__(self):
		return f'id: {self._id} - name: {self._name} - role: {self._role}'
	